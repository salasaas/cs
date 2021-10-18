import re
import sys

class Node:
  def __init__(self, data):
    self.children = []
    self.parent = None
    self.data = data
  
  def addChild(self, child):
    child.parent = self
    self.children.append(child)

  def level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    return level

  def displayTee(self):
    tab = '\t' * self.level()
    print(tab + self.data)
    if self.children:
      for child in self.children:
        child.print_tree()


def main(argv):
  try:
    input = open(sys.argv[1], 'r')
  except open.error as msg:
    print("Unable to Open Text File")
    print("Description: " + str(msg))

  output = open(sys.argv[2], 'w')
  output.write("Tokens:\n")

  while True:
    try:
      line = input.readline()
    except:
      print("Unable to read line.")

    if not line:
      break
    
    string, tokens = scanner(line)
    output.write(string)
  

  input.close()
  output.close()


def scanner(line):
  identifier = re.compile('[a-zA-Z][a-zA-Z0-9]*')
  number = re.compile('[0-9]+')
  symbol = re.compile('[\\* | \\+ | \\- | \\( | \\) | \\/ \\:= \\;]')
  whitespace = " "
  leftP = re.compile('[\\(]')


  


  filterStr = ''.join((filter(lambda x: x not in ['(', ')'], line)))
  lineList = filterStr.split(whitespace)

  string = ""
  token = ""

  i = 0
  while i < len(lineList):
    if identifier.match(lineList[i]):
      token += lineList[i]
      string = string + lineList[i] + " : Identifier\n"   
    elif number.match(lineList[i]):
      token += lineList[i]
      string = string + lineList[i] + " : Number\n"
    
    elif symbol.match(lineList[i]):
      token += lineList[i]
      string = string + lineList[i] + " : Symbol\n"

    else:
      token += lineList[i]
      string = string + lineList[i] + " : Error\n"
    
    i += 1
  
  return string, token


if __name__ == "__main__":
    main(sys.argv[1:])
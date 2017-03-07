# python3

import sys

#Typical implementation of Stack
class Stack:

    def __init__(self):
        self.stack = []
        self.countAllTime = 0
        
    def push(self, key):
        self.countAllTime = self.countAllTime + 1
        return self.stack.append(key)
        
    def pop(self):
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def clearStack(self):
        self.countAllTime = 0
        self.stack = []
                        
    def numElems(self):
        return len(self.stack)
            
    def __str__(self):
        return str(self.stack)

#Bracket object represents any of the opening brackets: {, [, (
class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False
    
    def __str__(self):
        return str(self.bracket_type)+ " " + str(self.position)

if __name__ == "__main__":
    text = sys.stdin.read()

    brackets_stack = Stack()
    last = False
    mismatch = False
    
    for i, next in enumerate(text):
        #create Bracket objects only with opening brackets
        if next == '(' or next == '[' or next == '{':
            brackets_stack.push(Bracket(next, i))
        #if a closing bracket encountered then 
        #it's either a mismatch if the stack is empty
        #or a match if topmost bracket matches the closing bracket
        if next == ')' or next == ']' or next == '}':
            if brackets_stack.empty():
                print(i+1)
                mismatch = True
                break
            top = brackets_stack.pop()
            if not (top.Match(next)):
                print(i+1)
                mismatch = True
                break

    #If stack of brackets is not empty, but no mismatch 
    #print the position of the last symbol
    #This is a corner case when number of opening brackets
    #is larger than the number of closing
    if not brackets_stack.empty() and not mismatch:
        print(brackets_stack.stack[-1].position + 1)
    
    #If text has brackets balanced out then print "Success"
    if brackets_stack.empty() and not mismatch: 
        print("Success")


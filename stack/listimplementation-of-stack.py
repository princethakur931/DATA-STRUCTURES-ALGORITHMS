# implementation of stack using list or array where append work like push operation and pop works like pop operation in stack.

class stack:
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return print('stack is empty')
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return 'stack is empty. so there is no top most element!!'
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isempty(self):
        return len(self.stack) == 0

    def printstack(self):
        print(self.stack)

s = stack()
# # s.push(4)
# # s.push(6)
# # s.push(10)
# s.printstack()
# s.pop()
# s.printstack()
# print(s.top())
# print(s.size())
s.isempty()
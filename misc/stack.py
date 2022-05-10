class Stack(object):
    stack = []

    def pop(self):
        lastItem = self.stack[-1]
        self.stack = self.stack[0:len(self.stack)-1]
        return lastItem
    
    def push(self, item):
        self.stack.append(item)
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

s = Stack()
print(s.isEmpty())
s.push(5)
print(s.isEmpty())
val = s.pop()
print(val)

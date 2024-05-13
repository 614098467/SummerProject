
class MyStack(object):
    def __init__(self):
        self.stack = []
    def IsEmpty(self):
        return len(self.stack) == 0

    def GetSize(self):
        return len(self.stack)

    def Push(self,number):
        self.stack.append(number)

    def Pop(self):
        if self.IsEmpty():print("Stack  empty")
        else:self.stack.pop()

    def Display(self):
        if self.IsEmpty():print("Stack  empty")
        else:return self.stack

    def Top(self):
        if self.IsEmpty():print("Stack is empty")
        else:print(self.stack[-1])

    def Clear(self):
        self.stack = []

    def Contains(self,item):
        return item in self.stack

    def ToArray(self):
        return list(self.stack)

    def ToString(self):
        return str(self.stack)

    def Reverse(self):
        return self.stack.reverse()









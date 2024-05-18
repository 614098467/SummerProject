
'''
基于顺序表
完成栈'''
class MyStack(object):
    def __init__(self):
        self.stack = []

    def GetSize(self):
        return len(self.stack)

    def Push(self,value):
        self.stack.append(value)

    def Remove(self,value):
        if value in self.stack:
            self.stack.remove(value)
        else:
            raise ValueError("Value not in stack")

    def RemoveAll(self):
        self.stack = []

    def RemoveIndex(self,index):
        if index < 0 or index > len(self.stack): raise IndexError("Index out of range")
        else:self.stack.pop(index)

    def Pop(self):
        self.stack.pop()

    def GetTop(self):
        return self.stack[-1]


    def __str__(self):
        value = []
        for i in range(len(self.stack)):
            value.append(str(self.stack[i]))

        return " " .join(value)


stack = MyStack()

stack.Push(2)
stack.Push(5)
stack.Push(8)
stack.Push(2)
stack.Push(5)
stack.Push(8)
stack.Push(2)
stack.Push(5)
stack.Push(8)
stack.Pop()

stack.Remove(2)
stack.Remove(2)

stack.RemoveIndex(2)

print(stack.GetTop())
print(stack)

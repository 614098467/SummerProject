
'''顺序表实现'''
class MyQueue(object):

    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    def Push(self,number):
        self.data.append(number)
        self.tail  += 1

    def Pop(self):
        if self.empty() :return "Queue is empty"
        else:
            value = self.data[self.head]
            self.head += 1
        return value

    def GetTop(self):
        if self.empty(): return "Queue is empty"
        else: return self.data[self.head]

    def GetSize(self):
        return self.tail - self.head

    def empty(self):
        return self.head == self.tail

    def __str__(self):
        val = []
        for i in range(self.head,self.tail):
            val.append(str(self.data[i]))
        return ' '.join(val)



queue = MyQueue()
queue.Push(2)
queue.Push(4)
queue.Push(6)
queue.Push(8)
queue.Pop()
print(queue.GetTop())
print(queue.GetSize())
print(queue)





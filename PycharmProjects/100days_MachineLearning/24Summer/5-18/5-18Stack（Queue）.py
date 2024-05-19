
'''
用两个队列 完成栈的编写
'''
from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.size = 0

    def Empty(self):
        return self.size == 0

    def Push(self,value):
        self.q1.append(value)
        self.size += 1

    def Pop(self):
        if self.Empty():raise ValueError("Empty")
        elif self.size == 1:self.q1.pop()
        else:
            for _ in range(self.size-1):
                value = self.q1.popleft()
                self.q2.append(value)
            self.q1.popleft()
            for _ in range(self.size-1):
                value = self.q2.popleft()
                self.q1.append(value)
            self.size -= 1

    def __str__(self):
        val = []
        if self.Empty():raise ValueError("Empty")
        else:
            for _ in range(self.size):
                value = self.q1.popleft()
                val.append(str(value))
        return " ".join(val)





q = deque()
q.append(2)
q.append(4)
q.append(6)
q.append(4)
q.append(8)
print(q)
print(q.index(4))
print(q.count(8))






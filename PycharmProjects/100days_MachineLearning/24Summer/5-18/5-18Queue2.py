'''
单向链表实现队列
'''

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class MyQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Push(self,value):
        new_node = ListNode(value)
        if self.head is None:new_node.next = self.head;self.head = new_node
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = new_node
        self.size += 1
    def Empty(self):
        return self.size == 0

    def GetSize(self):
        return self.size

    def Pop(self):
        if self.Empty():raise ValueError("Queue is empty")
        elif self.size == 1:self.head = None
        else:
            currentNode = self.head
            self.head = currentNode.next
        self.size -= 1
    def GetTop(self):
        if self.Empty(): raise ValueError("Queue is empty")
        else:
            return self.head.value

    def __str__(self):
        val = []
        current_node = self.head
        while current_node is not None:
            val.append(str(current_node.val))
            current_node = current_node.next
        return "-".join(val)


Q = MyQueue()
Q.Push(2)
Q.Push(4)
Q.Push(6)
Q.Push(8)
Q.Push(10)
Q.Pop()
print(Q)








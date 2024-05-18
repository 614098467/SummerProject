'''
基于单链表
完成栈
'''


class ListNode(object):
    def __init__(self,value):
        self.value = value
        self.next  = None

class Mystack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def GetSize(self):
        return self.size

    def Push(self,value):
        new_node = ListNode(value)
        if self.head is None:new_node.next = self.head;self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1

    def Empty(self):
        return self.size == 0

    def Pop(self):
        if self.Empty() : raise ValueError("Stack is empty")
        elif self.size == 1:self.head = None
        else:
            sentinel = ListNode(0)
            sentinel.next = self.head
            current_node = self.head
            while current_node.next is not None:
                sentinel = sentinel.next
                current_node = current_node.next
            sentinel.next = None
        self.size -= 1

    def Change(self,index,value):
        if self.Empty(): raise ValueError("Stack is empty")
        elif index < 0 or index > self.size: raise IndexError("Index out of range")
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.value = value

    def Clear(self):
        self.head = None

    def __str__(self):
        if self.Empty():raise ValueError("Stack is empty")
        else:
            val = []
            current_node = self.head
            while current_node is not None:
                val.append(str(current_node.value))
                current_node = current_node.next
            return "-".join(val)





stack = Mystack()
stack.Push(2)
stack.Push(4)
stack.Push(6)
stack.Push(8)
stack.Pop()
stack.Change(2,1)
print(stack)









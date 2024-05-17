
class LinkNode(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def Add(self,value):
        new_node = LinkNode(value)
        if self.head is None:self.head = new_node;self.size += 1
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            self.size += 1

    def GetSize(self):
        return self.size


    def Insert(self,index,value):
        if index<0 or index> self.size:raise IndexError("Index out of bounds")
        else:
            new_node = LinkNode(value)
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                prev_node = self.head
                for _ in range(index-1):
                    prev_node = prev_node.next
                new_node.next = prev_node.next
                prev_node.next = new_node
            self.size += 1

    def Delete(self,index):
        if index<0 or index>= self.size:raise IndexError("Index out of bounds")
        else:
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            current_node = prev_node.next
            if current_node.next is None:
                prev_node.next = None
            else:
                nexe_node = current_node.next
                prev_node.next = nexe_node
        self.size -= 1

    def Change(self,index,value):
        if index<0 or index>self.size: raise IndexError("Index out of bounds")
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.value = value

    def __str__(self):
        value = []
        current = self.head
        while current is not None:
            value.append(str(current.value))
            current = current.next
        return "->".join(value)



ll = LinkedList()












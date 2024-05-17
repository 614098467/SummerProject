
class LinkNode(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def Add(self,value):
        new_node = LinkNode(value)
        if self.head is None:self.head = new_node;self.size+=1
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1

    def Insert(self,index,value):
        new_node = LinkNode(value)
        if index <0 or index > self.size:raise IndexError("Index out of bounds")
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
            self.size += 1

    def Delete(self,index):
        if index< 0 or index > self.size:raise IndexError("Index out of bounds")
        elif index == 0:
            current_node = self.head
            self.head = current_node.next
            self.size -= 1
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            current_node = prev.next
            if current_node.next is not None:
                prev.next = current_node.next
            else:prev.next = None
            self.size -= 1

    def Change(self,index,value):
        if index < 0 or index > self.size: raise IndexError("Index out of bounds")
        elif index == 0: current_node = self.head;current_node.value = value
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            current_node = prev.next
            current_node.value = value

    def __str__(self):
        value = []
        current_node = self.head
        while current_node is not None:
            value.append(str(current_node.value))
            current_node = current_node.next
        return "->".join(value)



ll = LinkList()
ll.Add(1)
ll.Add(3)
ll.Add(5)
ll.Insert(3,2)
ll.Delete(3)
ll.Change(1,5)
print(ll)







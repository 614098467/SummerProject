
class TreeNode(object):
    def __init__(self,value = None,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.maxNode = 0


    def InsertNode(self,node,value):
        if node is None:
            return TreeNode(value)
        else:
            if value < node.value:
                node.left = self.InsertNode(node.left,value)
            elif value > node.value:
                node.right = self.InsertNode(node.right,value)
            return node

    def Insert(self,value):
        self.root = self.InsertNode(self.root,value)


    def RemoveNode(self,node,value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.RemoveNode(node.left,value)
        elif value > node.value:
            node.right = self.RemoveNode(node.right,value)
        elif value == node.value:
            if node.left is None and node.right is None:
                return None
            elif node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                replace_node = node.right
                while replace_node.left:
                    replace_node = replace_node.left
                node.value = replace_node.value
                node.right = self.RemoveNode(node.right,replace_node.value)
        return node

    def Remove(self,value):
        self.root = self.RemoveNode(self.root,value)


    def SearchNode(self,node,value):
        if not node:
            return False
        if value < node.value:
            return self.SearchNode(node.left,value)
        elif value > node.value:
            return self.SearchNode(node.right,value)
        elif value == node.value:
            return True


    def Search(self,value):
        return self.SearchNode(self.root,value)

    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            print(node.value,end= ' ')
            self.inOrder(node.right)

    def InOrder(self):
        self.inOrder(self.root)




T = BinarySearchTree()
T.Insert(7)
T.Insert(9)
T.Insert(8)
T.Insert(11)
T.Insert(10)
T.Insert(1)
T.Insert(3)
T.Insert(5)
print(T.root.right.right.value)
print(T.Search(5))
T.InOrder()








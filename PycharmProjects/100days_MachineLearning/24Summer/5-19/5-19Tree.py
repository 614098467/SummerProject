
'''
5-19 author：iCake
'''

'''
思路，树是一个大的列表，每一个节点都是一个对象node
'''

class TreeNode(object):
    def __init__(self):
        self.data = None
        self.children = []

    def AddChild(self,nodeId):
        self.children.append(nodeId)

class Tree(object):
    '''初始化一个根节点，并且生成最大节点数个子节点对象放在列表中'''
    def __init__(self,MaxNode):
        self.root = None
        self.nodes = [TreeNode() for _ in range(MaxNode)]

    def GetNode(self,Id):
        return self.nodes[Id]

    def SetRoot(self,rootID):
        root = self.GetNode(rootID)
        self.root = root

    def AddChild(self,ParID,ChiID):
        parent = self.GetNode(ParID)
        child  = self.GetNode(ChiID)
        parent.AddChild(child)

    def AssignValue(self,ID,Value):
        node = self.GetNode(ID)
        node.data = Value

    def DFS(self,node = None):
        if node is None:
            node = self.root
        print(node.data,end = '->')
        for child in node.children:
            self.DFS(child)




T = Tree(8)
T.SetRoot(0)
T.AddChild(0,1)
T.AddChild(0,2)
T.AddChild(1,3)
T.AddChild(1,4)
T.AddChild(2,5)
T.AddChild(2,6)
T.AddChild(3,7)

T.AssignValue(0,0)
T.AssignValue(1,1)
T.AssignValue(2,2)
T.AssignValue(3,3)
T.AssignValue(4,4)
T.AssignValue(5,5)
T.AssignValue(6,6)
T.AssignValue(7,7)


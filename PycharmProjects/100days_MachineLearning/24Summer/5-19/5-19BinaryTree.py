'''
二叉树的构建
'''


'''
节点的构建：
'''

class TreeNode(object):
    def __init__(self,val = None,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self,MaxNode):
        self.root = None
        self.maxNode = MaxNode
        self.nodes = [TreeNode() for _ in range(MaxNode)]

    def GetNode(self,ID):
        return self.nodes[ID]

    def GetValue(self,ID):
        return self.nodes[ID].val

    def Create(self,TreeValueList,TreeSize,SetID):
        if SetID >= TreeSize or TreeValueList[SetID] == None:
            return None
        else:
            nowNode = self.GetNode(SetID)
            nowNode.val = TreeValueList[SetID]
            nowNode.left = self.Create(TreeValueList,TreeSize,SetID*2)
            nowNode.right = self.Create(TreeValueList,TreeSize,SetID*2+1)
            return nowNode

    def CreatTree(self,TreeValueList):
        self.root = self.Create(TreeValueList,len(TreeValueList), 1)

    def PiorLoop(self,a):
        if a >= self.maxNode or self.nodes[a].val == None:
            return None
        else:
            print(self.nodes[a].val)
            self.PiorLoop(a*2)
            self.PiorLoop(a*2+1)




a = [None,'a','b','c','d',None,'e','f','g','h',None,None,None,None,'i']
T = BinaryTree(15)
T.CreatTree(a)
T.PiorLoop(1)



class VertexNode(object):
    def __init__(self,v):
        self.data = v
        self.edge = []

class EdgeNode(object):
    def __init__(self,v,w):
        self.edge = v
        self.weight = w


class Graph(object):
    def __init__(self,n):
        self.n = n
        self.Nodes = [VertexNode(i) for i in range(n)]


    def addEdge(self,u,v,w):
        self.Nodes[u].edge.append(EdgeNode(v,w))


    def printGraph(self):
        for i in range(self.n):
            for j in range(len(self.Nodes[i].edge)):
                print("from",i,"to",self.Nodes[i].edge[j].edge,"weight is",self.Nodes[i].edge[j].weight)

g = Graph(3)
g.addEdge(0,1,2)
g.addEdge(0,2,5)
g.printGraph()



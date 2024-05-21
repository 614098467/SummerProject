

inf = -1
class Graph(object):

    def __init__(self,n):
        self.n = n
        self.Edge = []
        for i in range(n):
            l = []
            for j in range(n):
                l.append(-1)
            self.Edge.append(l)

    def addEdge(self,u,v,w):
        self.Edge[u][v] = w

    def printGraph(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.Edge[i][j],end=' ')
            print('\t')


G = Graph(5)
G.addEdge(0,1,1)
G.addEdge(1,2,3)
G.addEdge(2,4,3)
G.addEdge(3,4,1)
G.addEdge(4,1,2)
G.printGraph()
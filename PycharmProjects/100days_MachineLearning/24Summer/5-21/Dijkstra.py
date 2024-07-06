

class Graph(object):
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrices = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.vertex_data = ['']*num_vertices

    def add_edge(self,u,v,weight):
        if 0 <= u <self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrices[u][v] = weight
            self.adj_matrices[v][u] = weight

    def add_vertex_data(self,v,data):
        if 0 <= v <self.num_vertices:
            self.vertex_data[v] = data

    def dijkstra(self,start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.num_vertices
        distances[start_vertex] = 0
        visit = [False] * self.num_vertices
        for _ in range(self.num_vertices):
            min_distance = float('inf')
            min_index = -1
            for i in range(self.num_vertices):
                if distances[i] < min_distance and not visit[i]:
                    min_distance = distances[i]
                    min_index = i
            visit[min_index] = True
            for i in range(self.num_vertices):
                if self.adj_matrices[min_index][i] > 0 and not visit[i]:
                    new_distanve = distances[min_index] + self.adj_matrices[min_index][i]
                    if new_distanve < distances[i]:
                        distances[i] = new_distanve
        return distances

    def dijkstra_SpanningTree(self, start_vertex_data,studentID):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.num_vertices
        distances[start_vertex] = 0
        visit = [False] * self.num_vertices
        predecessors = [-1] * self.num_vertices

        for _ in range(self.num_vertices):
            min_distance = float('inf')
            current_vertex = -1

            for i in range(self.num_vertices):
                if not visit[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    current_vertex = i

            if current_vertex == -1:
                break

            visit[current_vertex] = True

            for i in range(self.num_vertices):
                if self.adj_matrices[current_vertex][i] > 0 and not visit[i]:
                    if self.adj_matrices[current_vertex][i]+distances[current_vertex] == studentID:
                        new_distance = distances[current_vertex] + self.adj_matrices[current_vertex][i]
                        distances[i] = new_distance
                        predecessors[i] = current_vertex
                        break
                    else:
                        new_distance = distances[current_vertex] + self.adj_matrices[current_vertex][i]
                        if new_distance < distances[i]:
                            distances[i] = new_distance
                            predecessors[i] = current_vertex

        SpanningTree = []
        for i in range(self.num_vertices):
            if predecessors[i] != -1:
                dis = distances[i]
                SpanningTree.append((self.vertex_data[i],self.vertex_data[predecessors[i]],dis))

        return distances,SpanningTree




g = Graph(6)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')

g.add_edge(0, 1, 2)  # A -> B, weight 2
g.add_edge(0, 2, 5)  # A -> C, weight 5
g.add_edge(0, 3, 1)  # A -> D, weight 1
g.add_edge(1, 2, 3)  # B -> C, weight 3
g.add_edge(1, 3, 2)  # B -> D, weight 2
g.add_edge(2, 3, 3)  # C -> D, weight 3
g.add_edge(2, 4, 1)  # c -> E, weight 1
g.add_edge(2, 5, 5)  # C -> F, weight 5
g.add_edge(3, 4, 1)  # D -> E, weight 1
g.add_edge(4, 5, 2)  # E -> F, weight 2

dis,Tree = g.dijkstra_SpanningTree('A',1)

print("Initial Distance Table")
print('\t',"0 2 5 1 0 0",'\n\t',"2 0 3 2 0 0",'\n\t',"5 3 0 3 1 5",'\n\t',"1 2 3 0 1 0",'\n\t',"0 0 1 1 0 2",'\n\t',"0 0 5 0 2 0")
print("Dijkstra Result")
print("Spanning Tree:ADECBF")
print("Destination,Previous node,Distance")
for i in range(len(Tree)):
    print(Tree[i])









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

        return





g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4)  # D -> A, weight 4
g.add_edge(3, 4, 2)  # D -> E, weight 2
g.add_edge(0, 2, 3)  # A -> C, weight 3
g.add_edge(0, 4, 4)  # A -> E, weight 4
g.add_edge(4, 2, 4)  # E -> C, weight 4
g.add_edge(4, 6, 5)  # E -> G, weight 5
g.add_edge(2, 5, 5)  # C -> F, weight 5
g.add_edge(1, 2, 2)  # B -> C, weight 2
g.add_edge(1, 5, 2)  # B -> F, weight 2
g.add_edge(6, 5, 5)  # G -> F, weight 5

distances = g.dijkstra('D')
print(distances)





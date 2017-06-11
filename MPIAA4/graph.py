import random

class Graph(object):
    """Graph class"""
    def __init__(self, vertices=[], edges=[], weight={}):
        self.vertices = set()
        self.adjacent = {}
        self.weight = {}
        for v in vertices:
            self.add_vertex(v)
        for v1, v2 in edges:
            self.add_edge(v1, v2)
        for k, v in weight:
            self.weight[k] = v

    def add_vertex(self, vertex):
        """Add vertex to the graph."""
        self.vertices.add(vertex)
        """Add vertex to the graph."""
        if vertex not in self.adjacent:
            self.adjacent[vertex] = []

    def add_edge(self, v1, v2, weight=1):
        """Add edge to the graph between vertices v1 and v2."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        if v1>v2:
            v1,v2=v2,v1
        if v1 in self.weight:
            if self.has_edge(v1,v2):
                self.weight[v1][v2]+=weight
            else:
                self.weight[v1][v2]=weight
        else:
            self.weight[v1] = {}
            self.weight[v1][v2] = weight
        if v2 not in self.weight:
            self.weight[v2] = {}
            self.weight[v1][v2] = weight
        v1_adj = self.adjacent[v1]
        v2_adj = self.adjacent[v2]
        if v2 not in v1_adj:
            v1_adj.append(v2)


    def get_vertices(self):
        """Get all vertices of the graph."""
        return list(self.vertices)

    def get_adjacent(self, vertex):
        """Get list of adjacent vertices in the graph for the vertex"""
        if vertex in self.adjacent:
            return self.adjacent[vertex]
        return []

    def get_edge_weight(self, v1, v2):
        return self.weight[v1][v2]

    def get_weight(self):
        weight=0
        for i in self.get_vertices():
            for j in self.get_adjacent(i):
                weight+=self.get_edge_weight(i, j)
        return weight

    def has_edge(self, v1, v2):
        """Returns True if there is an edge between vertices v1 and v2, False otherwise."""
        if v1 not in self.vertices or v2 not in self.vertices:
            return False
        return v2 in self.adjacent[v1]

    def input_Graph(self, file):
        graph = Graph()
        with open(file) as graph_file:
            graph_file = graph_file.read()
            for edge in graph_file.split('\n'):
                vert = edge.split('\t')
                graph.add_edge(str(vert[0]), str(vert[1]), random.randint(1, 10))
        return graph

    def krascal_alg(self):
        list = []
        edges = []
        for i in self.get_vertices():
            for j in self.get_adjacent(i):
                edges.append([i, j, self.get_edge_weight(i, j)])
        edges.sort(key=lambda x: x[2])
        edge = {i: i for i in self.get_vertices()}
        for start, end, weight in edges:
            if edge[start] != edge[end]:
                list.append((start, end, weight))
                a = edge[start]
                b = edge[end]
                for i in self.get_vertices():
                    if edge[i] == b:
                        edge[i] = a
        return list



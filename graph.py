"""
adjacency matrix
adjacency list
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def rm_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]
        return True

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'C')

my_graph.remove_edge('A', 'B')
my_graph.rm_vertex('A')
my_graph.print_graph()

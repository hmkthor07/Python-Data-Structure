"""
Graph Implementation using adjacency matrix
 - for undirected graph, with weighte or unweighted edges.

Vertex Class 
 - A vertex object only needs to store its name. 
"""

class Vertex:
    def __init__(self, n):
        self.name = n

"""
Graph Class

A graph object has three attributes:
- vertices - a dictionary with vertex-name:vertex_object
- edges - a 2-dimensional list(ie. a matrix) of edges. for an unweighted graph it will contain 0 for no edge and 1 for edge. 
- edge_indices - a dictionary with vertex_name:list_index(eg. A:0) to access edges. 
add_vertex updates all three of these attributes. 
add_edge only needs to update the edges matrix. 
"""

class Graph:
    vertices = {}
    edges = [] # 2 dimensional edges
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            # for loop appends a column of zeros to the edges matrix
            for row in self.edges:
                row.append(0)

            # append a row of zeros to the bottom of the edges matrix
            self.edges.append([0]*(len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end= ' ')
            print()



# Test code
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HD','HE','HI','IF','IH','JF','JG']
for edge in edges:
    g.add_edge(edge[0], edge[1])
g.print_graph()
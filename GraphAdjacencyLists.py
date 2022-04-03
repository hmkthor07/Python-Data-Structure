"""
Vertex Class
The Vertex class has a constructor that sets the name of the vertex(in our example, just a letter), 
and creates a new empty set to store neighbors

The add_neighbor method adds the name of a neighboring vertex to the neighbors set. 
Thbis set automatically eliminates duplicates.
"""

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = set()

    def add_neighbor(self, v):
        self.neighbors.add(v)
# Doubly Linke List
"""
Every Node has 3 parts:
    data and pointers to previous and next Nodes.
"""

# The following Node class will be used on all three types of linkedlists
class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    
    def __str__(self):
        return ('('+str(self.data)+')')


class DoublyLinkedList:
    def __init__(self, r=None):
        self.root=r
        self.last=r
        self.size=0
    
    def add(self,d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d,self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1
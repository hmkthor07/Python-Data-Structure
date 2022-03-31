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

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            elif this_node.next_node == None:
                return False
            else:
                this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None: 
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else:
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else: # delete last node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node
        return False

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node, end='->')
        print()
                

dll = DoublyLinkedList()
for i in [5,9,3,8,9]:
    dll.add(i)

print("size="+str(dll.size))
dll.print_list()
print(str(dll.root))
dll.remove(8)
dll.print_list()
print(str(dll.root))

print(dll.remove(15))
print(dll.find(15))
dll.add(21)
dll.add(22)
dll.remove(5)
dll.print_list()
print(dll.last.prev_node)
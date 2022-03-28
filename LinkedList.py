"""
Every Node has 2 parts which are data and a pointer to the next Node.

Linked Lists
Attributes: 
    1. root - pointer to the beginning of the List
    2. size - number of nodes in List
Operations:
    1. find(data)
    2. add(data)
    3. remove(data)
    4. print_list()
"""

# The following Node class will be used on all three types of linkedlists
class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    
    def __str__(self):
        return ('('+str(self.data)+')')

class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    def find(self,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None
    def remove(self,d):
        this_node=self.root
        prev_node=None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')



myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()

print("size="+str(myList.size))
myList.remove(8)
print("size="+str(myList.size))
print(myList.find(5))
print(myList.root)

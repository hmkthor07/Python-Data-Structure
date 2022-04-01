"""
Binary Search Tree

Each node is greater than every node in its left subtree.

Each node is less than every node in ints right subtree. 
"""

#Insert
#Start at root 
#Always insert as a leaf

#BST Delete
#3 possible cases: 1. leaf node 2. 1 child 3. 2 children
# in case delete 2 children => Find the next higher node!

"""
Traversal

1. Preorder Traversal
    Visit root before visiting the root's subtrees.
2. Inorder Traversal
    Visit root between visiting the root's subtrees.
    Gives values in sorted order.
"""

"""
Advantages of Binary Search Trees?
1. Insert, Delete, Find in O(h) = O(log n)
"""

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    
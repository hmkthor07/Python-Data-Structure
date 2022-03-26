def line():
    print("---------------------------------------------")

# MaxHeap 
# Complete Binary Tree
# Every node <= its parent

# MaxHeap is fast! 
# Insert in O(logN)
# Get in O(1)
# Remove Max in O(logN)

# Push : 1. Add value to the end of the array 2. Float it up to its proper position
# It's in the right position if it is greater than or equal to its child's nodes

# Peek : Return the value at heap[1]

# Pop : 1. move max to end of array(Swap it with the last position) 2. Delete it 3. Bubble down the item at index 1 to its proper postion
# 4. Return max

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap)-1)
    
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def pop(self):
        if(len(self.heap) > 2):
            self.__swap(1,len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif(len(self.heap)==2): # 기본 [0] 은 들어가있어서, len==2이면, 마지막 하나 남은 것이다. 
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def __floatUp(self, index):
        parent = index//2
        if(index <= 1):
            return
        if(self.heap[parent] < self.heap[index]):
            self.__swap(parent, index)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap)>left and self.heap[largest] < self.heap[left]:
            largest=left
        if len(self.heap)>right and self.heap[largest] < self.heap[right]:
            largest=right

        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
    
    def __str__(self):
        return str(self.heap)


line()
m = MaxHeap([95,3,21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
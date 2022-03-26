# Queues

# Enqueue : add an item to the end of the line. 
# Dequeue : remove an item from the front of the line.

# FIFO : First-In First-Out
# Enqueue on one end, and Dequeue from the other end. 

# Queues Use Cases
# Queues are good for modeling anything you wait in line for
# For instance, Bank tellers / Placing an order at McDonalds

# Deque is a double-ended queue, but we can use it for our queue.

from collections import deque

def line():
    print("---------------------------------------------")

my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())
print(my_queue)

line()
class Queue():
    from collections import deque
    def __init__(self):
        self.queue = deque()
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.popleft()
    def get_size(self):
        return len(self.queue)

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue.queue)
print(my_queue.get_size())
my_queue.dequeue()
print(my_queue.queue)
print(my_queue.get_size())
my_queue.dequeue()
print(my_queue.queue)
print(my_queue.get_size())
print(my_queue.queue)
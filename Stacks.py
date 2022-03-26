def line():
    print("---------------------------------------------")

# Stacks
# Push an item onto the stack
# Pop an item off of the stack

# LIFO : Last in First out
# All push and pop operations are to/form the top of the stack. 

# Peek : get item on top of the stack, without removing it. 
# Clear : clear all items from stack

# Stack use case 
# Undo : track whick commands have been executed. 
# Pop last command off command stack to undo it. 

# Stack using List
my_stack = list()
my_stack.append(1)
my_stack.append(12)
my_stack.append(13)
my_stack.append(144)
print(my_stack)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack)

line()
x = [1,2,3]

class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if(len(self.stack) > 0):
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if(len(self.stack)>0):
            return self.stack[-1]
        else:
            return None
    def __str__(self):
        return(str(self.stack))

line()

my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
print(my_stack.__str__())
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())

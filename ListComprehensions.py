import random

def line():
    print("---------------------------------------------")

# get values within a range
under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10))

# get squared values
squares = [x**2 for x in under_10]
print('squares : ' + str(squares))

# get odd numbers using mod
odds = [x for x in range(10) if x%2==1]
print('odds : ' + str(odds))

line()
# get multiples of 10
ten_x = [x*10 for x in range(10)]
print('ten_x: '+str(ten_x))

# get all numbers from a string
s = 'I love 2 go t0 the store 7 times a w3ek.'
nums = [x for x in s if x.isnumeric()]
print('nums : ' + str(nums))
print('nums : ' + ''.join(nums))

ex = ['k','b','o']
print(''.join(ex))

line()
# get index of a list item 
names = ['apple','banana','peach','mango']
idx = [k for k,v in enumerate(names) if v == 'peach'] # The enumerate returns both key and value.
print('index = '+str(idx[0]))

line()
# delete an item from a list
letters = [x for x in 'ABCDE']
print(letters)
random.shuffle(letters)
print(letters)
letrs = [x for x in letters if x != 'C']
print(letters, letrs)

line()
# nested loop iteration for 2D list
a = [[1,2],[3,4]]
new_list=[x for b in a for x in b]
print(new_list)
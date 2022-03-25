def line():
    print("---------------------------------------------")

# string
x = 'frog'
print(x[3])

# list
x = ['pig','cow','horse']
print(x[1])

# tuple
x = ('Kevin','Niklas','Jenny','Craig')
print(x[0])

#slicing [start : end+1 : step]
x = 'computer'
print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])

line()
# adding and concatenating
# string
x = 'horse' + 'shoe'
print(x)

# list
y = ['pig','cow'] + ['horse']
print(y)

# typle
z = ('Kevin','Niklas','Jenny') + ('Craig',)
print(z)

line()
# Multiplying
# string
x = 'bug' * 3
print(x)

y = [8,5] * 3
print(y)

z = (2,4) * 3
print(z)

line()
# Checking membership
# string
x = 'bug'
print('u' in x)

# list
y = ['a','b','c']
print('b' not in y)

# tuple
z = ('ga','na','da','la')
print('da' in z)

line()
# Iterating
# item
x = [7,8,3]
for item in x:
    print(item)

# index & item
y = [7,8,3]
for index, item in enumerate(y):
    print(index, item)

line()
# number of items
# string
x = 'bug'
print(len(x))

# list
y = ['ping','cow','horse']
print(len(y))

# tuple
z = ('Kevin','Niklas','Jenny','Craig')
print(len(z))

line()
# minimum
# string
x = 'bug'
print(min(x))

# list
y = ['ping','cow','horse']
print(min(y))

# tuple
z = ('Kevin','Niklas','Jenny','Craig')
print(min(z))

line()
# Maximum
x = 'bug'
print(max(x))

# list
y = ['ping','cow','horse']
print(max(y))

# tuple
z = ('Kevin','Niklas','Jenny','Craig')
print(max(z))

line()
# Sum
# list
y = [2,5,8,12]
print(sum(y))
print(sum(y[-2:]))

# tuple
z = (50,4,7,19)
print(sum(z))

line()
# Sorting : The sorted function does not change the original function, rather it just returns the sorted brand new list
x = 'bug'
print(sorted(x))

# list
y = ['ping','cow','horse']
print(sorted(y))

# tuple
z = ('Kevin','Niklas','Jenny','Craig')
print(sorted(z))

line()
# Sorting with lambda function
z = ('Kevin','Niklas','Jenny','Craig')
print(sorted(z, key=lambda k:k[1]))


line()
# Count
# string
x = 'hippo'
print(x.count('p'))

# list
y = ['ping','cow','horse','cow']
print(y.count('cow'))

# tuple
z = ('Kevin','Niklas','Jenny','Craig')
print(z.count('Kevin'))


line()
# Index
# string
x = 'hippo'
print(x.index('p'))

# list
y = ['ping','cow','horse','cow']
print(y.index('cow'))

# tuple
z = ('Kevin','Niklas','Jenny','Craig')
print(z.index('Jenny'))

line()
# Unpacking
y = ['ping','cow','horse']
a,b,c = y
print(a,b,c)

# Lists are sotable
# details of the List
x = list()
y = ['a',25,'dog',8.43]
tuple1 = (10,20)
z = list(tuple1)

line()
# list comprehension
a = [m for m in range(8)]
print(a)

b = [i**2 for i in range(10) if i>4]
print(b)

line()
# delete
x = [1,2,3,4,5]
del(x[1])
print(x)
del(x)
#print(x) # list x no longer exists

line()
# append
x = [1,2,3,4,5]
x.append(8)
print(x)

line()
#extend
x = [1,2,3]
y = [4,5]
x.extend(y)
print(x)

line()
# insert : insert an iten at a given index
x = [1,2,3]
x.insert(1,5)
print(x)
x.insert(1,['a','b'])
print(x)

line()
# pop : pops last item off list and returns item
x=[1,2,3,4]
val = x.pop()
x.append(val)
print(x)

line()
# remove - remove first instance of an item
x = [1,3,5,3,7]
x.remove(3)
print(x)

line()
x = [1,5,3,7]
x.reverse()
print(x)

line()
# sorted just return a new sorted list but sort is an in-place sort function
x = [5,3,7,1]
x.sort()
print(x)

# reverse sort (descending sort)
x = [5,3,8,6]
x.sort(reverse=True)
print(x)

line()
# Tuples 
# 1. Immutable 
# 2. Useful for fixed data
# 3. Faster than Lists
# 4. Sequence type

x = ()
print(x, type(x))
x = (1,2,3,)
print(x, type(x))
x = 1,2,3
print(x, type(x))
x = 1,
print(x, type(x))

x = [1,2,3]
x = tuple(x)
print(x, type(x))

line()
# Tuples are immutable
x = (1,2,3)
# del(x[1]) # fails
# x[1] = 8 # fails
print(x)

# However, a list in a tuple can be mutable
y = ([1,2],3)
del(y[0][1])
print(y)

y += (4,)
print(y)


line()
# Sets : non-duplicate items / Very fast access vs lists / Math Set options / Sets are unordered.

x = {3,5,3,5}
print(x)

y = set()
print(y)

list1 = [3,5,3,5]
print(list1)
z = set(list1)
print(z)

line()
x = {3,8,5}
print(x)
x.add(7)
print(x)
x.remove(5)
print(x)

line()
# get length of set x
print(len(x))
print(8 in x)
print(x.pop(), x) # pop random item from set x
# delete all items from set x
x.clear()
print(x)

line()
# Mathematical set operations
set1 = {1,2,3}
set2 = {3,4,5}

print(set1 & set2) #intersection
print(set1 | set2) # union
print(set1 ^ set2) # symmetric difference
print(set1 - set2)
print(set1 <= set2)
print(set1 >= set2)

line()
# Dictionaries : Key/Value pairs / Associative array like Java HashMap / Dicts are unordered
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
print(x)
x = dict([('pork',25.3),('beef',33.8),('chicken',22.7)])
print(x)
x = dict(pork=22, beef=4, chicken=7)
print(x)

line()
x['shrimp'] = 38.2
print(x)
x['pork'] = 100
print(x)

del(x['shrimp'])
print(x)

print(len(x))

# delete all items from dict x
x.clear()
print(x)

del(x) # free up the memory (entirely deleted)
#print(x)

line()
# Accessing keys and values in a dict
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
print(x.keys())
print(x.values())
print(x.items())

# check membership in x_keys (only looks in keys, not values)
print('beef' in x)
print(22 in x.values())

# iterating a dict
for key in x:
    print(key, x[key])

for k, v in x.items():
    print(k,v)
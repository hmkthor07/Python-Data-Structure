def line():
    print("-----------------------")

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
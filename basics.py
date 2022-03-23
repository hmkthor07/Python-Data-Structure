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
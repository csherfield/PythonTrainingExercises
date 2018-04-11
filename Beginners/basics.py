# Given
x = 10000.0
y = 3.0
print(x / y)
print(10000 / 3)
# What is happening?

# Given
print(x - 1 / y)
print((x - 1) / y)
# What is happening?

# Given 
x = 'foo'
y = 'bar'
# Create 'foobar' using x and y
s = x + y
print(s)
# Create 'foo -> bar' using x and y
print(x + " -> " + y)

# Given
x = 'hello world'
# from x create 'HELLO WORLD'
print(x.upper())
# from x create 'hellX wXrld'
print(x.replace('o', 'X'))

# Given
x = 10000.0
y = 3.0
# print "10000 / 3 = 3333" using x and y
print("{x} / {y} = {z}".format(x=x, y=y, z=x/y))

# Given
s = ['hello', 'world']
# print 'helloworld'
print(s[0] + s[1])
# print 'hello world'
print(s[0] , s[1])
# print 'hello
print(s[0])
# world'
print(s[1])

# Given
x = "Monty Python and the Holy Grail"
# create the list ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']
print(x.split())
y = "one,two,three,four"
# create the list ['one', 'two', 'three', 'four'
print(y.split(','))

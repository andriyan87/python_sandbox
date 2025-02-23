# Strings in python are surrounded by either single or double quotes.
# Let's look at string formatting and some string methods

name = 'Andriyan '
age = 37

# Concatenate
# print('Hello, my name is ' + name + ' and  I am ' + str(age) + ' years old')

# String Formatting

# Arguments by positions
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-String (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# using %
# print('Hello, my name is  %s and I am %s ' % (name, age))

# String Methods
s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'Everyone'))

# Count
sub = 'l'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())



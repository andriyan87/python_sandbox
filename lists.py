# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list 
numbers = [1,2,3,4,5,6]
fruits = ['Apples', 'Bananas', 'Peaches', 'Strawberries']

# Use constructor 
# numbers2 = list((1,2,3,4,5,6))

# Get a singles value of a list 

# print(fruits[1])

# Get a length of a list

# print(len(fruits))

# Append -- add to the end of a list 

fruits.append('Oranges')

# Remove form list

fruits.remove('Strawberries')

# Insert to specific position

fruits.insert(2, 'Strawberries')

# Change value 
fruits[0] = 'Blueberries'

# Remove using pop method for specific position

fruits.pop(2)

# Revers list

# fruits.reverse()

# Sort list
# fruits.sort()

# Revers sort
# fruits.sort(reverse=True)
print(fruits)



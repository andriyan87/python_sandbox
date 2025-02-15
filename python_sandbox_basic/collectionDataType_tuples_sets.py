# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple

fruits = ('Apples', 'Bananas', 'Strawberries', 'Grapes')

# Use constructor
#fruits2= tuple(('Apples', 'Bananas', 'Strawberries', 'Grapes'))

# Single value need trailing coma
fruits2 = ('Apples',)

# Get value 
# print(fruits[1])


#Can't change value 
# fruits[0] = 'Peaches'

# Delete tuple
del fruits2


# Get length 
# print(len(fruits))


# A Set is a collection which is unordered and unindexed and changeable. No duplicate members.


# Create set
fruits_set = {'Apples', 'Bananas', 'Mango'}

# Check if in set
# print('Apples' in fruits_set)

# Add to duplicate
fruits_set.add('Apples')

# Remove from set
# fruits_set.remove('Grape')

# Clear set
# fruits_set.clear()



# Delete set
# del fruits_set

print(fruits_set)







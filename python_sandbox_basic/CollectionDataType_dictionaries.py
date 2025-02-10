# A Dictionary is a collection which is unsordered,changeable and indexed. No duplicate members.
# Mutable types like list and dic cannot be dictionary keys
# Immutable can be keys like str, int, tuple 

# Create dict

person = {'name': 'Andriyan',
          'age' : 37,
          'town': 'Sofia'
}


# print(person, type(person))

# Use constructor
# person2 = dict(name = 'John', age = 23, town = 'Burgas')

# Get a  value 

# print(f"My name is {person['name']} and I am {person['age']}")
# print(f"My name is {person.get('name')} and I am {person.get('age')}")

# Add key/ value 
person['phone'] = '08781234'

# Get dict keys 
# print(person.keys())


# Get dict items
# print(person.items())

# Copy dict

person2 = person.copy()
# person2['country'] = 'Bulgaria'

# Remove item
del(person['age'])
person.pop('phone')

#Clear
# person.clear()

# Get length
# print(person, len(person))

# List of dict
people = [
    {'name': 'Bobby',
          'age' : 39,
          'town': 'Sofia'},
    {'name': 'Hulk',
          'age' : 44,
          'town': 'Plovdiv'},
    {'name': 'Joey',
          'age' : 11,
          'town': 'Varna'}
]

print(people[0]['town'])


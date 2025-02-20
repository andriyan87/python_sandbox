# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
from validator import validate_email

# Create class
class User:
    # Constructor 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        if(validate_email(self.email)):
            return f'My name is {self.name} and I am {self.age} and my email {self.email} is valid my equipment contains: !'
        else:
            return f'My name is {self.name} and I am {self.age} and my email is {self.email} is not valid '

    def has_birthday(self):
        self.age += 1

# Extend class
class Customer(User):
     # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.gymequipment  =  ['Belt with chain', 'push ups tools', 'towels']

    # Add new item to list 
    def set_gymequipment(self):
      self.gymequipment.append('Sneakers')
      return self.gymequipment

    def greeting(self):
        if(validate_email(self.email)):
            return f'My name is {self.name} and I am {self.age} and my email {self.email} is valid so my equipment contains:  {self.gymequipment}!'
        else:
            return f'My name is {self.name} and I am {self.age} and my email is {self.email} is not valid  so my equipment contains:  {self.gymequipment}!'


# Init user object 
andriyan = User('Andriyan Atanasov', 'a#abv.bg', 38)

#Init customer object
john = Customer('John Wick', 'john@abv.bg', 25)

john.set_gymequipment()
print(john.greeting())


# andriyan.has_birthday()
# print(andriyan.greeting())




# A variable is a container for a value, which can be of various types

"""
VARIABLES RULES
-- Variable names are case sensitive (name and NAME are different variables)
-- Must start with a letter or an underscore
-- Can have numbers but can not start with one
"""


# Multiple assignment
x, y, name, is_true = (1, 2.34, 'Andriyan', True)

# Basic math
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)

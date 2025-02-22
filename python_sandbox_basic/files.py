# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myfile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myfile.name)
print('Opening Mode: ', myfile.mode)
print('Is Closed: ', myfile.closed)

# Write to file
myfile.write('I love Python')
myfile.write(' and JavaScript')
myfile.close()


# Append to file
myfile = open('myfile.txt', 'a')
myfile.write(' I also like PHP')
myfile.close()

# Read from file
myfile = open('myfile.txt', 'r+')
text = myfile.read(100)
print(text)
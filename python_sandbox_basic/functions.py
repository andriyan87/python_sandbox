# A function is block of code which is running when its called . In Python it doesnt use curly brackets, use indetation like tabs and spaces 

# Create a function

def sumOf(firstNumber, secondNumber):
    totalSum = firstNumber + secondNumber
    return  totalSum

sum = sumOf(4,5)

# print(sum)
# Return value

# firstName = input()
# lastName = input()

def fullName(firstName, lastName):

    return print(f'{firstName } {lastName}')

# fullName(firstName,lastName)

# lambda function is a small anonymous function

sumOf = lambda firstNumber, secondNumber :  firstNumber + secondNumber

print(sumOf(2,2))




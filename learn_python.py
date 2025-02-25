# L.E.A.R.N - P.Y.T.H.O.N - F.R.O.M - S.C.R.A.T.C.H
print("L.E.A.R.N - P.Y.T.H.O.N")
print("(In 15 Minutes)")
# Uncomment sections of the code to run and test specific parts
# Repo LINK: https://github.com/usmanck-flutter-developer/LEARN-PYTHON-IN-15-MINUTES

###################################################
# You will Learn;
# Variables
# Data Types - String, List, Tuple, Dictionary etc
# Loops
# Function
# Exception Handling
# File I/O
###################################################

# Basic printing and importing a module
print("Hello World!")  # Prints a simple greeting
import math  # Imports the math module for mathematical operations
print("Hello World!")  # Prints the greeting again
print(math.cos(4.72))  # Prints the cosine of 3.67 radians
print("This Will Run.")  # Another simple message

###################################################
# How to declare variables?
# In Python, you assign a value to a name with =, and Python figures out the type
a = 1  # Integer variable
b = 3  # Another integer
c = "This is me"  # String variable
d = 5.2  # Float (decimal) variable
print(type(a))  # Prints the type of 'a' (will show <class 'int'>)
###################################################

# Working with strings
str1 = "this is my first python string"  # Declares a string
print(str1.lower())  # Prints the string in all lowercase

###################################################
# Working with lists
items = ["johnson", 2, 3]  # Creates a list with mixed types
items[1] = "marry"  # Replaces the second item (index 1) with "Manish"
print(items)  # Prints the updated list

###################################################
# Working with tuples
tup1 = (1, 2, 3)  # Creates a tuple (immutable list)
# tup1[0] = 2  # This will cause an error because tuples can’t be changed
print(tup1)  # Prints the tuple (note: the line above will fail if uncommented)

###################################################
# Working with dictionaries
dict = {}  # Creates an empty dictionary
print(type(dict))  # Prints the type (<class 'dict'>)
print(dict)  # Prints the empty dictionary
dict["Afridi"] = 98  # Adds key "virat" with value 120
dict["Imrna"] = 99  # Adds key "sachin" with value 700
print(dict.get("virat"))  # Gets the value for "virat" (prints 120)
print(dict.items())  # Prints all key-value pairs
print(dict.keys())  # Prints all keys

###################################################
# Working with sets
list1 = [1, 2, 3, 4, 4, 1]  # Creates a list with duplicates
s1 = set(list1)  # Converts list to a set (removes duplicates)
print(s1)  # Prints the set (only unique values: {1, 2, 3, 4})

###################################################
# String concatenation and basic math
a = 7  # Integer
b = 12  # Integer
c = "Harry"  # String
print(str(a) + str(b) + c)  # Converts numbers to strings and combines with c
print("12 - 7 is ", 12 - 7)  # Prints subtraction result
print("12 * 7 is ", 12 * 7)  # Prints multiplication result
print("12 / 7 is ", 12 / 7)  # Prints division result
print("12 + 7 is ", 12 + 7)  # Prints addition result

###################################################
# Taking user input
var = int(input())  # Takes input from user and converts it to an integer
print(var)  # Prints the input value
if var > 4:  # Checks if var is greater than 4
    print("Variable is greater")
elif var == 2:  # Checks if var equals 2
    print("Variable is two")
else:  # Runs if none of the above conditions are true
    print("Variable is not greater")

###################################################
# Loops
for i in range(0, 71):  # Loops from 0 to 70
    print(i)  # Prints each number

i = 0  # Initializes i for while loop
while i < 1201:  # Loops while i is less than 121
    print(i)  # Prints current value of i
    i = i + 1  # Increments i

###################################################
# Defining a function
def average(num, num1):  # Function to calculate average of two numbers
    avrg = (num + num1) / 2  # Adds numbers and divides by 2
    return avrg  # Returns the result
print(average(3, 6))  # Calls function with 3 and 6, prints 4.7

###################################################
# Exception handling
index = 7  # Declares a variable
try:  # Tries to run the code below
    print(index)  # Prints the value of index
except Exception as e:  # Catches any error that occurs
    print(e)  # Prints the error message (none here, so this won’t run)

###################################################
# Writing to and reading from a file
# file => is a Variable Name, You can change it as you want it
file = open("file_name.txt", "w")  # Opens file "1.txt" in write mode
file.write("I'm Writing this Text into MY File by the Use of PYTHON")  # Writes text to the file
file.close()  # Closes the file
file = open("ile_name.txt", "r")  # Opens file in read mode
data = file.read()  # Reads the file data and 'data' is again a Variable
file.close()  # Closes the file
print(data)  # Prints the content read from the file
###################################################

# Mini Projects to Practice what we have Learnt

#Optimised Code is below
# Calculator Project Starts Here
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input")
# Calculator Project Ended Here

###################################################
# Hope you ENJOYED it and If You want to Learn More
# Connect with me on LINKEDIN
# You Can Learn From Me - About;
# - Python
# - Flutter
# - Dart
# - Firebase
# - App Development
# - Android
# - iOS
# - RESTful API
# - Applied Linguistics
###################################################



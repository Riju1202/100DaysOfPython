# Day1 of Python, print and input statements

# print() is used to print the output on the screen
print("Hello World!")
# Types of quotation marks
# Single quotes
print('Hello "World!" ')# We can use single quotes inside double quotes
# Double quotes
print("Hello 'World!' ")# We can use double quotes inside single quotes
# Triple quotes
print(""" 'Hello' "World!" """)# We can use single and double quotes inside triple quotes
print('''Hello World!''')

# Escape sequence
print("Hello \"World!\" ")# We can use escape sequence to print the double quotes

# input() is used to take input from the user
input("What is your Name?\n")

# print and input is used to print and take input from the user respectively
print("Hello " + input("What is your Name?\n") + "!")

# print the length of the string
print(len(input("What is your Name?\n")))

# variables
name = input("What is your Name?\n")
print(len(name))

#Band Name Generator
print("Welcome to the Band Name Generator")
print("What is the name of the city you grew up in?")
city = input()
print("What is the name of your pet?")
pet = input()
print("Your Band Name could be " + city + " " + pet)

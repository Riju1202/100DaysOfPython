#Data Types
#String, Integer, Float, Boolean
#Subscripting
print("Hello"[4])
#Integer
a=123
# '_' is used to make the number more readable for example 1_23_456 = 1,23,456
b=4_5_6#456
print(type(a))
print(a+b)
#Float
c=3.14159
print(c)
#Boolean
print(type(True))
#Type Conversion
a=123
print("a is " + str(a))
#adding digits of a two digit number
two_digit_number = input()
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit+second_digit)
#Mathematical Operations
#PEMDAS
#Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
print(3+5)
print(7-4)
print(3*2)
print(6/3)
print(2**3)
#BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight)/float(height)**2
#converting the bmi to integer rounds off to the lower integer
print(int(bmi))
#rounding off the bmi rounds of to the nearest integer
print(round(bmi))
#rounding off the bmi to 2 decimal places
print(round(bmi,2))
#floor division
print(8//3)
#f-string
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
#Tip Calculator
print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people will split the bill?\n"))
total_bill = bill + (bill*(tip/100))
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)#rounding off to 2 decimal places but if the 
#second decimal is 0 then it will not be displayed so we can use format() function
#final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
def format_name(f_name, l_name):
  f_name = f_name.title()
  l_name = l_name.title()
  return f"{f_name} {l_name}"
print(format_name("angela", "YU"))

#Days in Month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) and month == 2:
    return month_days[month-1]+1 #29
  else:
    return month_days[month-1]
    
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

#Calculator
import os

def add(n1, n2):
  """"This function adds two numbers"""#This is a docstring
  return n1 + n2
def subtract(n1, n2):
  """This function subtracts two numbers"""
  return n1 - n2
def multiply(n1, n2):
  """This function multiplies two numbers"""
  return n1 * n2
def divide(n1, n2):
  """This function divides two numbers"""
  return n1 / n2
operations = ['+', '-', '*', '/']

# How to do the operations part with a Dictionary
# operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
# operations['+'](3, 4) # 7
# or operation = operations['+']
# operation(3, 4) # 7
# or operations.get('+')(3, 4) # 7

cont = 'n'
while cont != 'e':
  if cont == 'n' or cont == 'y':
    if cont == 'n':
      num1=float(input("What's the first number?: "))
    op = input("Please select the operation you want to perform: +, -, *, / \n")
    if op not in operations:
      print("Invalid operation. Please try again.")
      cont = 'y'
      continue
    num2=float(input("What's the second number?: "))
    result = 0
    if op == operations[0]:
      result = add(num1, num2)
    elif op == operations[1]:
      result = subtract(num1, num2)
    elif op == operations[2]:
      result = multiply(num1, num2)
    elif op == operations[3]:
      result = divide(num1, num2)
      
    print(f"The Result of: {num1} {op} {num2} is {result}")

  cont = input("Do you want to continue with the result if yes Type (Y) or if you want a fresh start Type (N) or Type (E) to exit the Program \n").lower()
  if cont == 'y':
    num1 = result
  elif cont == 'n':
    os.system('cls')
  elif cont == 'e':
    exit()
  else:
    print("Invalid input. Please try again.")
# Input a Python list of student heights

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(f"total height = {sum(student_heights)}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(sum(student_heights)/len(student_heights))}")

# While using for loop

# count = 0
# sum = 0
# for name in student_heights:
#   count += 1
#   sum += name
# print(f"total height = {sum}")
# print(f"number of students = {count}")
# print(f"average height = {round(sum/count)}")
# *************************************************************************

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# While using for loop
  
high_score=0
for score in student_scores:
  if score >high_score:
    high_score=score
print(f"The highest score in the class is: {high_score}")

# Using max() function

# print(f"The highest score in the class is: {max(student_scores)}")
# *************************************************************************

# Sum of even numbers between 0 to X (X included)
target = int(input()) # Enter a number between 0 and 1000

list = range(0,target+1,2)# range(start, stop, step)
print(sum(list))

# or While using for loop

# sum = 0
# for number in range(0,target+1,2):
#   sum += number
# print(sum)
# *************************************************************************

# FizzBuzz game

for num in range(1,101):
  if num%3 == 0 and num%5 != 0:
    print('Fizz')
  elif num%3 != 0 and num%5 == 0:
    print('Buzz')
  elif num%3 == 0 and num%5 == 0:
    print('FizzBuzz')
  else:
    print(num)

# Random password generator
    
import random
import string
print("Welcome to the PyPassword Generator!")
pass_len=int(input("How many characters would you like in your password?\n"))
pass_num=int(input("How many numbers would you like in your password?\n"))
pass_special=int(input("How many special characters would you like in your password?\n"))
alphabet = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
characters = [alphabet , numbers , symbols]
password = ""
for x in range(pass_len):
	char=random.choice(random.choice(characters))
	if char in numbers and pass_num>0:
		password += char
		pass_num -= 1
		if pass_num == 0:
			characters.remove(numbers)
	elif char in symbols and pass_special>0:
		password += char
		pass_special -= 1
		if pass_special == 0:
			characters.remove(symbols)
	else:
		password += char
print(f"Your Generated Password is: {password}")

# or using random.shuffle() and join() functions

import random
import string
print("Welcome to the PyPassword Generator!")
pass_len=int(input("How many characters would you like in your password?\n"))
pass_num=int(input("How many numbers would you like in your password?\n"))
pass_special=int(input("How many special characters would you like in your password?\n"))
pass_alpha=pass_len-pass_num-pass_special
alphabet = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
pass_list = []
for x in range(pass_alpha):
	pass_list.append(random.choice(alphabet))
for x in range(pass_num):
	pass_list.append(random.choice(numbers))
for x in range(pass_special):
  pass_list.append(random.choice(symbols))
random.shuffle(pass_list)# shuffles the list
password="".join(pass_list)# joins the list elements
print(f"Your Generated Password is: {password}")
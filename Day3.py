#If-else conditional statements

#BMI Example
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 60
weight = int(input())
# Calculate your BMI
BMI = weight/height**2
if BMI<18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI<25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI<30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI<35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"BMI is {BMI}, you are clinically obese.")

#Leap year example
# Which year do you want to check?
year = int(input())
if year%4 == 0:
  if year%100 != 0:
    print("Leap year")
  else:
    if year%400 == 0:
      print("Leap Year")
    else:
      print("Not leap year")
else:
  print("Not leap year")
      
#Pizza order example
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill=0
if size == 'S':
  bill=15
  if add_pepperoni == 'Y':
    bill += 2
  if extra_cheese == 'Y':
    bill += 1
elif size == 'M':
  bill=20
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
elif size == 'L':
  bill=25
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
print(f"Your final bill is: ${bill}.")
    
# Love Calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
name=name1+name2
name=name.lower()# convert the string to lowercase
count=0
total=0
for char in "love":
  count += name.count(char)# count the number of times the character appears in the string
total = count
count=0
for char in "true":
  count += name.count(char)
total += 10*count
if total<10 or total>90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total>40 and total<50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")

#Treasure Island
print(''' 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')
print("Welcome to the Treasure Island!!!!!!!!")
print("Your mission is to find the treasure.")
print("While wandering the Island you arrive at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input().lower()
if direction == 'left':
  print("You arrive at a river. There is a fortress across the river. Type 'wait' to wait for a boat or type 'swim' to swim across.")
  direction = input().lower()
  if direction == 'wait':
    print("You arrive at the fortress unharmed. There is a room with 3 doors. One red, one yellow and one blue. Which color do you choose?")
    direction = input().lower()
    if direction == 'red':
      print("It's a room full of fire. Game Over.")
    elif direction == 'yellow':
      print("You found the treasure! You Win!")
    else:
      print("You enter a room of beasts. Game Over.")
  else:
    print("You got eaten by a crocodile. Game Over.")
else:
  print("You were attacked by a Lion. Game Over.")
if direction == 'right' or direction == 'swim' or direction == 'red' or direction == 'blue':
  print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
  

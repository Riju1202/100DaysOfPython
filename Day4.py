#Random Module and List Data Type
# Head or Tails Exercise

import random
coin = random.randint(0,1)
if coin == 0:
  print("Tails")
else:
  print("Heads")

# Collection Data Types
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Treasure Map
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

position=position.lower()
longitude=ord(position[0])-97# ord() returns the ASCII value of the character
# or we can use 
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter) // index() returns the index of the element in the list
latitude=int(position[1])-1
map[latitude][longitude] = 'X' 

print(f"{line1}\n{line2}\n{line3}")

# Rock Paper Scissors

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
game = [Rock, Paper, Scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game_choice=random.randint(0,2)
if user==game_choice:
  print("It's a draw.")
elif (user==0 and game_choice==1) or (user==2 and game_choice==0) or (user==1 and game_choice==2): 
  print("You lose.")
elif (user==0 and game_choice==2) or (user==1 and game_choice==0) or (user==2 and game_choice==1):
    print("You win.")
else:
   print("Invalid input.")
print(f"Computer chose:\n{game[game_choice]}\n\n")
print(f"You chose:\n{game[user]}")

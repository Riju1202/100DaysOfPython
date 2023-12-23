#Functions with Parameters
# Positional Arguments and Keyword Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with("Alvin", "London")# Positional Arguments
greet_with(location="London", name="Alvin")# Keyword Arguments

# Paint Area Calculator

import math
def paint_calc(height,width,cover):
  print(f"You'll need {int(math.ceil((height*width)/cover))} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#Prime number checker

def prime_checker(number):
  flag=0
  for i in range(1,number):
    if number%i == 0:
      flag+=1
  if flag == 1:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input()) # Check this number
prime_checker(number=n)

# Caesar Cipher
import string
alphabet = string.ascii_lowercase
alphabet=list(alphabet)
print("\t\tWelcome to Caesar Cipher")

def Caesar(sentence, push, cipher):
  push = push%26
  new_sentence = ""
  sentence = list(sentence)
  if cipher == 'decode':
    push = -push
  for i in range(len(sentence)):
    if sentence[i] in alphabet:
      if alphabet.index(sentence[i])+push > 25:
        sentence[i] = alphabet[alphabet.index(sentence[i])+push-26]
      elif alphabet.index(sentence[i])+push < 0:
        sentence[i] = alphabet[alphabet.index(sentence[i])+push+26]
      else:
        sentence[i] = alphabet[alphabet.index(sentence[i])+push]
  print(new_sentence.join(sentence))

# def encode(sentence, push):
#   new_sentence = ""
#   sentence = list(sentence)
#   for i in range(len(sentence)):
#     if sentence[i] in alphabet:
#       if alphabet.index(sentence[i])+push > 25:
#         sentence[i] = alphabet[alphabet.index(sentence[i])+push-26]
#       else:
#         sentence[i] = alphabet[alphabet.index(sentence[i])+push]
#   print(new_sentence.join(sentence))

# def decode(sentence, push):
#   new_sentence = ""
#   sentence = list(sentence)
#   for i in range(len(sentence)):
#     if sentence[i] in alphabet:
#       if alphabet.index(sentence[i])-push < 0:
#         sentence[i] = alphabet[alphabet.index(sentence[i])-push+26]
#       else:
#         sentence[i] = alphabet[alphabet.index(sentence[i])-push]
#   print(new_sentence.join(sentence))

while True:
  text = input("Type your message:\n").lower()
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  shift = int(input("Type the shift number:\n"))
  Caesar(sentence=text, push=shift, cipher=direction)
  run_again = input("Do you want to run again? Yes or No\n").lower()
  if run_again == "no":
    print("Goodbye")
    break
    
# BlackJack Game

import os
import random

card = {"A": 11, "K": 10, "Q": 10, "J": 10, "2": 2, "3": 3, "4": 4, "5": 5,
         "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

def display_cards(who_cards):
  if who_cards == player_cards:
    print("Your cards are: ", end=' ')
    for i in range(len(who_cards)):
      print(who_cards[i][0], end=' ')
    print("\n")
  else:
    print("Dealer cards are: ", end=' ')
    for i in range(len(who_cards)):
      print(who_cards[i][0], end=' ')
    print("\n")

def list_convert(combo):
  for i in range(len(combo)):
    combo[i] = list(combo[i])

def check_ace(who_cards):
  for i in range(len(who_cards)):
    if who_cards[i][0] == 'A' and who_cards[i][1] == 11:
      return True
  
def change_ace(who_cards):
  list_convert(dealer_cards)
  list_convert(player_cards)
  for i in range(len(who_cards)):
    if who_cards[i][0] == 'A' and who_cards[i][1] == 11:
      who_cards[i][1] -= 10
      break

def sum_player_cards():
  player_score = 0
  for i in range(len(player_cards)):
    player_score += player_cards[i][1]
  return player_score

def sum_dealer_cards():
  dealer_score = 0
  for i in range(len(dealer_cards)):
    dealer_score += dealer_cards[i][1]
  return dealer_score

def check_player_score():
  if sum_player_cards() > 21 and check_ace(player_cards) and (sum_player_cards()-10) <= 21:
    change_ace(player_cards)
    return sum_player_cards()
  if sum_player_cards() > 21:
    display_cards(player_cards)
    display_cards(dealer_cards)
    print("You went over. You lose!")
    play_game()
  elif sum_player_cards() == 21:
    display_cards(player_cards)
    display_cards(dealer_cards)
    print("You win!")
    play_game()
  else:
    return sum_player_cards()
  
def check_dealer_score():
  if sum_dealer_cards() > 21:
    display_cards(player_cards)
    display_cards(dealer_cards)
    print("Dealer went over. You win!")
    play_game()
  elif sum_dealer_cards() == 21:
    display_cards(player_cards)
    display_cards(dealer_cards)
    print("Dealer got a BlackJack! You lose!")
    play_game()
  else:
    return sum_dealer_cards()
  
def draw_dealer_card():
  if sum_dealer_cards() > 21 and check_ace(dealer_cards) and (sum_dealer_cards()-10) <= 21:
    change_ace(dealer_cards)
  if check_dealer_score() < 17:
    dealer_cards.append(random.choice(list(card.items())))
    draw_dealer_card()
  
def draw_card():
  another_card = input("Do you want to draw another card? Type 'Y' for Yes or 'N'for No\n").lower()
  print()
  if another_card == 'y':
    player_cards.append(random.choice(list(card.items())))
    if check_player_score() < 21:
      display_cards(player_cards)
      draw_card()
  else:
    if sum_dealer_cards() < 17:
      draw_dealer_card()
    if sum_player_cards() > sum_dealer_cards():
      display_cards(player_cards)
      display_cards(dealer_cards)
      print("You win!")
      play_game()
    elif sum_player_cards() == sum_dealer_cards():
      display_cards(player_cards)
      display_cards(dealer_cards)
      print("It's a draw!")
      play_game()
    else:
      display_cards(player_cards)
      display_cards(dealer_cards)
      print("You lose!")
      play_game()

def game_start():
  display_cards(player_cards)
  print(f"Dealer's first card: {dealer_cards[0][0]}\n")
  if sum_dealer_cards() == 21:
    display_cards(dealer_cards)
    print("Dealer got a BlackJack! You lose!")
  elif sum_player_cards() == 21:
    print("You got a BlackJack! You win!")
  else:
    draw_card()

def play_game():    
  game = input("\nDo you want to play a game of BlackJack? Type 'Yes' or 'No'\n").lower()
  os.system('cls')
  if game == 'yes':
    global player_cards
    global dealer_cards
    player_cards = random.choices(list(card.items()), k=2)
    dealer_cards = random.choices(list(card.items()), k=2)
    if sum_player_cards() == 22:
      change_ace(player_cards)
    if sum_dealer_cards() == 22:
      change_ace(dealer_cards)
    game_start()
  else:
    print("Goodbye!")
    exit()
  play_game()

print("\t\t\tWelcome to BlackJack!\n")
print("The game is simple. You have to get as close to 21 as possible without going over. \n")
print("The dealer draws cards until it reaches a score of 17 or more. \n")
play_game()
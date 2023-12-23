# Dictionaries and Nesting
# Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
  if student_scores[key]>90:
    student_grades[key] = 'Outstanding'
  elif student_scores[key]>80:
    student_grades[key] = 'Exceeds Expectations'
  elif student_scores[key]>70:
    student_grades[key] = 'Acceptable'
  else:
    student_grades[key] = 'Fail'

print(student_grades)

# Nesting Lists and Dictionaries
# Nesting Dictionary in a List
capitals = [
  {"France": "Paris", # Nesting Dictionary in a List
   "cities_visited": ["Paris", "Lille", "Dijon"], # Nesting List in a Dictionary
   "total_visits": 12},
  {"Germany": "Berlin"},
]

# Dictionary in a List
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
  travel_log.append({"country": country, "visits": visits, "cities": list_of_cities}) 

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# Silent Auction

import os
 

print("\t\tWelcome to the Bidding Wars!")
print("The person who bids the highest will win the auction.")

bid_list = {}
while True:
  name = input("Please enter your Name below.\n")
  price = int(input("Please enter your bid below.\n$"))
  bid_list[name] = price
  cont = input("Do you want to continue? (y/n)\n").lower()
  os.system('cls')# Clearing the Screen
  if cont == 'n':
    break
max_key = max(bid_list, key=bid_list.get) #Getting the key with the highest value with
# the .get() method. The .get() method returns the value of the key.
print(f"\t\tThe winner is {max_key} with a bid of ${bid_list[max_key]}")
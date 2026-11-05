# Escape Characaters
print("Dear Class, \nI am so sad that this is out LAST day in ")

# Absolute v.s. Relative Paths
# data/data.txt relative to where your current working directory
#Absolute paths start from "Home"/users/szilli/...

#Modules and Libraries
import random

randim_int = random.randint(1,10)
print(random_int)

deck_of_cards = ["Kings of Spades", "8 of hears", "2 of Diamonds"]
random_card = random.choice(deck_of_cards)
print(random_card)



import math
answer = math.sqrt(64)
print(answer)


#File I/0
#Reading, Writing, Append
with open("demo.txt", "w") as file:
    file.write("File I/0 is soooo fun\n")

#challengeg 1: logger.py
#Write a program that asks the user for thier name
#and the ADDS it to a guest_list.txt file
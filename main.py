###############################################################################
# Title: Data Structures: RPG - Modules

# Class: Computer Science 30 P1 S2                                                                                                                   
# Date: March 13, 2023

# Coder's Name: Yifei Zhao                                                                                                            
# Version: 003                                                                                        
###############################################################################
"""
This program creates a map. 
The user should not be able to walk off the map.
When the user is in a room, there will be a message printed to the console. 
The user will be able to choose which direction to go. 
Has empty lists that the user will be able to add items into it. 
"""
###############################################################################
# Global Variables & Imports
row = 2
col = 2

import sys
import message
from map import *
from player import *
from action import *
from randomResult import *

User = Player(2, 2)
Inventory = Objects()

# map for the HauntedMansion 
HauntedMansion = [
  ["Grand Ball Room", "Master Bedroom", "Bathroom", "Master Bedroom"],
  ["Closet", "Master Bedroom", "Rooftop", "Closet"],
  ["Grand Ball Room", "Bathroom", "Entrance", "Bathroom"],
  ["Master Bedroom", "Closet", "Rooftop", "Bathroom"],
  ["Rooftop", "Master Bedroom", "Grand Ball Room", "Exit"]
]

# Create room objects
Rooftop = Rooms("You are currently at the Rooftop of this mansion. This is the highest place of this mansion. Be careful NOT to fall down... ", "randomized")
Entrance = Tile("You are currently at the Entrance. ", "randomized", "Welcome To The Haunted House! Your goal is to collect as many items as possible. ")
GrandBallRoom = Rooms("You are currently in the Grand Ball Room. This is the largest room in this house, maybe you want to explore it. BE CAREFUL!! ", "randomized")
Closet = Rooms("You are currently in the Closet. This is the smallest room in this house. All of the clothes in the closet... What can I find here? ", "randomized")
MasterBedroom = Rooms("You are currently in the Master Bedroom. This is where the previous couples stayed before they were never seen ever again... ", "randomized")
Bathroom = Rooms("You are currently in the Bathroom. The room of slaughter. Be careful NOT to be the next one... ", "randomized")
Exit = Tile("You are currently at the exit. ", "randomized", "You have successfully found the exit. Goodbye! ")

actionChoice = ["walk", "search", "quit", "inventory"]

# Create action objects
Walk = Action("Currently Walking Around! ", "You will be able to walk around the room. ")
Search = Action("Searching For Possible Keys! ", "You will be able to search the room. ")
Quit = Action("Thank you for playing. Bye! ", "The game will stop. ")
Inv = Action("These are your current inventories. ", "If you do not see anything in it, that is because you have not found or collected anything yet. ")


def mainChoice():
  """
    function for mainChoice
    this function will asks for the user's action 
  """
  # prints the options for action
  while True:
    print("Possible actions: ")
    # printing the possible options for the user
    for key in actionChoice:
      print(f"- {key}")
    actionChoice2 = (input(message.actionMessage))
    print('\n')
    # if the user chose walk as their action, do the following
    if actionChoice2 == "walk":
      Walk.mainChoiceMessages()
      break
    # if the user chose search as their action, do the following
    elif actionChoice2 == "search":
      Search.mainChoiceMessages()
      Inventory.randomResult()
      print('\n')
      break
    # if the user chose quit as their action, do the following
    elif actionChoice2 == "quit":
      Quit.mainChoiceMessages()
      sys.exit()
    # if the user chose inventory as their action, do the following
    elif actionChoice2 == "inventory":
      Inv.mainChoiceMessages()
      print("Inventories: ")
      for item in Inventory.inventory:
        print(f"- {item}")
        print('\n')
      print('\n')
      print("Medicines: ")
      for meds in Inventory.medicine:
        print(f"- {meds}")
        print('\n')
      print('\n')
      print("Foods: ")
      for food in Inventory.food:
        print(f"- {food}")
        print('\n')
      print('\n')
      break
    # if the user chose none of the above, do the following
    else:
      print("No capital letters!")
      print('\n')


# Main
Playing = True
while Playing: 
  current_location = HauntedMansion[User.row][User.col]
  # if the user is at the Entrance, do the following
  if current_location == "Entrance":
    print(Entrance.passage)
    print(Entrance.description)
    print('\n')
  # if the user is at the grand ball room, do the following
  elif current_location == "Grand Ball Room":
    print(GrandBallRoom.description)
    print('\n')
  # if the user is at the closet, do the following
  elif current_location == "Closet":
    print(Closet.description)
    print('\n')
  # if the user is at the master bedroom, do the following
  elif current_location == "Master Bedroom":
    print(MasterBedroom.description)
    print('\n')
  # if the user is at the rooftop, do the following
  elif current_location == "Rooftop":
    print(Rooftop.description)
    print('\n')
  # if the user is at the bathroom, do the following
  elif current_location == "Bathroom":
    print(Bathroom.description)
    print('\n')
  # if the user is at the exit, do the following
  elif current_location == "Exit":
    print(Exit.passage)
    sys.exit()
  # if the user is not at any of the locations above, do the following
  else:
    print(message.wrongMessage)
    print('\n')
  # Main Menu
  mainChoice()
  User.movements()
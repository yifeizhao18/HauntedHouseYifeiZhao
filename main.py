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
from randomResult import *
from action import *

Inventory = Objects()


# map for the HauntedMansion 
HauntedMansion = [
  ["Grand Ball Room", "Master Bedroom", "Bathroom", "Master Bedroom"],
  ["Closet", "Master Bedroom", "Rooftop", "Closet"],
  ["Grand Ball Room", "Bathroom", "Entrance", "Bathroom"],
  ["Master Bedroom", "Closet", "Rooftop", "Bathroom"],
  ["Rooftop", "Master Bedroom", "Grand Ball Room", "Exit"]
]

def movements():
  """
  movement function that asks for the user input on directions.
  makes sure the user does not walk off of the map.
  """
  global row, col
  # reading the maptile text file and printing it on the console
  with open("maptile.txt", "r") as file:
    sentence = file.read()
    print(sentence)
    print('\n')
  # printing the maptile to the external file called the tile.txt
  with open ("tile.txt","w") as file2:
    file2.write(f"This is the map: \n{sentence} ")
  while True:
    movementChoice = (input(message.askDirection))
    print('\n')
    # if the user put in North, do the following 
    try:
      if movementChoice == "north":
        # makes sure the user stays in the map
        if row == 0:
          print("You have ran into a wall. ")
          print('\n')
          print("Please type in another direction. ")
          print('\n')
        else:
          row -= 1
          break
      # if the user put in South, do the following
      elif movementChoice == "south":
        # makes sure the user stays in the map
        if row == 4:
          print("You have ran into a wall. ")
          print('\n')
          print("Please type in another direction. ")
          print('\n')
        else:
          row += 1
          break
      # if the user put in West, do the following
      elif movementChoice == "west":
        # makes sure the user stays in the map
        if col == 0:
          print("You have ran into a wall. ")
          print('\n')
          print("Please type in another direction. ")
          print('\n')
        else:
          col -= 1
          break
      # if the user put in East, do the following
      elif movementChoice == "east": 
        # makes sure the user stays in the map
        if col == 3:
          print("You have ran into a wall. ")
          print('\n')
          print("Please type in another direction. ")
          print('\n')
        else: 
          col += 1
          break
      # if the user chose none of the above, do the following
      else:
        print(message.wrongMessage)
        print('\n')
    # do this if there is an exception in the code
    except:
      print("Movement Exception")
      print('\n')
    # else break out of the while loop
    else:
      break
    # do this no matter what
    finally:
      print(massage.answer)
      print('\n')
      

# objects created for the ActionChoice class
Walk = ActionChoice("Currently Walking Around! ", "You will be able to walk around the room. ")
Search = ActionChoice("Searching For Possible Keys! ", "You will be able to search the room. ")
Quit = ActionChoice("Thank you for playing. Bye! ", "The game will stop. ")
Inventory = ActionChoice("These are your current inventories. ", "If you do not see anything in it, that is because you have not found or collected anything yet. ")

# list created for actionChoice
actionChoice = ["walk", "search", "quit", "inventory"]

def mainChoice(Inventory, Food, Medicine):
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
      print(Walk.description)
      print('\n')
      print(Walk.message)
      print('\n')
      break
    # if the user chose search as their action, do the following
    elif actionChoice2 == "search":
      print(Search.description)
      print('\n')
      print(Search.message)
      print('\n')
      randomResult()
      print('\n')
      break
    # if the user chose quit as their action, do the following
    elif actionChoice2 == "quit":
      print(Quit.description)
      print('\n')
      print(Quit.message)
      sys.exit()
    # if the user chose inventory as their action, do the following
    elif actionChoice2 == "inventory":
      print(Inventory.description)
      print('\n')
      print(Inventory.message)
      print('\n')
      print("Inventories: ")
      for item in object.inventory:
        print(f"- {item}")
        print('\n')
      print('\n')
      print("Medicines: ")
      for meds in object.medicine:
        print(f"- {meds}")
        print('\n')
      print('\n')
      print("Foods: ")
      for food in object.food:
        print(f"- {food}")
        print('\n')
      print('\n')
      break
    # if the user chose none of the above, do the following
    else:
      print("No capital letters!")
      print('\n')


# Main
# print the welcome message
Entrance = Tile("You are currently at the Entrance. ", "randomized", "Welcome To The Haunted House! Your goal is to collec as many items as possible. ")
print(Entrance.passage)
while True: 
  current_location = HauntedMansion[row][col]
  # if the user is at the Entrance, do the following
  if current_location == "Entrance":
    print(Entrance.description)
    print('\n')
  # if the user is at the grand ball room, do the following
  elif current_location == "Grand Ball Room":
    GrandBallRoom = Rooms("You are currently in the Grand Ball Room. This is the largest room in this house, maybe you want to explore it. BE CAREFUL!! ", "randomized")
    print(GrandBallRoom.description)
    print('\n')
  # if the user is at the closet, do the following
  elif current_location == "Closet":
    Closet = Rooms("You are currently in the Closet. This is the smallest room in this house. All of the clothes in the closet... What can I find here? ", "randomized")
    print(Closet.description)
    print('\n')
  # if the user is at the master bedroom, do the following
  elif current_location == "Master Bedroom":
    MasterBedroom = Rooms("You are currently in the Master Bedroom. This is where the previous couples stayed before they were never seen ever again... ", "randomized")
    print(MasterBedroom.description)
    print('\n')
  # if the user is at the rooftop, do the following
  elif current_location == "Rooftop":
    Rooftop = Rooms("You are currently at the Rooftop of this mansion. This is the highest place of this mansion. Be careful NOT to fall down... ", "randomized")
    print(Rooftop.description)
    print('\n')
  # if the user is at the bathroom, do the following
  elif current_location == "Bathroom":
    Bathroom = Rooms("You are currently in the Bathroom. The room of slaughter. Be careful NOT to be the next one... ", "randomized")
    print(Bathroom.description)
    print('\n')
  # if the user is at the exit, do the following
  elif current_location == "Exit":
    Exit = Tile("You are currently at the exit. ", "randomized", "You have successfully found the exit. Goodbye! ")
    print(Exit.passage)
    sys.exit()
  # if the user is not at any of the locations above, do the following
  else:
    print(message.wrongMessage)
    print('\n')
  # Main Menu
  Inventory.randomResult()
  #action.mainChoice(Inventory, randomResult.Food, randomResult.Medicine)
  movements()
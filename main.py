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
import sys
import map
import message
import randomResult
import action


# Main
while True: 
  current_location = map.HauntedMansion[map.row][map.col]
  # if the user is at the Entrance, do the following
  if current_location == "Entrance":
    print(map.Entrance.description)
    print('\n')
  # if the user is at the grand ball room, do the following
  elif current_location == "Grand Ball Room":
    print(map.roomsHauntedMansion["Grand Ball Room"]["description"])
    print('\n')
  # if the user is at the closet, do the following
  elif current_location == "Closet":
    print(map.roomsHauntedMansion["Closet"]["description"])
    print('\n')
  # if the user is at the master bedroom, do the following
  elif current_location == "Master Bedroom":
    print(map.roomsHauntedMansion["Master Bedroom"]["description"])
    print('\n')
  # if the user is at the rooftop, do the following
  elif current_location == "Rooftop":
    print(map.roomsHauntedMansion["Rooftop"]["description"])
    print('\n')
  # if the user is at the bathroom, do the following
  elif current_location == "Bathroom":
    print(map.roomsHauntedMansion["Bathroom"]["description"])
    print('\n')
  # if the user is at the exit, do the following
  elif current_location == "Exit":
    print(map.roomsHauntedMansion["Exit"]["description"])
    sys.exit()
  # if the user is not at any of the locations above, do the following
  else:
    print(message.wrongMessage)
    print('\n')
  # Main Menu
  action.mainChoice(randomResult.Inventory, randomResult.Food, randomResult.Medicine)
  map.movements()
import sys
from randomResult import *
actionChoice = ["walk", "search", "quit", "inventory"]

class ActionChoice:
  "a class for all of the actions"
  def __init__ (action, message, description):
    ActionChoice.action = action
    ActionChoice.message = message
    ActionChoice.description = description

    
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
      actionChoice2 = (input("message.actionMessage"))
      print('\n')
      # if the user chose walk as their action, do the following
      if actionChoice2 == "walk":
        Walk = ActionChoice("Currently Walking Around! ", "You will be able to walk around the room. ")
        print(Walk.description)
        print('\n')
        print(Walk.message)
        print('\n')
        break
      # if the user chose search as their action, do the following
      elif actionChoice2 == "search":
        Search = ActionChoice("Searching For Possible Keys! ", "You will be able to search the room. ")
        print(Search.description)
        print('\n')
        print(Search.message)
        print('\n')
        randomResult()
        print('\n')
        break
      # if the user chose quit as their action, do the following
      elif actionChoice2 == "quit":
        Quit = ActionChoice("Thank you for playing. Bye! ", "The game will stop. ")
        print(Quit.description)
        print('\n')
        print(Quit.message)
        sys.exit()
      # if the user chose inventory as their action, do the following
      elif actionChoice2 == "inventory":
        Inventory = ActionChoice("These are your current inventories. ", "If you do not see anything in it, that is because you have not found or collected anything yet. ")
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
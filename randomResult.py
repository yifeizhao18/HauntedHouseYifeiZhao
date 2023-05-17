# Global Variables and Imports
import random
import message

result1 = "Sorry! There is nothing here. "
result2 = "You found some energy drink. "
result3 = "You found a treasure chest with bandages. "
result4 = "You found some food. "
result5 = "You found a treasure chest with a flashlight in it. "
result6 = "You found a treasure chest with a knife in it. "
result7 = "You found a treasure chest with a sword in it. "
  


class Objects:
  "created a class for the inventory, food, medicine"
  def __init__ (object):
    object.inventory = []
    object.food = []
    object.medicine = []


  def randomResult(object):
    """
    This function is for randomizing results. 
    It will randomly give the user a result after they selected to 'search' the room
    """
    result = random.randint(0,9)
    # if it randomzied a 0, give the following result
    if result == 0:
      print(result1)
      print('\n')
    # if it randomized a 1, give the following result
    elif result == 1:
      print(result6)
      print('\n')
      print(message.congratsMessage)
      print('\n')
      while True:
        # asks the user if they want to collect the item
        collect = input(message.collectMessage)
        print('\n')
        # if the user says yes, do the following, and then break
        if collect == "yes":
          object.inventory.append("knife")
          print(object.inventory)
          print('\n')
          break
        # else if the user saya no, do the following, and then break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        # else do the following, and repeat
        else:
          print(message.wrongSpelling)
          print('\n')
    # if it randomized a 2, do the following
    elif result == 2: 
      print(result7)
      print('\n')
      print(message.congratsMessage)
      print('\n')
      while True:
        # asks the user if they want to collect it or not
        collect = input(message.collectMessage)
        print('\n')
        # if the user says yes, do the following, and then break
        if collect == "yes":
          object.inventory.append("sword")
          print(object.inventory)
          print('\n')
          break
        # else if the user says no, do the following, and then break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        # else do the following, and repeat  
        else:
          print(message.wrongSpelling)
          print('\n')
    # if it randomized a 3, do the following
    elif result == 3: 
      print(result4)
      print('\n')
      print(message.congratsMessag)
      print('\n')
      while True:
        # asks the user if they want to collect it or not
        collect = input(message.collectMessage)
        print('\n')
        # if the user says yes, do the following, and then break
        if collect == "yes":
          object.food.append("apples")
          print(object.food)
          print('\n')
          break
        # else if the user says no, do the following, and then break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        # else do the following, and repeat
        else:
          print(message.wrongSpelling)
          print('\n')
    # if it randomized a 4, do the following
    elif result == 4:
      print(result5)
      print('\n')
      print(message.congratsMessage)
      print('\n')
      while True: 
        # asks the user if they want to collect it or not
        collect = input(message.collectMessage)
        print('\n')
        # if the user says yes, do the following, and then break
        if collect == "yes":
          object.inventory.append("flashlight")
          print(object.inventory)
          print('\n')
          break
        # else if the user says no, do the following, and then break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        # else do the following, and repeat
        else:
          print(message.wrongSpelling)
          print('\n')
    # if it randomized a 5, do the following
    elif result == 5:
      print(result2)
      print('\n')
      print(message.congratsMessage)
      print('\n')
      while True:
        # asks the user if they want to collect it or not
        collect = input(message.collectMessage)
        print('\n')
        # if the user says yes, do the following, and then break
        if collect == "yes":
          object.food.append("energy drink")
          print(object.food)
          print('\n')
          break
        # else if the user says no, do the following, and then break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        # else do the following, and repeat
        else:
          print(message.wrongSpelling)
          print('\n')
    # if it randomized a 6, do the following
    elif result == 6:
      print(result3)
      print('\n')
      print(message.congratsMessage)
      print('\n')
      while True: 
        # asks the user if they want to collect it or not
        collect = input(message.collectMessage)
        print('\n')
        # if the user says yes, do the following, and then break
        if collect == "yes":
          object.medicine.append("bandages")
          print(object.medicine)
          print('\n')
          break
        # else if the user says no, do the following, and then break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        # else do the following, and repeat
        else:
          print(message.wrongSpelling)
          print('\n')
    # if it randomized a 7, do the following
    elif result == 7:
      print(result1)
      print('\n')
    # if it ranfomized a 8, do the following
    elif result == 8:
      print(result5)
      print('\n')
      print(message.congratsMessage)
      print('\n')
      while True: 
        # asks the user if they want to collect it or not
        collect = input(message.collectMessage)
        print('\n')
        # if the user says yes, do the following, and then break
        if collect == "yes":
          object.inventory.append("flashlight")
          print(object.inventory)
          print('\n')
          break
        # else if the user says no, do the following, and then break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        # else do the following, and repeat
        else:
          print(message.wrongSpelling)
          print('\n')
    # if it randomized a 9, do the following
    elif result == 9:
      print(result5)
      print('\n')
      print(message.congratsMessage)
      print('\n')
      while True:
        # asks the user if they want to collect it or not
        collect = input(message.collectMessage)
        print('\n')
        # if the user says yes, do the following, and then break
        if collect == "yes":
          object.inventory.append("flashlight")
          print(object.inventory)
          print('\n')
          break
        # else if the user says no, do the following, and then break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        # else do the following, and repeat
        else:
          print(message.wrongSpelling)
          print('\n')
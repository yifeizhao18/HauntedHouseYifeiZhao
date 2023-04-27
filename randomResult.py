# Global Variables and Imports
import random
import message

# empty list for inventory, foods, medicines, and weapons
Inventory = []
Food = []
Medicine = []

# possible results when the user chose to search
possibleResults = {
  "result1" : "Sorry! There is nothing here. ",
  "result2" : "You found some energy drink. ",
  "result3" : "You found a treasure chest with bandages. ",
  "result4" : "You found some food. ",
  "result5" : "You found a treasure chest with a flashlight in it. ",
  "result6" : "You found a treasure chest with a knife in it. ",
  "result7" : "You found a treasure chest with a sword in it. "
  }

def randomResult():
  """
  This function is for randomizing results. 
  It will randomly give the user a result after they selected to 'search' the room
  """
  result = random.randint(0,9)
  # if it randomzied a 0, give the following result
  if result == 0:
    print(possibleResults["result1"])
    print('\n')
  # if it randomized a 1, give the following result
  elif result == 1:
    print(possibleResults["result6"])
    print('\n')
    print(message.congratsMessage)
    print('\n')
    while True:
      # asks the user if they want to collect the item
      collect = input(message.collectMessage)
      print('\n')
      # if the user says yes, do the following, and then break
      if collect == "yes":
        Inventory.append("knife")
        print(Inventory)
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
    print(possibleResults["result7"])
    print('\n')
    print(message.congratsMessage)
    print('\n')
    while True:
      # asks the user if they want to collect it or not
      collect = input(message.collectMessage)
      print('\n')
      # if the user says yes, do the following, and then break
      if collect == "yes":
        Inventory.append("sword")
        print(Inventory)
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
    print(possibleResults["result4"])
    print('\n')
    print(message.congratsMessage)
    print('\n')
    while True:
      # asks the user if they want to collect it or not
      collect = input(message.collectMessage)
      print('\n')
      # if the user says yes, do the following, and then break
      if collect == "yes":
        Food.append("apples")
        print(Food)
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
    print(possibleResults["result5"])
    print('\n')
    print(message.congratsMessage)
    print('\n')
    while True: 
      # asks the user if they want to collect it or not
      collect = input(message.collectMessage)
      print('\n')
      # if the user says yes, do the following, and then break
      if collect == "yes":
        Inventory.append("flashlight")
        print(Inventory)
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
    print(possibleResults["result2"])
    print('\n')
    print(message.congratsMessage)
    print('\n')
    while True:
      # asks the user if they want to collect it or not
      collect = input(message.collectMessage)
      print('\n')
      # if the user says yes, do the following, and then break
      if collect == "yes":
        Food.append("energy drink")
        print(Food)
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
    print(possibleResults["result3"])
    print('\n')
    print(message.congratsMessage)
    print('\n')
    while True: 
      # asks the user if they want to collect it or not
      collect = input(message.collectMessage)
      print('\n')
      # if the user says yes, do the following, and then break
      if collect == "yes":
        Medicine.append("bandages")
        print(Medicine)
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
    print(possibleResults["result1"])
    print('\n')
  # if it ranfomized a 8, do the following
  elif result == 8:
    print(possibleResults["result5"])
    print('\n')
    print(message.congratsMessage)
    print('\n')
    while True: 
      # asks the user if they want to collect it or not
      collect = input(message.collectMessage)
      print('\n')
      # if the user says yes, do the following, and then break
      if collect == "yes":
        Inventory.append("flashlight")
        print(Inventory)
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
    print(possibleResults["result5"])
    print('\n')
    print(message.congratsMessage)
    print('\n')
    while True:
      # asks the user if they want to collect it or not
      collect = input(message.collectMessage)
      print('\n')
      # if the user says yes, do the following, and then break
      if collect == "yes":
        Inventory.append("flashlight")
        print(Inventory)
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
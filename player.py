import message

class Player:
  def __init__ (self, row, col):
    self.row = row
    self.col = col

  
  def movements(self):
    """
    movement function that asks for the user input on directions.
    makes sure the user does not walk off of the map.
    """
    # reading the maptile text file and printing it on the console
    try:
      with open("maptile.txt", "r") as file:
        sentence = file.read()
        print(sentence)
        print('\n')
      # printing the maptile to the external file called the tile.txt
      with open ("tile.txt","w") as file2:
        file2.write(f"This is the map: \n{sentence} ")
    except:
        print("File Exception")
    else:
      pass
    while True:
      movementChoice = (input(message.askDirection))
      print('\n')
      # if the user put in North, do the following 
      try:
        if movementChoice == "north":
          # makes sure the user stays in the map
          if self.row == 0:
            print("You have ran into a wall. ")
            print('\n')
            print("Please type in another direction. ")
            print('\n')
          else:
            self.row -= 1
            break
        # if the user put in South, do the following
        elif movementChoice == "south":
          # makes sure the user stays in the map
          if self.row == 4:
            print("You have ran into a wall. ")
            print('\n')
            print("Please type in another direction. ")
            print('\n')
          else:
            self.row += 1
            break
        # if the user put in West, do the following
        elif movementChoice == "west":
          # makes sure the user stays in the map
          if self.col == 0:
            print("You have ran into a wall. ")
            print('\n')
            print("Please type in another direction. ")
            print('\n')
          else:
            self.col -= 1
            break
        # if the user put in East, do the following
        elif movementChoice == "east": 
          # makes sure the user stays in the map
          if self.col == 3:
            print("You have ran into a wall. ")
            print('\n')
            print("Please type in another direction. ")
            print('\n')
          else: 
            self.col += 1
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
        print(message.answer)
        print('\n')
  
  
  
import sys

class Action:
  "a class for all of the actions"
  def __init__ (action, message, description):
    action.message = message
    action.description = description 
    
  def mainChoiceMessages(action):
    """   """
    print(action.description)
    print('\n')
    print(action.message)
    print('\n')

    
    
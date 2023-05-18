class Action:
  """
  a class for all of the actions
  """
  def __init__ (action, message, description):
    action.message = message
    action.description = description 
    
  def mainChoiceMessages(action):
    """ 
    prints the descriptions and the messages for each action
    """
    # prints the description message
    print(action.description)
    print('\n')
    # prints the message
    print(action.message)
    print('\n')

    
    
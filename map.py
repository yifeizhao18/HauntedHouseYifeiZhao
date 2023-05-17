import message
# Global Variables and Imports

class Rooms:
  "created a class for the Rooms for the tiles in the map"
  def __init__(room, description, num_treasure):
    room.description = description
    room.num_treasure = num_treasure


class Tile(Rooms):
  "created a child class for the class Rooms"
  def __init__ (room, description, num_treasure, passage):
    super(Tile, room).__init__(description, num_treasure)
    #room.__init__(room, description, num_treasure)
    room.passage = passage

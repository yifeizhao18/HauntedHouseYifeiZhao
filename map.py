# Global Variables and Imports

class Rooms:
  "created a class for the Rooms for the tiles in the map"
  def __init__(room, description, num_treasure):
    Rooms.room = room
    Rooms.description = description
    Rooms.num_treasure = num_treasure


class Tile(Rooms):
  "created a child class for the class Rooms"
  def __init__ (room, description, num_treasure, passage):
    Rooms.__init__(room, description, num_treasure)
    Rooms.passage = passage





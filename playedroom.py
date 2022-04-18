class PlayedRoom:
  def __init__(self, data, enter_from, item, fate):
    self.data = data
    self.item = item
    self.fate = fate
    self.enter_from = enter_from
    self.exits = ["north", "east", "west", "south",][:self.data.num_exits]

  def description(self):
    return self.data.enter_text

  def name(self):
    return self.data.name

  

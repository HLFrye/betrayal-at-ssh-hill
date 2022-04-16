
class Player:
    pos = (0, 0)

    def move(self, drn):
        match drn:
            case "north":
                self.pos = (self.pos[0], self.pos[1] + 1)
            case "south":
                self.pos = (self.pos[0], self.pos[1] - 1)
            case "east":
                self.pos = (self.pos[0] + 1, self.pos[1])
            case "west":
                self.pos = (self.pos[0] - 1, self.pos[1])


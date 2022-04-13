from dataclasses import dataclass

@dataclass
class Room:
    name: str
    enter_text: str
    num_exits: int

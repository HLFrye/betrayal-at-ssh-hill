from dataclasses import dataclass
import frontmatter
import glob

@dataclass
class RoomData:
    name: str
    enter_text: str
    num_exits: int

def load_room(f):
    inp = frontmatter.load(f)
    return RoomData(name=inp["name"], enter_text=inp.content, num_exits=inp["num_exits"])

def load_all_rooms():
    files = glob.glob("rooms/*.md")
    return [load_room(f) for f in files]

from dataclasses import dataclass
import frontmatter
import glob
from path import Path

@dataclass
class RoomData:
    name: str
    enter_text: str
    num_exits: int

def load_room(f):
    inp = frontmatter.load(f)
    filename = Path(f).stem
    return RoomData(name=inp.get("name", filename), enter_text=inp.content, num_exits=inp.get("num_exits", 0))

def load_all_rooms():
    files = glob.glob("rooms/*.md")
    return [load_room(f) for f in files]

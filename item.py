from dataclasses import dataclass
import frontmatter
import glob
from pathlib import Path

@dataclass
class ItemData:
  name: str
  description: str
  
def load_item(f):
    inp = frontmatter.load(f)
    filename = Path(f).stem
    return ItemData(name=inp.get("name", filename), description=inp.content)

def load_all_items():
    files = glob.glob("items/*.md")
    return [load_item(f) for f in files]


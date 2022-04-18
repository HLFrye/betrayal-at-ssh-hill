from dataclasses import dataclass
import frontmatter
import glob
from pathlib import Path

@dataclass
class FateData:
  name: str
  description: str
  
def load_fate(f):
    inp = frontmatter.load(f)
    filename = Path(f).stem
    return FateData(name=inp.get("name", filename), description=inp.content)

def load_all_fates():
    files = glob.glob("fates/*.md")
    return [load_fate(f) for f in files]


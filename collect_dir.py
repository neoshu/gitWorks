"""
    Collect all the folders of new_dir which in the same directory.
    Return a list.          
"""
from pathlib import Path

def collect(path):
    criteria = list(path.iterdir())
    if len(criteria) == 0:
        return path
    else:
        collected_dirs = []
        # criteria = list(path.iterdir())
        for each_dir in criteria:
            collected_dirs.append(collect(each_dir))
        return collected_dirs

path = Path("new_dir")
print(collect(path))
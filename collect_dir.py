"""
    Collect all the folders of new_dir which in the same directory.
    Return a list.          
"""
from pathlib import Path

target_path = Path('new_dir')
def main_collect(path=target_path):
    folders = [] # the returned result in list form
    def process_collect(dir):
        if dir.is_dir() and len(list(dir.iterdir())) == 0:
            folders.append(dir)
        elif dir.is_file():
            pass
        elif analyze_path_item(dir):
            folders.append(dir)
        else:
            for item in dir.iterdir():
                process_collect(item)
    process_collect(path)
    return folders

def analyze_path_item(path):
    for every in path.iterdir():
        if every.is_dir():
            return False
    return True

print(main_collect())
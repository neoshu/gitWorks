"""
    Collect all the folders of new_dir which in the same directory.
    Return a list.          
"""
from pathlib import Path

def are_all_file(path):
    judge_list = list(path.iterdir())
    for item in judge_list:
        if not item.is_file():
            return False
    return True

def collect(path):
    criteria = list(path.iterdir())
    if len(criteria) == 0:
        return path
    elif are_all_file(path):
        return path
    else:
        collected_dirs = []
        for each_dir in criteria:
            if each_dir.is_dir():
                collected_dirs.append(collect(each_dir))
        return collected_dirs

path = Path("new_dir")
result = collect(path)
corrected_result = []
for item in result:
    if type(item) != list:
        corrected_result.append(item)
    else:
        corrected_result.extend(item)
print(corrected_result)
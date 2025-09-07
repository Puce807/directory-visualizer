from pathlib import Path
from config import *

def get_stem(lst):
    # Args: List
    new_lst = []
    for item in lst:
        l_path = Path(item)
        if include_ext:
            new_lst.append(l_path.name)
        else:
            new_lst.append(l_path.stem)
    return new_lst

#print(get_stem([r"C:\Users\lrgc1\PycharmProject\directory-visualizer\test\text1.txt"]))
from pathlib import Path

from scan import *
from utils import *
from config import *

#target_dir = ""
target_dir = r"C:\Users\lrgc1\PycharmProject\directory-visualizer\test"
success = True
while not success:
    print("Please enter your target directory:")
    target_dir = Path(input(">  "))

    if target_dir.exists():
        success = True
    else:
        print(f"ERROR: '{target_dir}' does not exist!")

file_list = scan_files(target_dir)
stem_list = get_stem(file_list)
print(stem_list)

# Rendering Code:
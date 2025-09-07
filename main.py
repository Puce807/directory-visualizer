from pathlib import Path

from render import *
from scan import *
from utils import *
from config import *

target_dir = ""
success = False
while not success:
    print("Please enter your target directory:")
    target_dir = Path(input(">  "))

    if target_dir.exists():
        success = True
    else:
        print(f"ERROR: '{target_dir}' does not exist!")

file_list = scan_files(target_dir)
file_stem_list = get_stem(file_list)
dir_list = scan_dirs(target_dir)

print(f"{Path(target_dir).stem}\\")
print_contents(file_stem_list, dir_list, 0)
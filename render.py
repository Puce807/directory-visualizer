from config import *
from scan import *
from utils import *
from pathlib import Path

def print_contents(file_stem, dir_list, layer=0, last_flags=None):
    """
    Recursively prints files and directories with proper tree lines.
    :param file_stem: list of file names
    :param dir_list: list of directory paths
    :param layer: current depth
    :param last_flags: list of booleans tracking last-directory status for each layer
    """
    if last_flags is None:
        last_flags = []

    # Build prefix based on parent layers
    base_str = ""
    for is_last in last_flags[:-1]:  # skip the current layer for now
        base_str += "    " if is_last else "│   "

    # Print files
    for i, file in enumerate(file_stem):
        is_last_file = i == len(file_stem) - 1 and not dir_list
        connector = "└── " if is_last_file else "├── "
        print(f"{base_str}{connector}{file}")

    # Print directories recursively
    for i, d in enumerate(dir_list):
        is_last_dir = i == len(dir_list) - 1
        connector = "└── " if is_last_dir else "├── "
        print(f"{base_str}{connector}{Path(d).stem}")

        if expand_sub_dir:
            sub_files = scan_files(d)
            sub_file_stems = get_stem(sub_files)
            sub_dirs = scan_dirs(d)
            sub_dir_stems = get_stem(sub_dirs)
            # Pass updated last_flags
            print_contents(sub_file_stems, sub_dirs, layer + 1, last_flags + [is_last_dir])

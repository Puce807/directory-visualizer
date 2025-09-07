from pathlib import Path

def scan_files(path):
    folder_path = Path(path)
    files = [str(f) for f in folder_path.iterdir() if f.is_file()]

    return files

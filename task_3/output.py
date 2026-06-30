from pathlib import Path
from colorama import Fore

def print_directory(path: str | Path, space_level=0):
    path = Path(path)

    for item in path.iterdir():

        if item.is_dir():
            print(Fore.RED + "    " * space_level + item.name + "/")
            print_directory(item, space_level + 1)
        else:
            print(Fore.GREEN + "    " * space_level + item.name)
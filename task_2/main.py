from data import load_data, process_data
from pathlib import Path

def get_cats_info(path: str | Path) -> list[dict]:
    raw_data = load_data(path)
    cats_info = process_data(raw_data)
    return cats_info

if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent
    file_path = BASE_DIR / "cats_file.txt"
    cats_info = get_cats_info(file_path)
    print(cats_info)
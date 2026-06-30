def load_data(path: str) -> list[str]:

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()

    except FileNotFoundError:
        return []

def process_data(cats_data: list[str]) -> list[dict]:
    info = []
    for line in cats_data:
        if line.strip():
            cat_id, name, age = line.strip().split(",")
            info.append({
                "id": cat_id, 
                "name": name, 
                "age": age
                })

    return info
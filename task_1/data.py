def load_data(path: str) -> list[str]:

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()

    except FileNotFoundError:
        return []

def clean_data(salary_data: list[str]) -> list[float]:
    return [float(salary.strip().split(",")[-1]) for salary in salary_data if salary.strip()]


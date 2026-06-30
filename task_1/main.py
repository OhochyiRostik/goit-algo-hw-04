from data import load_data, clean_data
from processing import calculate_statistics
from pathlib import Path

def total_salary(path: str | Path) -> tuple[float]:
    raw_data = load_data(path)
    salary_list = clean_data(raw_data)
    stats = calculate_statistics(salary_list)
    return stats

if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent
    file_path = BASE_DIR / "salary_file.txt"
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
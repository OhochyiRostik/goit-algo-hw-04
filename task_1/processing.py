def calculate_statistics(salary_list: list[float]) -> tuple[float]:
    if not salary_list:
        return (0, 0)

    total = sum(salary_list)
    average = total/len(salary_list)

    return (total, average)

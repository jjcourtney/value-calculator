OPERATIONS = ("Sum", "Average", "Minimum", "Maximum", "Product")


def calculate_result(calculation: str, values: list[float]) -> float:
    match calculation:
        case "Average":
            return sum(values) / len(values)
        case "Minimum":
            return min(values)
        case "Maximum":
            return max(values)
        case "Product":
            product = 1.0
            for value in values:
                product *= value
            return product
        case _:
            return sum(values)


def format_number(value: float) -> str:
    if value.is_integer():
        return str(int(value))

    return f"{value:.6g}"

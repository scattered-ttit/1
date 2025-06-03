def calculate_expression(a, b):
    denominator = a - 3 * b
    if denominator == 0:
        return "Ошибка: деление на ноль"
    return (a + 4 * b) / denominator + a ** 2
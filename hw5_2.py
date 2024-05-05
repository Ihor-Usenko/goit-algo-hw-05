import re
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    for i in numbers:
        yield i


def sum_profit(text, fun_gen):
    res = 0
    for i in generator_numbers(text):
        res += float(i)
    return res


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

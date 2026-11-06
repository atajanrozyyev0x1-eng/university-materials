# Author = Розыев Атаджан
# Group = P3130
# Date = 21.10.2026

"""ЛР №3, задание 3.
ИСУ 559239: 559239 % 3 = 0.

Проверить правильность формата cron-выражения.
"""

import re


MINUTE = r"(?:[0-5]?\d)"
HOUR = r"(?:[01]?\d|2[0-3])"
DAY = r"(?:0?[1-9]|[12]\d|3[01])"
MONTH = r"(?:0?[1-9]|1[0-2])"
WEEKDAY = r"(?:[0-6])"


def make_field(value):
    item = rf"(?:\*|{value}(?:-{value})?)(?:/[1-9]\d*)?"
    field = rf"{item}(?:,{item})*"

    return field


cron_pattern = re.compile(
    rf"{make_field(MINUTE)}\s+"
    rf"{make_field(HOUR)}\s+"
    rf"{make_field(DAY)}\s+"
    rf"{make_field(MONTH)}\s+"
    rf"{make_field(WEEKDAY)}"
)


def is_valid_cron(expression):
    match = cron_pattern.fullmatch(expression.strip())

    return match is not None


TESTS = [
    ("30 14 * * *", True),
    ("*/5 * * * *", True),
    ("0 0 1 1 *", True),
    ("0,15,30,45 9-18 * * 1-5", True),
    ("60 14 * * *", False),
    ("0 24 * * *", False)
]


def run_tests():
    passed = 0

    for number, test in enumerate(TESTS, start=1):
        test_expression = test[0]
        expected = test[1]

        actual = is_valid_cron(test_expression)

        print(f"\nТест №{number}")
        print("Cron-выражение:", test_expression)
        print("Ожидается:", expected)
        print("Получено:", actual)

        if actual == expected:
            print("Тест пройден")
            passed += 1
        else:
            print("Тест не пройден")

    print(f"\nПройдено тестов: {passed}/{len(TESTS)}")


mode = input(
    "Выберите режим:\n"
    "1 — запустить тесты\n"
    "0 — ввести cron-выражение\n"
    "Ваш выбор: "
)

if mode == "1":
    run_tests()

elif mode == "0":
    user_expression = input("Введите cron-выражение: ")

    if is_valid_cron(user_expression):
        print("Cron-выражение корректно.")
    else:
        print("Cron-выражение некорректно.")

else:
    print("Ошибка: необходимо ввести 1 или 0.")
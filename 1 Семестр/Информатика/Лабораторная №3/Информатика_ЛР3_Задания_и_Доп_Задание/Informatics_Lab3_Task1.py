# Author = Розыев Атаджан
# Group = P3130
# Date = 21.10.2026

"""ЛР №3, задание 1.
ИСУ 559239: 559239 % 7 = 2.

Найти фрагменты:
слово ВТ, от 0 до 4 слов, слово ИТМО.
"""

import re


pattern = r"\bВТ\b(?:\W+\w+){0,4}\W+ИТМО\b"


def find_fragments(text):
    fragments = re.findall(pattern, text)
    result = []

    for raw_fragment in fragments:
        words = re.findall(r"\w+", raw_fragment)
        cleaned_fragment = " ".join(words)
        result.append(cleaned_fragment)

    return result


TESTS = [
    ("А ты знал, что ВТ – лучшая кафедра в ИТМО?", ["ВТ лучшая кафедра в ИТМО"]),
    ("ВТ ИТМО", ["ВТ ИТМО"]),
    ("ВТ один два три четыре ИТМО", ["ВТ один два три четыре ИТМО"]),
    ("ВТ один два три четыре пять ИТМО", []),
    ("ВТ ИТМО2026", []),
    ("ВТ ИТМО, а потом ВТ учится в ИТМО", ["ВТ ИТМО", "ВТ учится в ИТМО"])
]


def run_tests():
    passed = 0

    for number, test in enumerate(TESTS, start=1):
        test_text = test[0]
        expected = test[1]

        actual = find_fragments(test_text)

        print(f"\nТест №{number}")
        print("Введённый текст:", test_text)
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
    "0 — ввести свой текст\n"
    "Ваш выбор: "
)

if mode == "1":
    run_tests()

elif mode == "0":
    user_text = input("Введите текст: ")
    result = find_fragments(user_text)

    if result:
        print("Найденные фрагменты:")

        for found_fragment in result:
            print(found_fragment)
    else:
        print("Подходящих фрагментов нет.")

else:
    print("Ошибка: необходимо ввести 1 или 0.")
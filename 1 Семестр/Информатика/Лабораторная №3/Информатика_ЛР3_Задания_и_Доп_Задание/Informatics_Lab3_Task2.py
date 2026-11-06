# Author = Розыев Атаджан
# Group = P3130
# Date = 21.10.2026

"""ЛР №3, задание 2.
ИСУ 559239: 559239 % 5 = 4.

Найти слова, в которых буквы К, Р, А идут
в указанном порядке через один символ.
"""

import re


pattern = re.compile(r"\S*К\SР\SА\S*", re.IGNORECASE)


def find_words(text):
    words = pattern.findall(text)
    return words


TESTS = [
    ("КоРмА КоРкА КоРчмА", ["КоРмА", "КоРкА"]),
    ("корма КОРКА", ["корма", "КОРКА"]),
    ("Обычное слово подКоРмА находится здесь", ["подКоРмА"]),
    ("КРА КоРчмА", []),
    ("К1Р2А К_Р_А", ["К1Р2А", "К_Р_А"]),
    ("Ко РмА", [])
]


def run_tests():
    passed = 0

    for number, test in enumerate(TESTS, start=1):
        test_text = test[0]
        expected = test[1]

        actual = find_words(test_text)

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


mode = input("Выберите режим:\n1 — запустить тесты\n0 — ввести свой текст\nВаш выбор: ")

if mode == "1":
    run_tests()

elif mode == "0":
    user_text = input("Введите текст: ")
    result = find_words(user_text)

    if result:
        print("Найденные слова:")

        for found_word in result:
            print(found_word)
    else:
        print("Подходящих слов нет.")

else:
    print("Ошибка: необходимо ввести 1 или 0.")
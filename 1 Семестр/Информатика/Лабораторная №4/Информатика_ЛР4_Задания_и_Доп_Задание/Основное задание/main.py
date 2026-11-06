"""Лабораторная №4, вариант 87. Обязательная часть: INI -> объект Python."""
from ini_parser import parse_ini


def main():
    with open("schedule.ini", "r", encoding="utf-8-sig") as source:
        text = source.read()

    schedule = parse_ini(text)
    print("INI успешно разобран. Результат десериализации:")
    print(schedule)

    print("\nСписок занятий:")
    for section_name, fields in schedule.items():
        if section_name.startswith("tuesday_lesson_") or section_name.startswith("thursday_lesson_"):
            print(
                f"{fields['day']}, {fields['time']}: "
                f"{fields['subject']} — {fields['room']}"
            )


if __name__ == "__main__":
    main()
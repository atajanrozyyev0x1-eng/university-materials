"""ЛР №4, вариант 87, дополнительное задание №2 (+10%).

Сравнивает ручную реализацию и библиотеки на одних и тех же данных.
Файлы по умолчанию ищутся рядом с main.py, а не в папке терминала.
"""

from pathlib import Path
import sys
import yaml

from ini_parser import parse_ini
from yaml_serializer import serialize_yaml
from library_converter import parse_ini_library, serialize_yaml_library


def main():
    folder = Path(__file__).resolve().parent
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else folder / "schedule.ini"

    # Один входной файл для честного сравнения.
    with open(input_path, "r", encoding="utf-8-sig") as file:
        ini_text = file.read()

    # Способ №1: наши функции без готовых парсеров.
    manual_data = parse_ini(ini_text)
    manual_yaml = serialize_yaml(manual_data)

    # Способ №2: готовые библиотеки.
    library_data = parse_ini_library(ini_text)
    library_yaml = serialize_yaml_library(library_data)

    # Сравниваем не только текст, но и содержание YAML.
    same_dicts = manual_data == library_data
    same_yaml_data = yaml.safe_load(manual_yaml) == yaml.safe_load(library_yaml)
    preserved_data = yaml.safe_load(library_yaml) == library_data
    same_text = manual_yaml == library_yaml

    manual_output = folder / "schedule_manual.yaml"
    library_output = folder / "schedule_library.yaml"
    with open(manual_output, "w", encoding="utf-8", newline="\n") as file:
        file.write(manual_yaml)
    with open(library_output, "w", encoding="utf-8", newline="\n") as file:
        file.write(library_yaml)

    print("ЛР №4, вариант 87 — дополнительное задание №2")
    print("Секций расписания:", len(manual_data))
    print("Совпадают словари Python:", same_dicts)
    print("Совпадают данные двух YAML:", same_yaml_data)
    print("Данные сохраняются после YAML:", preserved_data)
    print("Побуквенно одинаковые YAML-файлы:", same_text)
    print("Ручной YAML:", manual_output)
    print("Библиотечный YAML:", library_output)

    if not (same_dicts and same_yaml_data and preserved_data):
        raise AssertionError("Результаты преобразований не совпадают по данным")


if __name__ == "__main__":
    main()
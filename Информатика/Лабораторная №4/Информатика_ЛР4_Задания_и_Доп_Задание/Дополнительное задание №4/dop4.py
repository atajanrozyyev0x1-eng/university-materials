"""ЛР4, вариант 87. Дополнительное №4: замеры 100 запусков.

Запусти этот файл в папке с schedule.ini, ini_parser.py,
yaml_serializer.py, xml_serializer.py и library_converter.py.
"""

from pathlib import Path
from time import perf_counter

from ini_parser import parse_ini
from yaml_serializer import serialize_yaml
from xml_serializer import serialize_xml
from library_converter import parse_ini_library, serialize_yaml_library


REPEATS = 100


def only_ini(text):
    """Обязательное задание: INI -> словарь Python."""
    return parse_ini(text)


def ini_to_yaml_manual(text):
    """Доп. №1: свой INI -> словарь -> свой YAML."""
    data = parse_ini(text)
    return serialize_yaml(data)


def ini_to_yaml_library(text):
    """Доп. №2: INI -> YAML с помощью библиотек."""
    data = parse_ini_library(text)
    return serialize_yaml_library(data)


def ini_to_xml_manual(text):
    """Доп. №3: свой INI -> словарь -> свой XML."""
    data = parse_ini(text)
    return serialize_xml(data)


def measure(label, function, text):
    """Измеряет суммарное время 100 запусков функции."""
    start = perf_counter()
    for _ in range(REPEATS):
        function(text)
    elapsed_ms = (perf_counter() - start) * 1000
    print(f"{label:<32} {elapsed_ms:>9.3f} мс")


def main():
    folder = Path(__file__).resolve().parent
    text = (folder / "schedule.ini").read_text(encoding="utf-8-sig")

    print(f"Время за {REPEATS} запусков (один файл schedule.ini):")
    measure("Основное: INI -> словарь", only_ini, text)
    measure("Доп. 1: INI -> YAML (свой)", ini_to_yaml_manual, text)
    measure("Доп. 2: INI -> YAML (библиотеки)", ini_to_yaml_library, text)
    measure("Доп. 3: INI -> XML (свой)", ini_to_xml_manual, text)


if __name__ == "__main__":
    main()

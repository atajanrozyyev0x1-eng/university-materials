"""ЛР №4, вариант 87. Дополнительное №3: INI -> dict -> XML."""
import sys
from pathlib import Path

from ini_parser import parse_ini
from xml_serializer import serialize_xml


def main():
    # По умолчанию входной и выходной файлы лежат рядом с main.py.
    folder = Path(__file__).resolve().parent
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else folder / "schedule.ini"
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else folder / "schedule.xml"

    # Часть 1: существующий парсер INI строит словарь Python.
    with open(input_path, "r", encoding="utf-8-sig") as file:
        ini_text = file.read()
    data = parse_ini(ini_text)

    # Дополнительное №3: вручную превращаем словарь в XML-текст.
    xml_text = serialize_xml(data)
    with open(output_path, "w", encoding="utf-8", newline="\n") as file:
        file.write(xml_text)

    print("INI успешно разобран. Секций:", len(data))
    print("XML сохранён в:", output_path)
    print("Первые строки XML:")
    for line in xml_text.splitlines()[:8]:
        print(line)


if __name__ == "__main__":
    main()

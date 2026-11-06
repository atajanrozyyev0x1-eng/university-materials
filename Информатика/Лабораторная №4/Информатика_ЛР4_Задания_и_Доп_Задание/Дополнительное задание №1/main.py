"""ЛР №4, вариант 87: десериализация INI и сериализация в YAML."""
import sys
from ini_parser import parse_ini
from yaml_serializer import serialize_yaml


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "schedule.ini"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "schedule.yaml"

    # Обязательная часть: читаем INI и вручную превращаем его в словарь.
    with open(input_path, "r", encoding="utf-8-sig") as file:
        text = file.read()
    data = parse_ini(text)
    print("INI успешно разобран. Секций:", len(data))

    # Дополнительное №1: вручную превращаем словарь в текст YAML.
    yaml_text = serialize_yaml(data)
    with open(output_path, "w", encoding="utf-8", newline="\n") as file:
        file.write(yaml_text)

    print("YAML сохранён в:", output_path)
    print("Первые строки YAML:")
    for line in yaml_text.splitlines()[:8]:
        print(line)


if __name__ == "__main__":
    main()

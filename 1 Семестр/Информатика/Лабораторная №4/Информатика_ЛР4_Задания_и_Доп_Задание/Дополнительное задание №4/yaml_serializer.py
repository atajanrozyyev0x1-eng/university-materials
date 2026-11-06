"""Ручная сериализация результата INI-парсера в YAML (вариант 87).

Без PyYAML, json, регулярных выражений или других библиотек сериализации.
Поддерживаемая структура: dict[str, dict[str, str]], как у parse_ini().
Все строки экранируются и заключаются в двойные кавычки, чтобы YAML
не интерпретировал, например, 'true', 'null' или '08:10' как другие типы.
"""


def _quote_yaml(value):
    """Преобразует строку Python в YAML-строку с двойными кавычками."""
    if not isinstance(value, str):
        raise TypeError("Имя секции, ключ и значение должны быть строками")

    escaped = []
    for character in value:
        code = ord(character)
        if character == '"':
            escaped.append('\\"')
        elif character == "\\":
            escaped.append("\\\\")
        elif character == "\n":
            escaped.append("\\n")
        elif character == "\r":
            escaped.append("\\r")
        elif character == "\t":
            escaped.append("\\t")
        elif code < 32 or 127 <= code <= 159 or code in (0x2028, 0x2029) or 0xD800 <= code <= 0xDFFF:
            escaped.append(f"\\u{code:04X}")
        else:
            escaped.append(character)

    return '"' + "".join(escaped) + '"'


def serialize_yaml(data):
    """Превращает вложенный словарь INI в текст YAML по грамматике проекта."""
    if not isinstance(data, dict):
        raise TypeError("Ожидался словарь секций")

    lines = []
    for section_name, properties in data.items():
        if not isinstance(section_name, str) or not isinstance(properties, dict):
            raise TypeError("Секция должна иметь строковое имя и словарь свойств")

        yaml_section = _quote_yaml(section_name)
        if not properties:
            lines.append(f"{yaml_section}: {{}}")
            continue

        lines.append(f"{yaml_section}:")
        for key, value in properties.items():
            lines.append(f"  {_quote_yaml(key)}: {_quote_yaml(value)}")

    if not lines:
        return "{}\n"
    return "\n".join(lines) + "\n"

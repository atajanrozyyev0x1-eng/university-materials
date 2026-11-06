"""Ручная сериализация результата INI-парсера в XML 1.0.

Без xml.etree, DOM, regex или сторонних библиотек сериализации.
Формат данных: dict[str, dict[str, str]].
"""


def _valid_xml_character(character):
    """Проверяет, разрешён ли символ в XML 1.0 (правило Char)."""
    code = ord(character)
    return (
        code in (9, 10, 13)
        or 0x20 <= code <= 0xD7FF
        or 0xE000 <= code <= 0xFFFD
        or 0x10000 <= code <= 0x10FFFF
    )


def _escape_xml(value, attribute=False):
    """Экранирует специальные символы XML в тексте или атрибуте."""
    result = []
    for character in value:
        if not _valid_xml_character(character):
            raise ValueError(
                f"В XML 1.0 запрещён символ с кодом U+{ord(character):04X}"
            )

        if character == "&":
            result.append("&amp;")
        elif character == "<":
            result.append("&lt;")
        elif character == ">":
            result.append("&gt;")
        elif attribute and character == '"':
            result.append("&quot;")
        elif character == "\r":
            # Без ссылки XML-парсер нормализует CR в LF.
            result.append("&#13;")
        elif attribute and character == "\n":
            # В атрибутах буквальные переводы строк нормализуются в пробелы.
            result.append("&#10;")
        elif attribute and character == "\t":
            result.append("&#9;")
        else:
            result.append(character)
    return "".join(result)


def serialize_xml(data):
    """Преобразует словарь INI в XML 1.0, возвращает строку.

    Секции записываются как <section name="...">, а пары ключ-значение
    как <entry key="...">значение</entry>. Имена не становятся тегами:
    поэтому произвольные допустимые INI-имена не портят XML-разметку.
    """
    if not isinstance(data, dict):
        raise TypeError("Ожидается словарь секций")

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', "<ini_data>"]

    for section_name, properties in data.items():
        if not isinstance(section_name, str) or not isinstance(properties, dict):
            raise TypeError("Имя секции должно быть строкой, секция — словарём")

        section_attribute = _escape_xml(section_name, attribute=True)
        lines.append(f'  <section name="{section_attribute}">')

        for key, value in properties.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise TypeError("Ключ и значение в секции должны быть строками")

            key_attribute = _escape_xml(key, attribute=True)
            value_text = _escape_xml(value)
            lines.append(f'    <entry key="{key_attribute}">{value_text}</entry>')

        lines.append("  </section>")

    lines.append("</ini_data>")
    return "\n".join(lines) + "\n"

"""Ручной разбор INI по грамматике из GRAMMAR.md (вариант 87).

Без configparser, регулярных выражений и библиотек-парсеров.
Результат: dict[str, dict[str, str]]. Все значения остаются строками.
"""


def _split_assignment(line, number):
    """Разбирает правило: ключ ('=' | ':') значение."""
    # Разделитель — первый знак '=' или ':'; следующие входят в значение.
    position = -1
    for index, character in enumerate(line):
        if character == "=" or character == ":":
            position = index
            break

    if position == -1:
        raise ValueError(
            f"Строка {number}: ожидалась пара 'ключ = значение' "
            "или 'ключ : значение'"
        )

    key = line[:position].strip()
    value = line[position + 1:].strip()

    if not key:
        raise ValueError(f"Строка {number}: пустой ключ")
    for character in key:
        if character in "[]=:":
            raise ValueError(
                f"Строка {number}: недопустимый символ в ключе '{key}'"
            )

    # Значения INI не приводим к int/bool: это текстовый формат.
    return key, value


def _parse_section(line, number):
    """Разбирает правило: '[' имя_секции ']'."""
    if not line.endswith("]"):
        raise ValueError(
            f"Строка {number}: заголовок секции должен заканчиваться ']'"
        )

    name = line[1:-1].strip()
    if not name:
        raise ValueError(f"Строка {number}: пустое имя секции")
    for character in name:
        if character in "[]=":
            raise ValueError(
                f"Строка {number}: недопустимый символ в имени секции '{name}'"
            )
    return name


def parse_ini(text):
    """Десериализует INI-текст в словарь словарей.

    Поддерживает секции, '=' и ':' в качестве разделителей, пустые строки,
    полнострочные комментарии ';' и '#', пустые значения и Unicode.
    Неверный синтаксис и дубликаты вызывают ValueError с номером строки.
    """
    if not isinstance(text, str):
        raise TypeError("parse_ini ожидает аргумент типа str")

    # Если в строку напрямую попал UTF-8 BOM, игнорируем его один раз.
    if text.startswith("\ufeff"):
        text = text[1:]

    result = {}
    current_section = None

    # Одна физическая строка INI = один элемент грамматики.
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()

        # Правила: пустая_строка | строка_комментария.
        if not line or line.startswith(";") or line.startswith("#"):
            continue

        # Правило: заголовок_секции = '[' имя ']'.
        if line.startswith("["):
            section_name = _parse_section(line, line_number)
            if section_name in result:
                raise ValueError(
                    f"Строка {line_number}: повторная секция '{section_name}'"
                )
            result[section_name] = {}
            current_section = section_name
            continue

        # Правило: пара_ключ_значение — только внутри секции.
        if current_section is None:
            raise ValueError(
                f"Строка {line_number}: ключ и значение вне секции"
            )

        key, value = _split_assignment(line, line_number)
        if key in result[current_section]:
            raise ValueError(
                f"Строка {line_number}: повторный ключ '{key}' "
                f"в секции '{current_section}'"
            )
        result[current_section][key] = value

    return result

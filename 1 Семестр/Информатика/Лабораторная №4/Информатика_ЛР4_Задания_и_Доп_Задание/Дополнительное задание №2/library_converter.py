"""ЛР4, вариант 87, доп. №2: INI -> dict -> YAML с готовыми библиотеками.

configparser входит в стандартную библиотеку Python.
PyYAML (модуль yaml) устанавливается отдельно.
"""

import configparser
import yaml


def parse_ini_library(text):
    """Десериализация INI в dict[str, dict[str, str]] через configparser."""
    parser = configparser.ConfigParser(
        interpolation=None,         # Не подставлять значения %(...)s.
        strict=True,                # Повторение секции или ключа — ошибка.
        delimiters=("=", ":"),     # Поддерживаем оба разделителя.
        comment_prefixes=(";", "#"),
        inline_comment_prefixes=None,  # '#' и ';' внутри значения — текст.
        allow_no_value=False,
        empty_lines_in_values=False,
    )
    parser.optionxform = str       # Не переводить ключи в нижний регистр.
    parser.read_string(text)

    # Обычный dict, как у нашей ручной реализации.
    result = {}
    for section_name in parser.sections():
        result[section_name] = dict(parser.items(section_name, raw=True))
    return result


def serialize_yaml_library(data):
    """Сериализация вложенного словаря в YAML с помощью PyYAML."""
    return yaml.safe_dump(
        data,
        allow_unicode=True,       # Русский текст сохраняем читаемым.
        sort_keys=False,          # Сохраняем порядок секций и полей.
        default_flow_style=False, # Вложенные словари с отступами.
        indent=2,
        width=1000,
    )

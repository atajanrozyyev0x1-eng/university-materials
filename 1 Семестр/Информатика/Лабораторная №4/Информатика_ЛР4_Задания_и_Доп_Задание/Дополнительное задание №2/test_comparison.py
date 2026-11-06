"""Необязательные автотесты для дополнительного задания №2."""

import unittest
import yaml

from ini_parser import parse_ini
from yaml_serializer import serialize_yaml
from library_converter import parse_ini_library, serialize_yaml_library


class ConverterComparisonTests(unittest.TestCase):
    def assert_same_data(self, text):
        manual = parse_ini(text)
        ready = parse_ini_library(text)
        self.assertEqual(manual, ready)
        self.assertEqual(yaml.safe_load(serialize_yaml(manual)), manual)
        self.assertEqual(yaml.safe_load(serialize_yaml_library(ready)), ready)

    def test_schedule_style(self):
        self.assert_same_data(
            "[lesson]\nsubject = Информатика\ntime = 13:30\nroom = 1327\n"
        )

    def test_comments_and_empty_values(self):
        self.assert_same_data(
            "; файл\n[Section]\n# комментарий\nempty =\ntext : a=b:c\n"
        )

    def test_punctuation_and_string_values(self):
        self.assert_same_data(
            "[Student]\nName=Alex\nactive=true\nage=19\n"
            "url=https://example.com/?x=1#fragment\n"
        )

    def test_empty_sections_and_empty_file(self):
        self.assert_same_data("[first]\n\n[second]\n")
        self.assert_same_data("\n; только комментарий\n")

    def test_repeated_sections(self):
        text = "[a]\nx=1\n[a]\ny=2\n"
        with self.assertRaises(ValueError):
            parse_ini(text)
        with self.assertRaises(Exception):
            parse_ini_library(text)

    def test_repeated_keys(self):
        text = "[a]\nx=1\nx=2\n"
        with self.assertRaises(ValueError):
            parse_ini(text)
        with self.assertRaises(Exception):
            parse_ini_library(text)

    def test_special_yaml_strings(self):
        self.assert_same_data(
            '[s]\nname=\"quoted\"\nyes=true\nnull=null\nnumber=001\n'
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

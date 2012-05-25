#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Language
import os

os.chdir(os.path.realpath(__file__).rpartition('/')[0])

DESKTOP_FILE = os.path.join(os.getcwd(), 'data/share/applications/emesene.desktop')

def write_to_file(line_number, string_type, language, string):
    global DESKTOP_FILE
    df = open(DESKTOP_FILE, 'r')
    text = ''
    for i, line in enumerate(df.readlines()):
        text += line
        if i == line_number:
            text += string_type + '[' + language + ']=' + string + '\n'
    df.close()
    df = open(DESKTOP_FILE, 'w')
    df.write(text)
    df.close()

language_management = Language.Language()
language_management.install_desired_translation(None)

%%%%%%%

number_of_translations = [0 for i in line_numbers]
for language in language_management.LANGUAGES_DICT.iterkeys():
    language_management.install_desired_translation(language)
    for idx, string in enumerate(translatable_strings):
        translated_string = _(string)
        if translated_string not in translatable_strings:
            write_to_file(line_numbers[idx]+sum(number_of_translations[:idx]), string_types[idx], language, translated_string)
            number_of_translations[idx] += 1

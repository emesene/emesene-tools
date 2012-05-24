#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gettext
import Language
import os

_ = gettext.gettext
os.chdir(os.path.realpath(__file__).rpartition('/')[0])

DESKTOP_FILE = os.path.join(os.getcwd(), 'data/share/applications/emesene.desktop')

def write_to_file(line_number, string_type, language, string):
    global DESKTOP_FILE
    df = open(DESKTOP_FILE, 'w')
    text = ''
    for i, line in enumerate(df.readlines()):
        text += line + '\n'
        if i == line_number:
            text += string_type + '[' + language + ']=' + string


%%%%%%%

original_strings = translatable_strings

language_management = Language.Language()

i = 0
for language in language_management.LANGUAGES_DICT.iterkeys():
    language_management.install_desired_translation(language)
    print original_strings
    for idx, string in enumerate(translatable_strings):
        print string
        if string not in original_strings:
            write_to_file(line_numbers[idx]+i, string_types[idx], language, string)
            i += 1

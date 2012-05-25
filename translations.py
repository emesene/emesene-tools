#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import subprocess
import gettext
import shutil

_ = gettext.gettext

EMESENE_DIR = os.path.expanduser('~/emesene-dev')
EMESENE_DIR2 = os.path.join(EMESENE_DIR, 'emesene')
CURRENT_DIR = os.getcwd()
FILE_LIST = ['*.py', 'e3/base/*.py', 'e3/common/*.py', 'e3/papylib/*.py', 'gui/base/*.py', 'gui/gtkui/*.py', 'gui/common/*.py']
DESKTOP_FILE = os.path.join(EMESENE_DIR2, 'data/share/applications/emesene.desktop')
BLACKLIST = ['emesene']

os.chdir(EMESENE_DIR)

# Remove all translations from the desktop file
df = open(DESKTOP_FILE, 'r')
text = ''
for line in df.readlines():
    if not line.startswith('Comment[') and not line.startswith('Name['):
        text += line
df.close()
df = open(DESKTOP_FILE, 'w')
df.write(text)
df.close()

# Find strings that have to be translated in the desktop file
desktop_file = open(DESKTOP_FILE, 'r')
strings = []
indices = []
types = []
for i, line in enumerate(desktop_file.readlines()):
    if line.startswith('Name='):
        text = line[5:-1]
        if text in BLACKLIST:
            continue
        strings.append(text)
        indices.append(i)
        types.append('Name')
    if line.startswith('Comment='):
        text = line[8:-1]
        if text in BLACKLIST:
            continue
        strings.append(text)
        indices.append(i)
        types.append('Comment')
desktop_file.close()

def list2str(l, trans=False):
    start = '_(\''
    end = '\')'
    return '['+start+(end+', '+start).join(l)+end+']'

shutil.copy(os.path.join(CURRENT_DIR, 'temp_translations_file.py'), EMESENE_DIR2)
temp_translations_file = open(os.path.join(EMESENE_DIR2, 'temp_translations_file.py'), 'r')
text = ''
text += 'translatable_strings = '+list2str(strings)+'\n'
text += 'line_numbers = '+str(indices)+'\n'
text += 'string_types = '+str(types)+'\n'

write_text = temp_translations_file.read()
temp_translations_file.close()
temp_translations_file = open(os.path.join(EMESENE_DIR2, 'temp_translations_file.py'), 'w')
write_text = write_text.replace('%%%%%%%', text)
temp_translations_file.write(write_text)
temp_translations_file.close()

args = ['xgettext']
args.extend([os.path.join('emesene', f) for f in FILE_LIST])
args.append('-o')
args.append(os.path.join(EMESENE_DIR, 'emesene.pot'))
args.append(os.path.join(CURRENT_DIR, 'translations.py'))
args = ' '.join(args)

subprocess.call(args, shell=True)
subprocess.call('python '+os.path.join(EMESENE_DIR2, 'temp_translations_file.py'), shell=True)
os.remove(os.path.join(EMESENE_DIR2, 'temp_translations_file.py'))

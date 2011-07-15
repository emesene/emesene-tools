# #!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import subprocess

def list_files(dir):
    basedir = dir
    subdirlist = []
    file_list = []
    for item in os.listdir(dir):
        path = os.path.join(basedir, item)
        if os.path.isdir(path) and 'papyon' not in path and 'xmppy' not in path:
            subdirlist.append(path)
        elif item.rpartition('.')[2] == 'py':
            file_list.append(path)
    for subdir in subdirlist:
        file_list.extend(list_files(subdir))
    return file_list

def test(line):
    return '.' in line and "'''" not in line and '"""' not in line and \
    '#' not in line

files = list_files(os.path.expanduser('~/emesene'))
output = ''
for _file in files:
    if _file == os.path.expanduser('~/emesene/emesene/e3/common/Signal.py'):
        continue
    worker_file = open(_file, 'r')
    lines = worker_file.readlines()
    signal_list = []
    for i, line in enumerate(lines):
        if 'subscribe' in line and test(line):
            signal = '.'.join(line.partition('(')[0].strip().split('.')[0:-1])
            if 'unsubscribe' in line:
                pass
            else:
                #signal_list[signal] = _file
                signal_list.append(signal)
    for i, line in enumerate(lines):
        if 'unsubscribe' in line and test(line):
            signal = '.'.join(line.partition('(')[0].strip().split('.')[0:-1])
            #del signal_list[signal]
            signal_list.remove(signal)
    if len(signal_list) != 0:
        splfile = _file.split('/')
        output+= '/'.join(splfile[4:len(splfile)]) + '\n\n'
        for signal in signal_list:
            output += signal + '\n'
        output += '\n'
output_file = open('unsubscribed_signals.txt', 'w')
output_file.write(output)
output_file.close()

subprocess.call('diff -U 1000 original_unsubscribed_signals.txt unsubscribed_signals.txt > diff.txt', shell=True)
diff_file = open('diff.txt', 'r')
lines = diff_file.readlines()
diff_file.close()
output = ''
for i, line in enumerate(lines):
    if i < 3:
        continue
    elif line[0] == '-':
        output += '<del>'+line[1:-1]+'</del>\n'
    else:
        output += line[1:]

diff_file = open('diff.txt', 'w')
lines = diff_file.write(output)
diff_file.close()

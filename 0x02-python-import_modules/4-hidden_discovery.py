#!/usr/bin/python3
import py_compile
import sys

py_compile.compile('hidden_4.py')

with open('hidden_4.pyc', 'rb') as file:
    magic = file.read(4)
    moddate = file.read(4)
    code = file.read()

    module = sys.modules['__main__']
    exec(code, module.__dict__)

names = [name for name in dir(module) if not name.startswith('__')]
names.sort()

for name in names:
    print(name)

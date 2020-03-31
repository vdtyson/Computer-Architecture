#!/usr/bin/env python3

"""Main."""

import sys
from ls8.cpu import CPU
from typing import DefaultDict, Dict


def start_ls8(cpu: type(CPU), file_name: str):
    cpu.load(file_name)
    cpu.run()


if __name__ == '__main__':
    c_pu: type(CPU) = CPU()
    file_name_input: str = input("Input unique file name (examples/[unique file name].ls8): ")
    start_ls8(c_pu, f'examples/{file_name_input}.ls8')

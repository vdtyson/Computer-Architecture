#!/usr/bin/env python3

"""Main."""

import sys
from ls8.cpu import CPU


def run_ls8(cpu: type(CPU), file_name: str):
    cpu.load(file_name)
    cpu.run()


if __name__ == '__main__':
    file: str = input("Enter file name: ")
    run_ls8(CPU(), file)

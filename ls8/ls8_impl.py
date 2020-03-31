#!/usr/bin/env python3

"""Main."""

import sys
from ls8.cpu import CPU

if __name__ == '__main__':
    cpu = CPU()
    cpu.set_instruction_dispatcher()
    cpu.load()
    cpu.run()

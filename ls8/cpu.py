"""CPU functionality."""

import sys
from typing import List, Dict, Any
from ls8.cpu_components.cpu_reg import CPUReg
from ls8.cpu_components.cpu_ram import CPURam

# Instructions for today
"""
Day 2:

Un-hardcode the machine code

Implement the load() function to load an .ls8 file given the filename passed in as an argument

Implement a Multiply instruction (run mult.ls8)
"""


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Program Counter -- address of the currently executing instruction
        self.pc: int = 0
        # Flags -- holds the current flag status
        self.fl: int = 0
        self.ir: int = 0
        self.reg: List[int] = [0] * 8
        self.ram: List[int] = [0] * 256
        self.instruction_dispatcher: Dict = {
            0b00000001: lambda _, __: self._hlt(),
            0b10000010: lambda op_a, op_b: self._ldi(op_a, op_b),
            0b01000111: lambda op_a, _: self._prn(op_a),
            0b10100010: lambda op_a, op_b: self._mul(op_a, op_b)
        }

    @staticmethod
    def _hlt():
        print("\nHalted.")
        sys.exit(0)

    def _ldi(self, operand_a: int, operand_b: int):
        self.reg[operand_a] = operand_b
        self.ir += 3

    def _prn(self, operand_a: int):
        print(self.reg[operand_a])
        self.ir += 2

    def _mul(self, operand_a: int, operand_b: int):
        self.reg[operand_a] = self.reg[operand_a] * self.reg[operand_b]
        self.ir += 3

    # Memory Address Register -- holds the memory address we're reading or writing
    # Memory Data Register -- holds the value to write or the value just read
    def ram_read(self, mar: int) -> int:
        mdr = self.ram[mar]
        return mdr

    def ram_write(self, mar: int, mdr: int):
        self.ram[mar] = mdr

    def load(self, file_name: str):
        """Load a program into memory."""

        print("Loading program. Beep bop boop\n")

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #    # From print8.ls8
        #    0b10000010,  # LDI R0,8
        #    0b00000000,
        #    0b00001000,
        #    0b01000111,  # PRN R0
        #    0b00000000,
        #    0b00000001,  # HLT
        # ]

        with open(file_name) as f:
            lines: List[str] = f.readlines()
            lines = [line for line in lines if line.startswith('0') or line.startswith('1')]
            program: List[int] = [int(line[:8], 2) for line in lines]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        is_running: bool = True

        # Instruction Register -- contains a copy of the currently executing instruction
        self.ir = self.pc

        while is_running:
            instruction = self.ram_read(self.ir)
            operand_a = self.ram_read(self.ir + 1)
            operand_b = self.ram_read(self.ir + 2)
            self.instruction_dispatcher[instruction](operand_a, operand_b)

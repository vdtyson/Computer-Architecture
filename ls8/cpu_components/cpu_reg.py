from typing import List


class Register:
    pass


class CPUReg:

    def __init__(self):
        # Program Counter -- address of the currently executing instruction
        self.pc: int = 0
        # Instruction Register -- contains a copy of the currently executing instruction
        self.ir: int = 0
        # Memory Address Register -- holds the memory address we're reading or writing
        self.mar: int = 0
        # Memory Data Register -- holds the value to write or the value just read
        self.mdr: int = 0
        # Flags -- holds the current flage status
        self.fl: int = 0

        self.registry: List[int] = [0] * 8

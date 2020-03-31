from typing import List


class CPURam:
    def __init__(self):
        self.storage: List[int] = [0] * 256

    def read(self, address: int):
        return self.storage[address]

    def write(self, address: int, value):
        self.storage[address] = value

"""
tape.py

A Brainfuck tape.
"""

import sys


MAX = 256 # A cell is represented by an unsigned, 8-bit integer.


class Tape():
    __tape: bytearray
    __index: int

    def __init__(self, size: int) -> None:
        self.__tape = bytearray(size)
        self.__index = 0

    def __len__(self) -> int:
        """
        Return the length of the Tape.
        """
        return len(self.__tape)

    def add(self, n: int) -> None:
        """
        Add `n` to the current cell of the tape.
        """
        self.value += n

    def move(self, n: int) -> None:
        """
        Move the current cell by `n`.
        """
        if self.__index + n < 0:
            raise ValueError("cannot move current cell below 0")

        if self.__index >= len(self):
            raise ValueError(
                "cannot move current cell beyond size ({})".format(len(self))
            )

        self.__index += n

    @property
    def value(self) -> int:
        """
        The value of the tape at the current index.
        """
        return self.__tape[self.__index]

    @value.setter
    def value(self, n: int) -> None:
        self.__tape[self.__index] = n % MAX

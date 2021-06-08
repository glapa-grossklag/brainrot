"""
tape.py

A representation of the tape.
"""

import sys
import constants


class Tape():
    _tape: bytearray
    _index: int

    def __init__(self, size: int = constants.TAPE_LENGTH) -> None:
        self._tape = bytearray(size)
        self._index = 0

    def __len__(self) -> int:
        """
        Return the length of the Tape.
        """
        return len(self._tape)

    def move(self, n: int) -> None:
        """
        Move the current cell by `n`.
        """
        if self._index + n < 0:
            raise ValueError("cannot move current cell below 0")

        if self._index >= len(self):
            raise ValueError(
                "cannot move current cell beyond size ({})".format(len(self))
            )

        self._index += n

    @property
    def value(self) -> int:
        """
        The value of the tape at the current index.
        """
        return self._tape[self._index]

    @value.setter
    def value(self, n: int) -> None:
        self._tape[self._index] = n % constants.CELL_MAX

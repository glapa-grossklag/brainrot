"""
A Brainfuck tape.
"""

import sys
from typing import TextIO


MAX = 256 # A cell is represented by an unsigned, 8-bit integer.


class Tape():
    input_file: TextIO
    output_file: TextIO
    __tape: list[int]
    __index: int

    def __init__(self, size: int, input_file: TextIO = sys.stdin, output_file: TextIO = sys.stdout) -> None:
        self.__tape = [0] * size
        self.__index = 0
        self.input_file = input_file
        self.output_file = output_file

    def __len__(self) -> int:
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
        return self.__tape[self.__index]

    @value.setter
    def value(self, n: int) -> None:
        self.__tape[self.__index] = n % MAX

    def apply(self, code: str) -> None:
        i = 0

        while i < len(code):
            c = code[i]

            if c == '>':
                self.move(1)

            elif c == '<':
                self.move(-1)

            elif c == '+':
                self.add(1)

            elif c == '-':
                self.add(-1)

            elif c == '.':
                self.output_file.write(chr(self.value))

            elif c == ',':
                self.value = ord(self.input_file.read(1))

            elif c == '[':
                # If the byte at the data pointer is zero, then instead of moving
                # the instruction pointer forward to the next command, jump it
                # forward to the command after the matching ] command.
                if self.value == 0:
                    found = False
                    skip = 0

                    # Find matching ']'
                    for j in range(i + 1, len(code)):
                        if found:
                            break

                        if code[j] == '[':
                            # Skip over nested loops.
                            skip += 1
                        elif code[j] == ']':
                            if skip == 0:
                                i = j
                                found = True
                            else:
                                skip -= 1
                    else:
                        raise SyntaxError("missing closing bracket")

            elif c == ']':
                # If the byte at the data pointer is nonzero, then instead of
                # moving the instruction pointer forward to the next command, jump
                # it back to the command after the matching [ command.
                if self.value != 0:
                    found = False
                    skip = 0

                    for j in range(i - 1, -1, -1):
                        if found:
                            break

                        if code[j] == ']':
                            # Skip over nested loops.
                            skip += 1
                        elif code[j] == '[':
                            if skip == 0:
                                i = j
                                found = True
                            else:
                                skip -= 1
                    else:
                        raise SyntaxError("missing open bracket")

            i += 1

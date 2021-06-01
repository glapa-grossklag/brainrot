"""
bipy.py

This module is the actual Brainfuck interpreter.
"""


import sys
from tape import Tape
from typing import IO


def evaluate(code: str, tape: Tape, input_file: IO = sys.stdin, output_file: IO = sys.stdout) -> None:
    """
    Evaluate given Brainfuck code and apply it to the given Tape.
    """
    i = 0

    while i < len(code):
        c = code[i]

        if c == '>':
            tape.move(1)

        elif c == '<':
            tape.move(-1)

        elif c == '+':
            tape.add(1)

        elif c == '-':
            tape.add(-1)

        elif c == '.':
            output_file.write(chr(tape.value))

        elif c == ',':
            tape.value = ord(input_file.read(1))

        elif c == '[':
            # If the byte at the data pointer is zero, then instead of moving
            # the instruction pointer forward to the next command, jump it
            # forward to the command after the matching ] command.
            if tape.value == 0:
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
            if tape.value != 0:
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

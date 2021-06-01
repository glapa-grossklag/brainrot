"""
bipy.py

The actual Brainfuck interpreter.
"""


import sys
from tape import Tape
from typing import IO


def evaluate(code: str, tape: Tape, input_file: IO = sys.stdin, output_file: IO = sys.stdout) -> None:
    """
    Evaluate Brainfuck code and apply it to the Tape.

    Read from stdin and write to stdout by default.
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
            # If the byte at the data pointer is zero, then jump the
            # instruction pointer forward to the command after the matching
            # ']'.
            if tape.value == 0:
                skip = 0  # The number of nested loops to skip over.

                # Find matching ']'.
                for j in range(i + 1, len(code)):
                    if code[j] == '[':
                        skip += 1
                    elif code[j] == ']':
                        if skip == 0:
                            i = j
                            break
                        else:
                            skip -= 1
                else:
                    raise SyntaxError("missing closing bracket")

        elif c == ']':
            # If the byte at the data pointer is non-zero, then jump the
            # instruction pointer back to the command after the matching '['.
            if tape.value != 0:
                skip = 0  # The number of nested loops to skip over.

                # Find matching '['.
                for j in range(i - 1, -1, -1):
                    if code[j] == ']':
                        skip += 1
                    elif code[j] == '[':
                        if skip == 0:
                            i = j
                            break
                        else:
                            skip -= 1
                else:
                    raise SyntaxError("missing open bracket")

        i += 1

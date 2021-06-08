"""
bipy.py

The actual Brainrot interpreter.
"""


import sys
from typing import IO

from constants import NameSpace
from tape import Tape

def evaluate(code: str, tape: Tape, namespace: NameSpace, input_file: IO = sys.stdin, output_file: IO = sys.stdout) -> None:
    """
    Evaluate Brainrot code and apply it to the Tape.

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
            tape.value += 1

        elif c == '-':
            tape.value -= 1

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

        elif c == '(':
            name = tape.value
            definition = ""

            # Find matching ')'.
            for j in range(i + 1, len(code)):
                if code[j] == '(':
                    raise SyntaxError("illegal nested function definition")

                elif code[j] == ')':
                    namespace[name] = definition
                    i = j
                    break

                else:
                    definition += code[j]
            else:
                raise SyntaxError("missing closing parenthesis")

        elif c == ')':
            # The `c == '('` case will handle any closing parenthesis, so this
            # shouldn't ever be seen.
            raise SyntaxError("missing opening parenthesis")

        elif c == '!':
            # Adjust `code` to contain the definition.
            if tape.value in namespace:
                code = code[:i + 1] + namespace[tape.value] + code[i + 1:]

        i += 1

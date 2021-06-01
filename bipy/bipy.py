"""
A Brainfuck interpreter.
"""

import sys
from tape import Tape


def printerr(*args, **kwargs):
    """
    Print to stderr using the same syntax as the built-in print function.
    """
    print(*args, file=sys.stderr, **kwargs)


def main() -> None:
    program = None

    # CLI Arguments
    if len(sys.argv) != 2:
        printerr("Usage:")
        printerr("    {} <input file>".format(sys.argv[0]))
        exit(2)

    try:
        program = open(sys.argv[1], "r")
    except OSError:
        printerr("Failed to open '{}'".format(sys.argv[1]))

    # Interpret
    tape = Tape(30000)
    tape.input_file = sys.stdin
    tape.output_file = sys.stdout

    code = "".join(program.readlines())

    tape.apply(code)

"""
__main__.py

The driver code to read and interpret a Brainfuck source file.
"""

import sys
import bipy
import util
from tape import Tape


def main() -> None:
    program = None

    # CLI Arguments
    if len(sys.argv) != 2:
        util.printerr("Usage:")
        util.printerr("    {} <input file>".format(sys.argv[0]))
        exit(2)

    try:
        program = open(sys.argv[1], "r")
    except OSError:
        util.printerr("Failed to open '{}'".format(sys.argv[1]))
        exit(2)

    tape = Tape(30000)
    code = "".join(program.readlines())
    bipy.evaluate(code, tape)


if __name__ == "__main__":
    main()

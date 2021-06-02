"""
__main__.py

The driver code to read and interpret a Brainfuck source file.
"""

import sys
import bipy
import util
from tape import Tape


def main() -> None:
    sourcefile = sys.stdin

    # CLI Arguments
    if len(sys.argv) > 2:
        util.printerr("Usage:")
        util.printerr("    {} <input file>".format(sys.argv[0]))
        exit(2)

    if len(sys.argv) == 2:
        try:
            sourcefile = open(sys.argv[1], "r")
        except OSError:
            util.printerr("Failed to open '{}'".format(sys.argv[1]))
            exit(2)
    else:
        # Input is stdin.
        print("Welcome to bipy: a Brainfuck Interpreter in Python")

    tape = Tape(30000)
    code = sourcefile.read()
    bipy.evaluate(code, tape)
    sourcefile.close()


if __name__ == "__main__":
    main()

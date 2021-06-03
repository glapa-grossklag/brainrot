"""
__main__.py

The driver code to read and interpret a Brainfuck source file.
"""


import sys
import bipy
import util
import constants
from tape import Tape


def main() -> None:
    sourcefile = sys.stdin
    tape = Tape(constants.DEFAULT_TAPE_SIZE)

    if len(sys.argv) > 2:
        util.printerr("Usage:")
        util.printerr("    {} <input file>".format(sys.argv[0]))
        exit(2)

    elif len(sys.argv) == 2:
        try:
            sourcefile = open(sys.argv[1], "r")
        except OSError:
            util.printerr("Failed to open '{}'".format(sys.argv[1]))
            exit(2)

        code = sourcefile.read()
        bipy.evaluate(code, tape)

    elif len(sys.argv) == 1:
        # REPL
        print("Welcome to bipy: a Brainfuck Interpreter in Python")
        while True:
            line = input(constants.PROMPT)
            bipy.evaluate(line, tape)

    sourcefile.close()


if __name__ == "__main__":
    main()

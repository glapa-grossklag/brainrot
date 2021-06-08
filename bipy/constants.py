"""
constants.py
"""

from typing import TypedDict


# The length of the tape.
TAPE_LENGTH = 2 ** 16

# A cell is one eight-bit, unsigned integer.
CELL_MAX = 255

# The prompt for the REPL.
PROMPT = "[bipy] "

# A NameSpace represents a mapping of the value of a cell (within 0 - MAX,
# usually 0 - 255) to code (as a string).
NameSpace = TypedDict("NameSpace", { n: str for n in range(0, CELL_MAX + 1) })

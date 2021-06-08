"""
constants.py
"""

# A NameSpace represents a mapping of the value of a cell (within 0 - MAX,
# usually 0 - 255) to code (as a string).
NameSpace = TypedDict("NameSpace", { n: str for n in range(0, MAX + 1) })

DEFAULT_TAPE_SIZE = 2 ** 16
PROMPT = "[bipy] "

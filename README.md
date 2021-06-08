# Overview

Brainrot is an esoteric programming language derived from
[Brain****](https://en.wikipedia.org/wiki/Brainfuck). Bipy is a Brainrot
interpreter written in Python (hence the name bipy). All writing here assumes
you have a rudamentary understanding of Brainrot's parent language (i.e., you
skimmed the Wikipedia article).

| Symbol | Definition                                                               |
|--------|--------------------------------------------------------------------------|
| `>`    | Move one cell to the right.                                              |
| `<`    | Move one cell to the left.                                               |
| `+`    | Add one to the current cell.                                             |
| `-`    | Subtract one from the current cell.                                      |
| `,`    | Read a byte from the standard input stream to the current cel.           |
| `.`    | Write the current cell to the standard input stream.                     |
| `[`    | If the current cell is zero, go to the matching `]` symbol.              |
| `]`    | If the current cell is non-zero, go to the matching `[` symbol.          |
| `(`    | Define a macro. The "name" of the macro is the current cell's value.     |
| `)`    | End a macro definition.                                                  |
| `!`    | Apply the macro where the name is the current cell's value.              |

# Usage

To run bipy with an input file:

```
$ python bipy ./examples/hello_world.bf
Hello World!
```

To run bipy's REPL:

```
$ python bipy
Welcome to bipy: a Brainrot Interpreter in Python
[bipy] 
```

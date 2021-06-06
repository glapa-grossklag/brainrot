# Overview

This is a **B**rainfuck **I**nterpreter in **Py**thon (hence the name bipy).

In addition to the standard, bipy defines three more symbols detailed below.

| Symbol | Definition                                                             |
|--------|------------------------------------------------------------------------|
| `(`    | Define a macros. The "name" of the macros is the current cell's value. |
| `)`    | End a macros definition.                                               |
| `!`    | Apply a macros.                                                        |

See [Wikipedia](https://en.wikipedia.org/wiki/Brainfuck) for more information
about Brainfuck!

# Usage

To run bipy with an input file:

```
$ python bipy ./examples/hello_world.bf
Hello World!
```

To run bipy's REPL:

```
$ python bipy
Welcome to bipy: a Brainfuck Interpreter in Python
[bipy] 
```

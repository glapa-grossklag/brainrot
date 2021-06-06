# Overview

This is a **B**rainfuck **I**nterpreter in **Py**thon (hence the name bipy).

In addition to the standard, bipy defines three more symbols detailed below.
For an example of these new symbols in use, see [](examples/macro-smile.bf).

| Symbol | Definition                                                           |
|--------|----------------------------------------------------------------------|
| `(`    | Define a macro. The "name" of the macro is the current cell's value. |
| `)`    | End a macro definition.                                              |
| `!`    | Apply a macro.                                                       |

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

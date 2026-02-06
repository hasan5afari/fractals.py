## Summary

This project is an implementation of the mathematical fractals using Python.
I used Lindenmayer System to represent a fractal and then used pygame module
to visualize it.

## Lindenmayer System

Lindenmayer System is a formal grammar used to describe a system, also it has
a mechanism for translating generated strings into geometric structures. formally
we have:

**G** = (V, ω, P)

- V - Alphabet (Variables + Terminals)
- ω - Axiom (Initial string)
- P - Production rules (Set of rules defining the way that each variables can be replaced with combination of terminals and other variables)

**Geometric translation mechanism**

-  'F' - Move forward by line length drawing a line
-  'f' - Move forward by line length without drawing a line
-  '\+' - Turn left by turning angle
-  '\-' - Turn right by turning angle
-  '|' - Reverse direction (ie: turn by 180 degrees)
-  '[' - Push current drawing state onto stack
-  ']' - Pop current drawing state from the stack
-  '\#' - Increment the line width by line width increment
-  '!' - Decrement the line width by line width increment
-  '@' - Draw a dot with line width radius
-  '{' - Open a polygon
-  '}' - Close a polygon and fill it with fill colour
-  '>' - Multiply the line length by the line length scale factor
-  '<' - Divide the line length by the line length scale factor
-  '&' - Swap the meaning of + and -
-  '(' - Decrement turning angle by turning angle increment
-  ')' - Increment turning angle by turning angle increment

## Examples

#### Triangle fractal

<img src="https://github.com/hasan5afari/fractals.py/blob/main/previews/Triangle.gif" width="500" height="350"/>
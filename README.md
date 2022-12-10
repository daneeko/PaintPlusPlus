# Paint++
Paint++ : Graphical esolang using only Microsoft Paint's default colors.

This is an esolang, that much like Piet, uses images as programs. Code is read by the 'code pointer', which starts at the top left of the image, with its direction indicating to move 1 pixel to the right every step. Every time it steps on a pixel, it executes the instruction its color represents. Data storage is handled very much like brainfuck (via a tape of cells), however every cell has a range of 0-65535 instead of 0-255. Additionally, the program stops when the code pointer steps outside of the bounds of the image/program.

Functions of all 20 colors:

White           (FFFFFF): Empty space, does nothing.

Black           (000000): Outputs the value of the memory cell (as a character).

Gray-25%        (C3C3C3): Stops the program.

Gray-50%        (7F7F7F): Input a value to replace the value of the memory cell (as a character).

Brown           (B97A57): Sets the value of the memory cell to 65535 minus itself.

Dark red        (880015): Moves 2 steps forward in the current direction, instead of 1.

Rose            (FFAEC9): Sets value of the memory cell to a random number between 0 and 65535.

Red             (ED1C24): Turn the code pointer 90 degrees left.

Gold            (FFC90E): Turn the code pointer 180 degrees.

Orange          (FF7F27): Set the code pointer's direction to upwards if the value of the memory cell is non-zero, otherwise set it downwards.

Light yellow    (EFE4B0): Set value of memory cell to sum of values of its two adjacent cells.

Yellow          (FFF200): Turn the code pointer 90 degrees right.

Lime            (B5E61D): Move data pointer one cell to the right.

Green           (22B14C): Move data pointer one cell to the left.

Light turquoise (99D9EA): Subtract 1 from value of memory cell.

Turquoise       (00A2E8): Add 1 to value of memory cell.

Blue-gray       (7092BE): Divide value of memory cell by the value of the next cell.


Indigo          (3F48CC): Multiply value of memory cell by the value of the next cell.

Lavender        (C8BFE7): Move [value of memory cell] steps backwards in current direction.

Purple          (A349A4): Move [value of memory cell] steps forwards in current direction.

Note: Invalid colors are treated as empty space as well.

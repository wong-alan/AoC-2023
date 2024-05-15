# Advent of Code 2023

A small repository documenting solutions for AoC 2023 in Python3.

Find the puzzles at: https://adventofcode.com/2023

____
### To run:
Add your puzzle input as `input.txt` within the corresponding "day directory".

#### In PyCharm:
- Run as is

> For running in Terminal and VSCode we will need to do some tweaking to use the `@timed` decorator
- Above the import for `from utils import timed`, add the following
```
  import sys
  import os
  sys.path.append(os.path.abspath(".."))
```
#### In Terminal:
- Run from within each "day directory"
- ex. `cd 2023/1`  >>  `python3 program.py`

#### In VSCode:

- Install Python extension
- Open Settings:
  - Windows/Linux - File > Preferences > Settings
  - macOS - Code > Preferences > Settings
- Set workspace setting:
  - Check the checkbox at: Extensions > Python > Terminal: Execute In File Dir
  - Set `python.terminal.executeInFileDir` to `true`
- Run `program.py`
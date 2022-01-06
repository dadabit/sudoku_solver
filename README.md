# sudoku_solver
A sudoku solver

## What is Sudoku?
Sudoku (Japanese: 数独, romanized: sūdoku). originally called Number Place) is a logic-based, combinatorial number-placement puzzle.
more on https://en.wikipedia.org/wiki/Sudoku

### Dependency:
* python3
* shell
* macos or linux
  
---

### Simply Running:

```
python3 sudoku.py puzzle.sudoku
python3 sudoku.py -info
```

### Installing:

```
./install.sh
sudoku puzzle.sudoku
sudoku -info
```

---

## .sudoku file formatting

all space are ignored, just keep in mind that a there is 9 character in a row and 9 character in a column.

#### sample file: puzzle.sudoku

```
9 0 0 7 4 0 0 0 0
0 1 0 0 0 0 0 0 0
4 0 0 0 0 1 0 6 7
0 9 0 0 5 0 6 0 4
0 0 5 0 7 0 2 0 0
6 0 4 0 2 0 0 8 0
3 8 0 5 0 0 0 0 1
0 0 0 0 0 0 0 5 0
0 0 0 0 6 3 0 0 8
```

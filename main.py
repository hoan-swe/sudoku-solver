from Generator import GRID
from SolvingAlgorithm import *


s1 = [[9,0,0,6,0,0,0,0,1],
      [0,0,0,0,0,3,0,8,5],
      [0,0,1,0,2,0,0,0,0],
      [0,0,0,5,0,7,0,0,0],
      [6,0,4,0,0,0,1,0,7],
      [0,9,0,0,0,0,0,0,0],
      [5,0,0,0,0,0,0,7,0],
      [0,0,2,0,1,0,0,0,0],
      [8,0,0,0,4,5,0,0,9]]

solution = [[9, 8, 7, 6, 5, 4, 3, 2, 1],
           [2, 4, 6, 1, 7, 3, 9, 8, 5],
           [3, 5, 1, 9, 2, 8, 7, 4, 6],
           [1, 2, 8, 5, 3, 7, 6, 9, 4],
           [6, 3, 4, 8, 9, 2, 1, 5, 7],
           [7, 9, 5, 4, 6, 1, 8, 3, 2],
           [5, 1, 9, 2, 8, 6, 4, 7, 3],
           [4, 7, 2, 3, 1, 9, 5, 6, 8],
           [8, 6, 3, 7, 4, 5, 2, 1, 9]]
sudoku = GRID(s1)

Solve_sudoku(sudoku)
#Solve_sudoku(sudoku)

print(f'\nMain Func: {sudoku.solve}\nUpdate Func: {sudoku.update}\nEasy Func: {sudoku.easy}\nHard Func: {sudoku.hard}')

print(f'\nRow: {sudoku.row} Col: {sudoku.col} Box: {sudoku.box}')

print(f'\nUnsolved: {len(sudoku.answers_dict.keys())}')

if sudoku.grid == solution:
  print()
  print('SOLVED!')
else:
  print()
  print('WRONG!')

if sudoku.answers_dict:
  print()
  print('Cannot be solved without guessing!')

'''for pos in sudoku.answers_dict:
  print(f'P: {pos} A: {sudoku.answers_dict[pos]}')'''
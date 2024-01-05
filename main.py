from ValidCheck import *
from Generator import *
from SolvingAlgorithm import *

s1 = [[4,0,9,0,0,8,0,3,7],
     [0,5,0,0,3,2,0,1,8],
     [1,0,0,5,0,0,2,0,6],
     [8,0,0,0,0,3,0,0,0],
     [0,3,0,0,4,0,0,7,5],
     [0,0,1,0,0,7,0,0,0],
     [0,0,0,4,0,0,0,0,9],
     [0,1,0,0,0,0,0,4,2],
     [2,0,4,0,1,0,0,5,0]]

solution = [[4, 2, 9, 1, 6, 8, 5, 3, 7],
            [7, 5, 6, 9, 3, 2, 4, 1, 8],
            [1, 8, 3, 5, 7, 4, 2, 9, 6],
            [8, 4, 7, 6, 5, 3, 9, 2, 1],
            [9, 3, 2, 8, 4, 1, 6, 7, 5],
            [5, 6, 1, 2, 9, 7, 3, 8, 4],
            [3, 7, 8, 4, 2, 5, 1, 6, 9],
            [6, 1, 5, 3, 8, 9, 7, 4, 2],
            [2, 9, 4, 7, 1, 6, 8, 5, 3]]
sudoku = GRID(s1)
#print(sudoku.answers_dict)

Solve_sudoku(sudoku)


print(f'\nSolve: {sudoku.solve}\nUpdate: {sudoku.update}\nEasy: {sudoku.easy}\nHard: {sudoku.hard}')

if sudoku.grid == solution:
  print()
  print('SOLVED!')
else:
  print()
  print('WRONG!')

if sudoku.answers_dict:
  print()
  print('Cannot be solved without guessing!')
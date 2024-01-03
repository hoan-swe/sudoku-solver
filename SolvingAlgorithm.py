from ValidCheck import *

def Solve_sudoku(GRID):
  #Update_possible_answers(GRID)
  check = True
  while(check):
    check = Solve_sudoku_easy(GRID)
  GRID.solve += 1
  #if GRID.unsolved_dict.keys() != []:
    #Solve_sudoku_hard(GRID)
  

def Update_possible_answers(GRID):
  for position in GRID.unsolved_dict:
    poss_nums = GRID.nums - set(GRID.grid[position[0]])
    for num in poss_nums.copy():
      if Is_in_col(GRID.grid, position[1], num) or Is_in_box(GRID.grid, position[0] - position[0]%3, position[1] - position[1]%3, num):
        poss_nums.remove(num)
    GRID.unsolved_dict[position] = poss_nums
  #print(GRID.unsolved_dict)
  GRID.update += 1

def Solve_sudoku_easy(GRID):
  is_obvious = False
  for position in GRID.unsolved_dict.copy():
    if len(GRID.unsolved_dict[position]) == 1:
      row = position[0]
      col = position[1]
      GRID.grid[row][col] = list(GRID.unsolved_dict[position])[0]

      #print(position)
      GRID.unsolved_dict.pop(position)
      
      is_obvious = True

  Update_possible_answers(GRID)
  GRID.easy += 1
  return is_obvious

def Solve_sudoku_hard(GRID):
  for position in GRID.unsolved_dict:
    GRID.grid[position[0],position[1]] = list(GRID.unsolved_dict[position])[0]
    Solve_sudoku(GRID)
  
  GRID.hard += 1


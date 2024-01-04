from ValidCheck import *


# Main function.
def Solve_sudoku(GRID):
  '''
  Calling easy funtion until there are no more empty fields with an obvious answer.
  '''
  check = True
  while(check):
    check = Solve_sudoku_easy(GRID)
  GRID.solve += 1
  
# Update the dictionary containing possible answers of the remaining fields.
def Update_possible_answers(GRID):
  '''
  For each empty field, get a set of numbers that haven't been used in that row.
  Then check each number in that set if it has been used in that field's column or box.
  Remove the number for the set if it has been used.
  Assign the resulting set as value to the empty field.
  '''
  for position in GRID.answers_dict:
    poss_nums = GRID.nums - set(GRID.grid[position[0]])
    for num in poss_nums.copy():
      if Is_in_col(GRID.grid, position[1], num) or Is_in_box(GRID.grid, position[0] - position[0]%3, position[1] - position[1]%3, num):
        poss_nums.remove(num)
    GRID.answers_dict[position] = poss_nums
  #print(GRID.answers_dict)
  GRID.update += 1

# Fill all empty fields that have an obvious answer (only 1 possible answer).
def Solve_sudoku_easy(GRID):
  '''
  For each empty field, check its possible answers set.
  If there is only 1 possible answer (1 element in the set), fill the field with that number.
  Remove the field from the answers dictionary.
  Set a boolean variable to TRUE (meaning there is at least 1 field that has been solved/updated),
  or FALSE if there is no empty field with an abvious answer.
  Call the answers dictionary update function to remove the used number above from all answer sets.
  Return the boolean variable.
  '''
  is_obvious = False
  for position in GRID.answers_dict.copy():
    if len(GRID.answers_dict[position]) == 1:
      row = position[0]
      col = position[1]
      GRID.grid[row][col] = list(GRID.answers_dict[position])[0]

      #print(position)
      GRID.answers_dict.pop(position)
      is_obvious = True

  Update_possible_answers(GRID)
  GRID.easy += 1
  return is_obvious

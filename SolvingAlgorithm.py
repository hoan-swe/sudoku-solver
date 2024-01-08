from ValidCheck import Is_used


# Main function.
def Solve_sudoku(GRID):
  GRID.solve += 1
  Solve_sudoku_easy(GRID)
  
  print()
  print('Easy:')
  for i in range(9):
    print(GRID.grid[i])
  
  if GRID.answers_dict:  # Empty dictionary yields FALSE
    Solve_sudoku_hard(GRID)
  
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
      if Is_used(GRID.grid, position[0], position[1], num):
        poss_nums.remove(num)
    GRID.answers_dict.update({position : poss_nums})

  GRID.update += 1

# Fill all empty fields that have an obvious answer (only 1 possible answer).
def Solve_sudoku_easy(GRID):
  '''
  For each empty field, check its possible answers set.
  If there is only 1 possible answer (1 element in the set), fill the field with that number.
  Remove the field from the answers dictionary.
  Call the answers dictionary update function to remove the used number above from all answer sets.
  Repeat until there is no change in the answers dictionary.
  '''
  used = []
  temp = {}
  while (temp != GRID.answers_dict):
    used.clear()
    temp = GRID.answers_dict.copy()
    for position in GRID.answers_dict:
      if len(GRID.answers_dict[position]) == 1:        
        GRID.grid[position[0]][position[1]] = list(GRID.answers_dict[position])[0]
        used.append(position)        

    for position in used:
      GRID.answers_dict.pop(position)
    
    Update_possible_answers(GRID)
    
    GRID.easy += 1
    
# Solve remaining fields that have more than 1 possible answers.
def Solve_sudoku_hard(GRID):
  '''
  For each row, compare all empty fields and their possible answers in that row to each other.
  If there is a number that can be filled in only 1 empty field,
  fill that number, and update the answers dictionary.
  Do the same for columns, and then 3x3 boxes.
  '''
  GRID.hard += 1
  positions = []  # A list to store empty fields in a particular row, column, or box.
  temp = GRID.answers_dict.copy()  # A copy of answers dictionary before a operation.
  save = []  # A list to store visited fields
  nums = set()  # A set to store current row's, column's, or box's answers.
  
  # Row check
  GRID.row += 1

  '''
  For each row (1 - 9), clear and update the nums set,
  and add all empty fields' coordinate of that row to position list.
  If there is no empty field in the row (position list is empty), skip to next row.
  Else, run a check on the row.
  '''
  for row in range(9):
    positions.clear()
    nums.clear()
    for pair in GRID.answers_dict:
      if pair[0] == row:
        positions.append(pair)
        nums = nums|GRID.answers_dict[pair]
    if not positions:  # If position list is empty.
      continue

    '''
    For each number in a particular row's answer set,
    check and see if that number can be fit in more than 1 field.
    If not, fill the field that can hold the number.
    '''
    #Is_valid(GRID, nums, save, positions)
    for num in nums:
      save.clear()
      for pos in positions:
        if num in GRID.answers_dict[pos]:
          save.append(pos)

      if len(save) == 1:
        GRID.grid[save[0][0]][save[0][1]] = num
        GRID.answers_dict.pop(save[0])
        positions.remove(save[0])
  
  Update_possible_answers(GRID)

  print()
  print('Row check:')
  for i in range(9):
    print(GRID.grid[i])

  '''
  If the answers dictionaries before and after the check operation above are different,
  then it means there are fields that were solved.
  If so, re-run easy function to solve for new obvious fields.
  '''
  if temp != GRID.answers_dict:
    Solve_sudoku_easy(GRID)
  '''If answers dictionary is empty (means the puzzle is solved), return.'''
  if not GRID.answers_dict:
    return
  
  # Column check
  '''
  Clear all sets and lists, apply the same process from above to columns
  '''
  temp = GRID.answers_dict.copy()
  
  GRID.col += 1
  
  for col in range(9):
    positions.clear()
    nums.clear()
    for pair in GRID.answers_dict:
      if pair[1] == col:
        positions.append(pair)
        nums = nums|GRID.answers_dict[pair]
    if not positions:
      continue

    for num in nums:
      save.clear()
      for pos in positions:
        if num in GRID.answers_dict[pos]:
          save.append(pos)

      if len(save) == 1:
        GRID.grid[save[0][0]][save[0][1]] = num
        GRID.answers_dict.pop(save[0])
        positions.remove(save[0])
    
  Update_possible_answers(GRID)

  print()
  print('Column check:')
  for i in range(9):
    print(GRID.grid[i])

  if temp != GRID.answers_dict:
    Solve_sudoku_easy(GRID)
  if not GRID.answers_dict:
    return
  
  # Box check
  '''
  Clear all sets and lists, apply the same process from above to 3x3 boxes
  '''
  temp = GRID.answers_dict.copy()

  GRID.box += 1

  for row in range(0, 9, 3):
    for col in range(0, 9, 3):
      positions.clear()
      nums.clear()
      for pair in GRID.answers_dict:
        if row <= pair[0] < row + 3 and col <= pair[1] < col + 3:
          positions.append(pair)
          nums = nums|GRID.answers_dict[pair]
      if not positions:
        continue
      
      for num in nums:
        save.clear()
        for pos in positions:
          if num in GRID.answers_dict[pos]:
            save.append(pos)

        if len(save) == 1:
          GRID.grid[save[0][0]][save[0][1]] = num
          GRID.answers_dict.pop(save[0])
          positions.remove(save[0])

  Update_possible_answers(GRID)

  print()
  print('Box check:')
  for i in range(9):
    print(GRID.grid[i])

  '''
  Recall main function and start over in there are fields were solved.
  '''
  if temp != GRID.answers_dict:
    Solve_sudoku(GRID)
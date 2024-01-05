from ValidCheck import *


# Main function.
def Solve_sudoku(GRID):
  '''
  Calling easy funtion until there are no more empty fields with an obvious answer.
  '''
  #print('main')
  #print(len(GRID.answers_dict.keys()))

  Solve_sudoku_easy(GRID)
  
  print()
  print('Easy:')
  for i in range(9):
    print(GRID.grid[i])

  GRID.solve += 1
  
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
  Set a boolean variable to TRUE (meaning there is at least 1 field that has been solved/updated),
  or FALSE if there is no empty field with an abvious answer.
  Call the answers dictionary update function to remove the used number above from all answer sets.
  Return the boolean variable.
  '''
  used = []
  temp = {}
  while (temp != GRID.answers_dict):
    temp.clear()
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
  positions, answers = [], []
  temp = GRID.answers_dict.copy()
  
  # Row check 
  for row in range(9):
    positions.clear()
    answers.clear()
    used_num = set()
    check = False
    
    for pair in GRID.answers_dict:
      if pair[0] == row:
        positions.append(pair)
        answers.append(GRID.answers_dict[pair])
    if not positions:
      continue

    for i in range(len(answers)):
      for num in answers[i]:
        for j in range(i+1, len(answers)):
          if num not in answers[j]:
            continue
          else:
            check = False
            used_num.add(num)
            break
        check = True
        if check and num not in used_num:
          GRID.grid[positions[i][0]][positions[i][1]] = num
          del GRID.answers_dict[positions[i]]
          used_num.add(num)
          check = False
          break
  Update_possible_answers(GRID)

  print()
  print('Row check:')
  for i in range(9):
    print(GRID.grid[i])

  if temp != GRID.answers_dict:
    Solve_sudoku(GRID)  
  
  # Column check
  if not GRID.answers_dict:
    GRID.hard += 1
    return
  temp.clear()
  temp = GRID.answers_dict.copy()
  for col in range(9):
    positions.clear()
    answers.clear()
    check = False
    used_num.clear()
    for pair in GRID.answers_dict:
      if pair[1] == col:
        positions.append(pair)
        answers.append(GRID.answers_dict[pair])
    if not positions:
      continue

    for i in range(len(answers)):
      for num in answers[i]:
        for j in range(i+1, len(answers)):
          if num not in answers[j]:
            continue
          else:
            check = False
            used_num.add(num)
            break
        check = True
        if check and num not in used_num:
          GRID.grid[positions[i][0]][positions[i][1]] = num
          GRID.answers_dict.pop(positions[i])
          used_num.add(num)
          check = False
          break
  Update_possible_answers(GRID)

  print()
  print('Column check:')
  for i in range(9):
    print(GRID.grid[i])

  if temp != GRID.answers_dict:
    Solve_sudoku(GRID)
  
  # Box check
  else:
    if not GRID.answers_dict:
      GRID.hard += 1
      return
    temp.clear()
    temp = GRID.answers_dict.copy()
    for row in range(0, 9, 3):
      for col in range(0, 9, 3):
        positions.clear()
        answers.clear()
        check = False
        used_num.clear()
        for pair in GRID.answers_dict:
          if row <= pair[0] < row + 3 and col <= pair[1] < col + 3:
            positions.append(pair)
            answers.append(GRID.answers_dict[pair])
        
        for i in range(len(answers)):
          for num in answers[i]:
            for j in range(i+1, len(answers)):
              if num not in answers[j]:
                check = True
                continue
              else:
                check = False
                used_num.add(num)
                break
              
          if check and num not in used_num:
            GRID.grid[positions[i][0]][positions[i][1]] = num
            GRID.answers_dict.pop(positions[i])
            used_num.add(num)
            check = False
            break
    Update_possible_answers(GRID)
    if temp != GRID.answers_dict:
      Solve_sudoku(GRID)

    print()
    print('Box check:')
    for i in range(9):
      print(GRID.grid[i])
    
  GRID.hard += 1

def Is_used(grid, row, col, num):
  if any(grid[i][col] == num for i in range(9)):
    return True
  else:
    row = row - row%3
    col = col - col%3
    for i in range(3):
      for j in range(3):
        if(grid[i + row][j + col] == num):
          return True
    return False

'''def Is_valid(GRID, nums, save, positions):
  for num in nums:
    save.clear()
    for pos in positions:
      if num in GRID.answers_dict[pos]:
        save.append(pos)

    if len(save) == 1:
      GRID.grid[save[0][0]][save[0][1]] = num
      GRID.answers_dict.pop(save[0])
      positions.remove(save[0])'''
# Returns a boolean which indicates 
# whether any assigned entry
# in the specified row matches 
# the given number.
'''def Is_in_row(grid, row, num):
  return any(grid[row][i] == num for i in range(9))'''

# Returns a boolean which indicates 
# whether any assigned entry
# in the specified column matches 
# the given number.
'''def Is_in_col(grid, col, num):
  return any(grid[i][col] == num for i in range(9))'''

# Returns a boolean which indicates 
# whether any assigned entry
# within the specified 3x3 box 
# matches the given number
'''def Is_in_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if(grid[i + row][j + col] == num):
                return True
    return False'''


def Is_used(grid, row, col, num):
  if any(grid[row][i] == num for i in range(9)) or any(grid[i][col] == num for i in range(9)):
    return True
  else:
    row = row - row%3
    col = col - col%3
    for i in range(3):
      for j in range(3):
        if(grid[i + row][j + col] == num):
          return True
    return False
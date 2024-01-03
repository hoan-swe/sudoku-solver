from ValidCheck import *

class GRID:
    def __init__(self, grid):
      self.grid = grid
      self.unsolved_dict = {}
      self.nums = {1,2,3,4,5,6,7,8,9}
      self.solve, self.update, self.easy, self.hard = 0,0,0,0

      for row in range(9):
        for col in range(9):
          if self.grid[row][col] == 0:
            poss_nums = self.nums - set(self.grid[row])
            for num in poss_nums.copy():
              if Is_in_col(self.grid, col, num) or Is_in_box(self.grid, row - row%3, col - col%3, num):
                poss_nums.remove(num)
            self.unsolved_dict[(row, col)] = poss_nums
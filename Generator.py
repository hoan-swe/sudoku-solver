from ValidCheck import Is_used


class GRID:
    def __init__(self, grid):
      self.grid = grid
      self.answers_dict = {}
      self.nums = {1,2,3,4,5,6,7,8,9}
      self.solve, self.update, self.easy, self.hard = 0,0,0,0
      self.row, self.col, self.box = 0, 0, 0
      
      for row in range(9):
        for col in range(9):
          if self.grid[row][col] == 0:
            poss_nums = self.nums - set(self.grid[row])
            for num in poss_nums.copy():
              if Is_used(self.grid, row, col, num):
                poss_nums.remove(num)
            self.answers_dict[(row, col)] = poss_nums
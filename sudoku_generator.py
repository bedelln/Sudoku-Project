import random
import pygame

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=40):
        self.row_length = row_length
        self.board = [[0] * row_length for _ in range(row_length)]
        self.removed_cells = removed_cells

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))

    def fill_box(self, row_start, col_start):
        nums = list(range(1, 10))
        random.shuffle(nums)
        i = 0
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                self.board[r][c] = nums[i]
                i += 1

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self):
        for row in range(self.row_length):
            for col in range(self.row_length):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.fill_remaining():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining()

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1

def generate_sudoku(size, removed):
    generator = SudokuGenerator(size, removed)
    generator.fill_values()
    generator.remove_cells()
    return generator.get_board()

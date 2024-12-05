import math,random
import pygame

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length=9, removed_cells=40):
        self.row_length = row_length
        self.board = [[0] * row_length for _ in range(row_length)]
        self.removed_cells = removed_cells


    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for i, row in enumerate(self.board):
            if i != 0: #no separator for first row
                if i % 3 == 0:
                    print("-" * 23) #draw line separator

            row_r = ""
            for j, number in enumerate(row):
                if j != 0: #no separator for first column
                    if j % 3 == 0:
                        row_r += " |" #draw vertical separator with space
                    else:
                        row_r += f" {number}" #draw number with space
            print(row_r)
    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for r in range(9):
            if self.board[r][int(col)] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        for r in range(3):
            for c in range(3):
                if self.board[int(r + row_start)][int(c + col_start)] == num:
                    return False
        return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and self.valid_in_col(col, num)) and (self.valid_in_box(row / 3, col / 3, num))

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        num_list = random.sample(range(1, 10), 9)
        for num in num_list:
            for r in range(0, 3):
                for c in range(0, 3):
                    if self.valid_in_box(row_start, col_start, num):
                        self.board[r + row_start][c + col_start] = num

    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        x = 0
        while x < self.removed_cells:
            random1 = random.randint(0, 8)
            random2 = random.randint(0, 8)
            if self.board[random1][random2] != "_":
                self.board[random1][random2] = "_"
                x += 1

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(width, height, difficulty):
    sudoku = Board(width, height, difficulty)
    sudoku.fill_values()
    solved_board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class Cell:
   def __init__(self, value, row, col, screen):
       self.value = value
       self.row = row
       self.col = col
       self.sketched_value = None
       self.screen = screen
       self.selected = False

   def set_cell_value(self, value):
       self.value = value

   def set_sketched_value(self, value):
       self.sketched_value = value

   def draw(self):
       if self.selected:
           color = "red"
       else:
           color = "black"
       pygame.draw.rect(self.screen, color, pygame.Rect((self.row + 1) * 81, (self.col + 1) * 81, 40, 40), 1)
       font = pygame.font.Font(None, 48)
       if self.value != 0:
           text = font.render(str(self.value), True, "black")
           self.screen.blit(text, (self.row * 81, self.col * 81))

   def __getitem__(self):
       return self

class Board(SudokuGenerator):
   def __init__(self, width, height, difficulty):
       self.width = float(width)
       self.height = float(height)
       if difficulty == "easy":
           removed_cells = 30
       elif difficulty == "medium":
           removed_cells = 40
       else:
           removed_cells = 50
       super().__init__(9, removed_cells)
       self.base_board = self.board
       self.screen = pygame.display.set_mode((self.width, self.height))
       self.screen.fill("blue")
       self.cells = []
       for r in range(9):
           for c in range(9):
               self.cells.append(Cell(0, r, c, self.screen))

   def draw(self):
       pygame.display.update()
       for cell in self.cells:
           cell.draw()

   def select(self, row, col):
       if self.click(row, col) is not None:
           for r in range(9):
               for c in range(9):
                   if self.cells[r][c].selected:
                       self.cells[r][c].selected = False
           self.cells[row][col].selected = True

   def click(self, row, col):
       if row <= 81 and col <= 81:
           return row, col
       return None

   def clear(self):
        for r in range(9):
           for c in range(9):
               self.cells[r][c].set_cell_value(0)

   def sketch(self, value):
       for r in range(9):
           for c in range(9):
               if self.cells[r][c].selected:
                   self.cells[r][c].set_sketched_value(value)

   def place_number(self):
       for r in range(9):
           for c in range(9):
               if self.cells[r][c].selected:
                   self.cells[r][c].set_cell_value(self.cells[r][c].value)

   def reset_to_original(self):
       for r in range(9):
           for c in range(9):
               self.cells[r][c].value = self.base_board[r][c]
               self.board[r][c] = self.base_board[r][c]

   def is_full(self):
       for r in range(9):
           for cell in self.cells[r]:
               if cell.value == 0:
                   return False
       return True

   def update_board(self):
       for r in range(9):
           for c in range(9):
               self.board[r][c] = self.cells[r][c].value

   def find_empty(self):
       for r in range(9):
           for c in range(9):
               if self.cells[r][c].value == 0:
                   return r, c

   def check_board(self, solved_board):
       for r in range(9):
           for c in range(9):
               if self.board[r][c] != solved_board[r][c]:
                   return False
       return True

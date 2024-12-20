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
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.board = [[0] * row_length for _ in range(row_length)]
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(self.row_length))
        self.solved = []


    '''
    Enters in the sketched value the user entered into the board
        
    Parameters: 
    selected_location is the intended location for the number
    selected_key is the key clicked by the user (will only be a number 1-9)
        
    Return: None
    '''
    def set_sketched_value(self, selected_location, selected_key = None):
        if selected_key == None:
            self.board[int(selected_location[0])][int(selected_location[1])] = 0
        else:
            self.board[int(selected_location[0])][int(selected_location[1])] = selected_key - pygame.K_0


    '''
    Similar function to set_sketched_value, sets the board value to the sketched value
    Only called when enter is pressed in sudoku.py
    
    Parameters:
    selected_location is the intended location for the number
    num is the number that will set in the board, already entered by the user
    
    Return: None
    '''
    def set_actual_value(self, selected_location, num):
        self.board[int(selected_location[0])][int(selected_location[1])] = num


    '''
    Resets the board to the original generated board before values were entered
    
    Parameters: 
    initial_board is the initial board generated when the difficulty was selected
    
    Return: None
    '''
    def reset_board(self, initial_board):
        for i in range(self.row_length):
            for j in range(self.row_length):
                self.board[i][j] = initial_board[i][j]


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
        for row in self.board:
            print(row)


    '''
            Determines if num is contained in the specified column (vertical) of the board
            If num is already in the specified col, return False. Otherwise, return True

            Parameters:
            col is the index of the column we are checking
            num is the value we are looking for in the column

            Return: boolean
        '''
    def valid_in_row(self, row, num):
        return num not in self.board[row]


    '''
        	Determines if num is contained in the specified column (vertical) of the board
            If num is already in the specified col, return False. Otherwise, return True

        	Parameters:
        	col is the index of the column we are checking
        	num is the value we are looking for in the column

        	Return: boolean
        '''
    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]


    '''
        Determines if it is valid to enter num at (row, col) in the board
        This is done by checking that num is unused in the appropriate, row, column, and box

    	Parameters:
    	row and col are the row index and col index of the cell to check in the board
    	num is the value to test if it is safe to enter in this cell

    	Return: boolean
        '''
    def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == num:
                    return False
        return True


    '''
        Fills the specified 3x3 box with values
        For each position, generates a random digit which has not yet been used in the box

    	Parameters:
    	row_start and col_start are the starting indices of the box to check
    	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

    	Return: None
        '''
    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))


    '''
        Fills the three boxes along the main diagonal of the board
        These are the boxes which start at (0,0), (3,3), and (6,6)

    	Parameters: None
    	Return: None
        '''
    def fill_diagonal(self):
        for start in range(0, 6, 3):
            for r in range(3):
                for c in range(3):
                    rand_num = random.randint(1, 10)
                    if self.valid_in_box(r // 3, c // 3, rand_num):
                        self.board[r + start][c + start] = rand_num


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


    def fill_box(self, row_start, col_start):
        nums = list(range(1, 10))
        random.shuffle(nums)
        i = 0
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                self.board[r][c] = nums[i]
                i += 1


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


    def fill_di(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)


    def fill_rest(self):
        for row in range(self.row_length):
            for col in range(self.row_length):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.fill_rest():
                                return True
                            self.board[row][col] = 0
                    return False
        return True


    def fill_board(self):
        self.fill_di()
        self.fill_rest()


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
        count = self.removed_cells
        while count > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1


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
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


def generate(size, removed):
    generator = SudokuGenerator(size, removed)
    generator.fill_board()
    generator.solved = [row[:] for row in generator.board]
    generator.remove_cells()
    return generator

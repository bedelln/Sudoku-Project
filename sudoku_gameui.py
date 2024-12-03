import pygame
import random 

def main():
    try:
        pygame.init()

        #screen dimensions 
        width, height = 600, 600 
        rows, cols, = 9, 9 
        cell_size = width // cols 
        
        #defining movable number & selected cell, so the user input for number
    

        #creating a screen 
        screen = pygame.display.set_mode((width, height))
        #caption 
        pygame.display.set_caption("Sudoku")

        # Drawing Grid 
        for i in range(rows + 1): 
            #thicker lines to seperate subgrids 
            if i % 3 == 0: 
                thickness = 3 
            else: 
                1 #is it one or pass?
            #horizontal lines
            pygame.draw.line(screen, "black", (0, i * cell_size), (width, i * cell_size), thickness)
            #vertical 
            pygame.draw.line(screen, "black", (i * cell_size, 0), (i * cell_size, height), thickness)


        #fill the grid, not sure how to fill it, need fucntion to generate specific set of "randomn" numbers, that make the game playable. 
        sodoku_puzzle = ...

        #function to display soduku numbers. 
        def draw_numbers(): 

        #handling user input 
        class UserInput: 
            selected_cell = None

            #updates selected_cell based on mouse click. 
            def select_cell(pos): #note to self/reminder: pos is a variable from pygame that allows us to retrieve position when handling mouse clicks.
                x, y = pos 
                col, row = x // cell_size, y // cell_size 
                selected_cell = (row, col)

            #highlights selected cell for user 
            def draw_selected_cell(): 
                if selected_cell = True:  
                    row, col = selected_cell 
                    #beloow (col...) represents tuple for position & rectangle size. double cell_size is the width & height of selected rectangle. 
                    pygame.draw.rect(screen, BLUE, (col * cell_size, row * cell_size, cell_size, cell_size), 3)

        #maine game loop 
        running = True
        while running:
            screen.fill("white")  # Clear screen
            draw_grid()
            draw_numbers()
            draw_selected_cell()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #closes on close button 
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN: #selects cell
                    select_cell(pygame.mouse.get_pos())

                elif event.type == pygame.KEYDOWN: #adds number to selected cell. keydown is when a key is pressed
                    if selected_cell = True and event.unicode.isdigit(): #event unicode is charachter reprisenttaon of what key was pressed + making sure key pressed is a digit. 
                        row, col = selected_cell
                        sudoku_puzzle[row][col] = int(event.unicode) #need to create a soduku puzzle. 

            pygame.display.flip()  # Update display



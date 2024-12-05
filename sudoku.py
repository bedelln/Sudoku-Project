import pygame
import sys
from sudoku_generator import generate_sudoku  

# UPDATE

pygame.init()

# Constants
WIDTH, HEIGHT = 700, 600
CELL_SIZE = WIDTH // 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRID_COLOR = (0, 0, 0)
FONT = pygame.font.SysFont("Arial", 32)
USER_INPUT_COLOR = (169, 169, 169)  # Gray color for user inputs
BUTTON_COLOR = (50, 150, 255)  # Blue for buttons
BUTTON_TEXT_COLOR = WHITE


# Function to draw grid, numbers, and buttons
def draw_board(screen, board, selected=None, user_inputs=None):
    if user_inputs is None:
        user_inputs = set()
        
    # Draw the grid and numbers
    for r in range(9):
        for c in range(9):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            # Highlight the selected cell
            if selected == (r, c):
                pygame.draw.rect(screen, RED, rect, 3)

            # Draw cell borders
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

            # Draw the numbers in the grid
            val = board[r][c]
            if val != 0:
                color = USER_INPUT_COLOR if (r, c) in user_inputs else GRID_COLOR
                text = FONT.render(str(val), True, color)
                screen.blit(text, (c * CELL_SIZE + CELL_SIZE // 3, r * CELL_SIZE + CELL_SIZE // 3))

    # Draw thicker lines for subgrid separation
    for i in range(1, 3):
        pygame.draw.line(screen, GRID_COLOR, (0, i * CELL_SIZE * 3), (WIDTH, i * CELL_SIZE * 3), 3)  # Horizontal lines
        pygame.draw.line(screen, GRID_COLOR, (i * CELL_SIZE * 3, 0), (i * CELL_SIZE * 3, HEIGHT), 3)  # Vertical lines

    # Draw buttons
    reset_button = pygame.Rect(20, HEIGHT + 10, 150, 50)
    restart_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT + 10, 150, 50)
    exit_button = pygame.Rect(WIDTH - 170, HEIGHT + 10, 150, 50)
    
    pygame.draw.rect(screen, BUTTON_COLOR, reset_button)
    pygame.draw.rect(screen, BUTTON_COLOR, restart_button)
    pygame.draw.rect(screen, BUTTON_COLOR, exit_button)

    # Draw button text
    button_font = pygame.font.SysFont(None, 24)
    reset_text = button_font.render("RESET", True, BUTTON_TEXT_COLOR)
    restart_text = button_font.render("RESTART", True, BUTTON_TEXT_COLOR)
    exit_text = button_font.render("EXIT", True, BUTTON_TEXT_COLOR)

    screen.blit(reset_text, (reset_button.x + (reset_button.width - reset_text.get_width()) // 2,
                             reset_button.y + (reset_button.height - reset_text.get_height()) // 2))
    screen.blit(restart_text, (restart_button.x + (restart_button.width - restart_text.get_width()) // 2,
                               restart_button.y + (restart_button.height - restart_text.get_height()) // 2))
    screen.blit(exit_text, (exit_button.x + (exit_button.width - exit_text.get_width()) // 2,
                            exit_button.y + (exit_button.height - exit_text.get_height()) // 2))

    return reset_button, restart_button, exit_button

def start_page(screen):
    # Buttons for selecting difficulty
    easy_button = pygame.Rect(50, 400, 150, 70)
    medium_button = pygame.Rect(210, 400, 150, 70)
    hard_button = pygame.Rect(370, 400, 150, 70)

    # Text for buttons
    font = pygame.font.SysFont(None, 50)
    easy_text = font.render("EASY", True, WHITE)
    medium_text = font.render("MEDIUM", True, WHITE)
    hard_text = font.render("HARD", True, WHITE)

    # Welcome text
    title_font = pygame.font.SysFont(None, 80)
    title_text = title_font.render("Welcome to Sudoku", True, BLACK)
    subtitle_font = pygame.font.SysFont(None, 50)
    subtitle_text = subtitle_font.render("Select Difficulty", True, BLACK)

    while True:
        screen.fill(WHITE)

        # Draw title and buttons
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(subtitle_text, (WIDTH // 2 - subtitle_text.get_width() // 2, 200))
        pygame.draw.rect(screen, BLUE, easy_button)
        pygame.draw.rect(screen, ORANGE, medium_button)
        pygame.draw.rect(screen, BLUE, hard_button)

        # Center button text
        screen.blit(easy_text, (easy_button.x + (easy_button.width - easy_text.get_width()) // 2, 
                                easy_button.y + (easy_button.height - easy_text.get_height()) // 2))
        screen.blit(medium_text, (medium_button.x + (medium_button.width - medium_text.get_width()) // 2, 
                                  medium_button.y + (medium_button.height - medium_text.get_height()) // 2))
        screen.blit(hard_text, (hard_button.x + (hard_button.width - hard_text.get_width()) // 2, 
                                hard_button.y + (hard_button.height - hard_text.get_height()) // 2))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return "easy"
                elif medium_button.collidepoint(event.pos):
                    return "medium"
                elif hard_button.collidepoint(event.pos):
                    return "hard"

        pygame.display.update()

def game_won_page(screen):
    # place exit button
    exit_button = pygame.Rect(300, 500, 210, 80)
    # draw text of buttons
    exit_font = pygame.font.SysFont(None, 50)
    exit_text = exit_font.render("EXIT", True, WHITE)
    won_font = pygame.font.Font(None, 120)
    won_text = won_font.render("Game Won!", True, BLACK)

    while True:
        # set screen color
        screen.fill(WHITE)
        # draw exit button
        pygame.draw.rect(screen, ORANGE, exit_button)
        # draw text
        screen.blit(won_text, (180, 260))
        # center exit text
        x_exit_text = exit_button.x + (exit_button.width - exit_text.get_width()) // 2
        y_exit_text = exit_button.y + (exit_button.height - exit_text.get_height()) // 2
        # draw start text
        screen.blit(exit_text, (x_exit_text, y_exit_text))
        # event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):  # check if the exit button was clicked
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def game_over_page(screen):
    # place restart button
    restart_button = pygame.Rect(300, 500, 210, 80)
    # draw text of buttons
    restart_font = pygame.font.SysFont(None, 50)
    restart_text = restart_font.render("RESTART", True, WHITE)
    game_over_font = pygame.font.Font(None, 120)
    game_over_text = game_over_font.render("Game Over :(", True, BLACK)

    while True:
        # set screen color
        screen.fill(WHITE)
        # draw exit button
        pygame.draw.rect(screen, ORANGE, restart_button)
        # draw text
        screen.blit(game_over_text, (145, 260))
        # center exit text
        x_exit_text = restart_button.x + (restart_button.width - restart_text.get_width()) // 2
        y_exit_text = restart_button.y + (restart_button.height - restart_text.get_height()) // 2
        # draw start text
        screen.blit(restart_text, (x_exit_text, y_exit_text))
        # event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):  # check if the restart button was clicked
                    return  # Go back to the main game

        pygame.display.update()


def main():
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 70))  # Adjust height for buttons
    pygame.display.set_caption("Sudoku Game")

    # Start page for difficulty selection
    difficulty = start_page(screen)

    # Map difficulties to pre-filled cell counts
    difficulty_map = {"easy": 30, "medium": 40, "hard": 50}
    removed_cells = difficulty_map[difficulty]

    # Generate Sudoku board
    board = generate_sudoku(9, removed_cells)
    selected = None
    user_inputs = set()

    while True:
        screen.fill(WHITE)
        reset_button, restart_button, exit_button = draw_board(screen, board, selected, user_inputs)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if reset_button.collidepoint(event.pos):
                    board = generate_sudoku(9, removed_cells)  # Reset the board
                    user_inputs.clear()
                elif restart_button.collidepoint(event.pos):
                    main()  # Restart the game
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

                # Handle user input
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE
                selected = (row, col)

            if event.type == pygame.KEYDOWN:
                if selected:
                    row, col = selected
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        board[row][col] = event.key - pygame.K_0

        pygame.display.update()

if __name__ == "__main__":
    main()

import pygame
import sys
pygame.font.init()

#set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 95, 0)

#set size of the page
WIDTH = 810
HEIGHT = 972
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def start_page(screen):
    #place mode buttons, set button width 200 and button height 70
    easy_button = pygame.Rect(100, 500, 200, 70)
    medium_button = pygame.Rect(310, 500, 200, 70)
    hard_button = pygame.Rect(520, 500, 200, 70)
    #draw text of buttons
    font = pygame.font.SysFont(None, 50)
    easy_text = font.render("EASY", True, WHITE)
    medium_text = font.render("MEDIUM", True, WHITE)
    hard_text = font.render("HARD", True, WHITE)

    welcome_font = pygame.font.Font(None, 80)
    welcome_text = welcome_font.render("Welcome to Sudoku", True, BLACK)
    selection_font = pygame.font.Font(None, 65)
    selection_text = selection_font.render("Select Game Mode:", True, BLACK)


    while True:
        #set screen color"
        screen.fill(WHITE)
        #draw text
        screen.blit(welcome_text, (140, 150))
        screen.blit(selection_text, (190, 300))
        #draw buttons
        pygame.draw.rect(screen, BLUE, easy_button)
        pygame.draw.rect(screen, ORANGE, medium_button)
        pygame.draw.rect(screen, BLUE, hard_button)
        #center text
        x_easy_text = easy_button.x + (easy_button.width - easy_text.get_width()) // 2
        y_easy_text = easy_button.y + (easy_button.height - easy_text.get_height()) // 2
        screen.blit(easy_text, (x_easy_text, y_easy_text))

        x_medium_text = medium_button.x + (medium_button.width - medium_text.get_width()) // 2
        y_medium_text = medium_button.y + (medium_button.height - medium_text.get_height()) // 2
        screen.blit(medium_text, (x_medium_text, y_medium_text))

        x_hard_text = hard_button.x + (hard_button.width - hard_text.get_width()) // 2
        y_hard_text = hard_button.y + (hard_button.height - hard_text.get_height()) // 2
        screen.blit(hard_text, (x_hard_text, y_hard_text))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return "easy mode"
                elif medium_button.collidepoint(event.pos):
                    return "medium mode"
                elif hard_button.collidepoint(event.pos):
                    return "hard mode"

        pygame.display.update()


def game_won_page(screen):
    #place exit button
    exit_button = pygame.Rect(300, 500, 210, 80)
    # draw text of buttons
    exit_font = pygame.font.SysFont(None, 50)
    exit_text = exit_font.render("EXIT", True, WHITE)
    won_font = pygame.font.Font(None, 120)
    won_text = won_font.render("Game Won!", True, BLACK)

    while True:
        #set screen color
        screen.fill(WHITE)
        #draw exit button
        pygame.draw.rect(screen, ORANGE, exit_button)
        # draw text
        screen.blit(won_text, (180, 260))
        #center exit text
        x_exit_text = exit_button.x + (exit_button.width - exit_text.get_width()) // 2
        y_exit_text = exit_button.y + (exit_button.height - exit_text.get_height()) // 2
        #draw start text
        screen.blit(exit_text, (x_exit_text, y_exit_text))
        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):  #check if the exit button was clicked
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def game_over_page(screen):
    #place restart button
    restart_button = pygame.Rect(300, 500, 210, 80)
    # draw text of buttons
    restart_font = pygame.font.SysFont(None, 50)
    restart_text = restart_font.render("RESTART", True, WHITE)
    game_over_font = pygame.font.Font(None, 120)
    game_over_text = game_over_font.render("Game Over :(", True, BLACK)

    while True:
        #set screen color
        screen.fill(WHITE)
        #draw exit button
        pygame.draw.rect(screen, ORANGE, restart_button)
        # draw text
        screen.blit(game_over_text, (145, 260))
        #center exit text
        x_exit_text = restart_button.x + (restart_button.width - restart_text.get_width()) // 2
        y_exit_text = restart_button.y + (restart_button.height - restart_text.get_height()) // 2
        #draw start text
        screen.blit(restart_text, (x_exit_text, y_exit_text))
        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):  #check if the restart button was clicked
                    pygame.quit()
                    sys.exit()
        pygame.display.update()



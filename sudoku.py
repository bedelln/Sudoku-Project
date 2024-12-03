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
    easy_button = pygame.Rect(100, 550, 200, 70)
    medium_button = pygame.Rect(310, 550, 200, 70)
    hard_button = pygame.Rect(520, 550, 200, 70)
    #draw text of buttons
    font = pygame.font.SysFont(None, 50)
    easy_text = font.render("EASY", True, WHITE)
    medium_text = font.render("MEDIUM", True, WHITE)
    hard_text = font.render("HARD", True, WHITE)
    while True:
        #set screen color
        screen.fill(WHITE)
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
if __name__ == "__main__":
    selected_mode = start_page(screen)
    print(f"Selected Mode: {selected_mode}")

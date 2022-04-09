from unicodedata import name
import pygame
from GUI.gui_constants import *
from GUI.game import main as game_main


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")


button_with_heuristic = pygame.Rect(94,324,BUTTON_WIDTH, BUTTON_HEIGHT)
button_without_heuristic = pygame.Rect(491,324,BUTTON_WIDTH, BUTTON_HEIGHT)

def draw_window():
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    text = CONNECT_FOUR_FONT.render("Connect Four", 1, BLACK)

    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 100))

    pygame.draw.rect(WIN, RED, button_with_heuristic)
    pygame.draw.rect(WIN, BLUE, button_without_heuristic)

    text_with_heuristic = START_FONT.render("Play With Pruning", 1, WHITE)
    text_without_heuristic = START_FONT.render("Play Without Pruning", 1, WHITE)
    WIN.blit(text_with_heuristic, (button_with_heuristic.x + button_with_heuristic.width/2 - text_with_heuristic.get_width()/2, button_with_heuristic.y + button_with_heuristic.height/2 - text_with_heuristic.get_height()/2))
    WIN.blit(text_without_heuristic, (button_without_heuristic.x + button_without_heuristic.width/2 - text_without_heuristic.get_width()/2, button_without_heuristic.y + button_without_heuristic.height/2 - text_without_heuristic.get_height()/2))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_with_heuristic.collidepoint(pygame.mouse.get_pos()):
                    game_main(True)
                elif button_without_heuristic.collidepoint(pygame.mouse.get_pos()):
                    game_main(False)
        
        draw_window()

if __name__ == "__main__":
    main()
import pygame
import gui

pygame.font.init()
WIN = pygame.display.set_mode((gui.WIDTH, gui.HEIGHT))

CONNECT_FOUR_FONT = pygame.font.SysFont("comicsans", 70)

CELL_WIDTH, CELL_HEIGHT = 60, 60

turn = 0

cells = []
current_state = []
for i in range(7):
    current_state.append([])
    for j in range(6):
        current_state[i].append('0')

def draw_window():
    WIN.blit(gui.BACKGROUND_IMAGE, (0, 0))
    text = CONNECT_FOUR_FONT.render("Connect Four", 1, gui.BLACK)
    WIN.blit(text, (gui.WIDTH/2 - text.get_width()/2, 20))
    for i in range(7):
        cells.append([])
        for j in range(6):
            cell_border = pygame.Rect(180 + (i+1)*CELL_WIDTH, 530 - (j+1)*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(WIN, gui.BLACK, cell_border )
            cell = pygame.Rect(cell_border.x + 1, cell_border.y + 1, CELL_WIDTH - 2, CELL_HEIGHT - 2)
            pygame.draw.rect(WIN, gui.WHITE, cell )
            cells[i].append(cell)
    

    pygame.display.update()



def main(WithHeuristic: bool):
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(gui.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(7):
                    for j in range(6):
                        if cells[i][j].collidepoint(pygame.mouse.get_pos()):
                            print("column:", i)
        draw_window()

if __name__ == "__main__":
    main()
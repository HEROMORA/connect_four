import pygame
from GUI.gui import *
from models.node_type import NodeType
from models.pruning import Pruning
from minimaxAlgorithm import decide
from models.state import State
from scoreCalculation import count_fours

import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

pygame.font.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

CONNECT_FOUR_FONT = pygame.font.SysFont("comicsans", 70)

CELL_WIDTH, CELL_HEIGHT = 60, 60

cells = []
current_state = []
for i in range(7):
    current_state.append([])
    for j in range(6):
        current_state[i].append('0')

def draw_window(current_column: int, current_player_color:tuple, sequence:str, isFull:bool):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    text = CONNECT_FOUR_FONT.render("Connect Four", 1, BLACK)
    red_four_count = count_fours(sequence, 'r')
    blue_four_count = count_fours(sequence, 'b')
    red_score = SCORE_FONT.render(f"AI agent: {red_four_count}", 1, BLACK)
    blue_score = SCORE_FONT.render(f"You: {blue_four_count}", 1, BLACK)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    for i in range(7):
        cells.append([])
        k = 0
        for j in range(6):
            cell_border = pygame.Rect(180 + (i+1)*CELL_WIDTH, 530 - (j+1)*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(WIN, BLACK, cell_border )
            cell = pygame.Rect(cell_border.x + 1, cell_border.y + 1, CELL_WIDTH - 2, CELL_HEIGHT - 2)
            pygame.draw.rect(WIN, WHITE, cell )
            if sequence[k+i] == 'r':
                pygame.draw.circle(WIN, RED, (cell.x + CELL_WIDTH/2, cell.y + CELL_HEIGHT/2), CELL_HEIGHT/2-10)
            elif sequence[k+i] == 'b':
                pygame.draw.circle(WIN, BLUE, (cell.x + CELL_WIDTH/2, cell.y + CELL_HEIGHT/2), CELL_HEIGHT/2-10)
            cells[i].append(cell)
            k+=7
    
    if(current_column != -1):
        pygame.draw.circle(WIN, current_player_color, (cells[current_column][5].x + CELL_WIDTH/2, cell.y + CELL_HEIGHT/2), CELL_HEIGHT/2-10)

    WIN.blit(red_score, (10, 10))
    WIN.blit(blue_score, (WIDTH - blue_score.get_width() - 10, 10))
    if isFull:
        if(red_four_count > blue_four_count):
            text = CONNECT_FOUR_FONT.render("AI agent wins!", 1, BLACK)
        elif(red_four_count < blue_four_count):
            text = CONNECT_FOUR_FONT.render("You win!", 1, BLACK)
        else:
            text = CONNECT_FOUR_FONT.render("Draw!", 1, BLACK)

        WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()

def handle_hover(mouse_pos):
    if(len(cells) == 0):
        return -1
    current_column = -1
    for i in range(7):
        for j in range(6):
            if cells[i][j].collidepoint(mouse_pos):
                current_column = i
                break
        if current_column != -1:
            break
    return current_column


def main(WithHeuristic: bool):
    num_levels = simpledialog.askinteger("Number of levels", "Enter the number of levels you want to traverse to:")
    run = True
    clock = pygame.time.Clock()
    filled_cells = "0"*7*6
    turn = False
    isFull = False
    while run:
        clock.tick(FPS)
        if(turn):
            curr_state = State(filled_cells, NodeType.max)
            returned_state = decide(curr_state, num_levels, WithHeuristic, 'r')
            filled_cells = returned_state.sequence
            if(returned_state.is_full_board()):
                isFull = True
            turn = not turn
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(7):
                    for j in range(6):
                        if cells[i][j].collidepoint(pygame.mouse.get_pos()):
                            child = filled_cells[i::7]
                            if '0' not in child:
                                continue
                            index = child.index('0')*7 + i
                            char = 'r' if turn else 'b'
                            filled_cells = filled_cells[:index] + char + filled_cells[index+1:]
                            turn = not turn

        current_column = handle_hover(pygame.mouse.get_pos())
        color = RED if turn else BLUE
        draw_window(current_column,color, filled_cells, isFull)

if __name__ == "__main__":
    main()
import pygame
import sys
from ai import ai

from script import *

#initializing the pygame window and game variables
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Checkers')
red_translucent = pygame.image.load("assets/red_translucent.png")
black_translucent = pygame.image.load("assets/black_translucent.png")
clock = pygame.time.Clock()

#main loop
game_over = False
is_black = True
ai1 = ai(is_black)
print(get_piece(ai1.is_black))
player_piece_value = get_piece(is_black)
board = make_board(is_black)
player_turn = True
running = True
moving = False
indexes = []
moving_indexes = []
place_holder = 0
draw_board(board, gameDisplay)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not player_turn and not game_over:
            pygame.time.wait(600)
            board = ai1.next_move(board)
            draw_board(board, gameDisplay)
            pygame.display.update()
            player_turn = True

        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and not moving and player_turn:
            x,y = pygame.mouse.get_pos()
            indexes = where_clicked(board,x,y)
            if board[indexes[0]][indexes[1]]==1 and not is_black:
                place_holder = board[indexes[0]][indexes[1]]
                board[indexes[0]][indexes[1]]=0
                draw_board(board, gameDisplay)
                moving = True
            if board[indexes[0]][indexes[1]]==2 and is_black:
                place_holder = board[indexes[0]][indexes[1]]
                board[indexes[0]][indexes[1]]=0
                draw_board(board, gameDisplay)
                moving = True

        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and moving and player_turn:
            x,y = pygame.mouse.get_pos()
            moving_indexes = where_clicked(board,x,y)
            valid = valid_move(board,indexes,moving_indexes,player_piece_value)
            if type(valid)!=bool:
                    board[moving_indexes[0]][moving_indexes[1]]=place_holder
                    place_holder = 0
                    jumping_indexes = valid[1]
                    board[jumping_indexes[0]][jumping_indexes[1]]=0
                    draw_board(board, gameDisplay)
                    pygame.display.update()
                    moving = False
                    player_turn = False
            else:
                if valid:
                    board[moving_indexes[0]][moving_indexes[1]]=place_holder
                    place_holder = 0
                    draw_board(board, gameDisplay)
                    pygame.display.update()
                    moving = False
                    player_turn = False
                else:
                    board[indexes[0]][indexes[1]]=place_holder
                    draw_board(board, gameDisplay)
                    pygame.display.update()
                    moving = False

    if moving == True:
        x,y = pygame.mouse.get_pos()
        draw_board(board, gameDisplay)
        if place_holder == 1: gameDisplay.blit(red_translucent, tuple(map(lambda x: x-50,pygame.mouse.get_pos())))
        else: gameDisplay.blit(black_translucent, tuple(map(lambda x: x-50,pygame.mouse.get_pos())))
        clock.tick(60)
        pygame.display.update()
#end of main loop

pygame.display.quit()
pygame.quit()
sys.exit()

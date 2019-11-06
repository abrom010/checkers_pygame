#Checkers game
import pygame

boardImage = pygame.image.load("assets/board.png")
red = pygame.image.load("assets/red.png")
black = pygame.image.load("assets/black.png")

coordinates =  (((0, 0), (100, 0), (200, 0), (300, 0), (400, 0), (500, 0), (600, 0), (700, 0)),
                ((0, 100), (100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100)),
                ((0, 200), (100, 200), (200, 200), (300, 200), (400, 200), (500, 200), (600, 200), (700, 200)),
                ((0, 300), (100, 300), (200, 300), (300, 300), (400, 300), (500, 300), (600, 300), (700, 300)),
                ((0, 400), (100, 400), (200, 400), (300, 400), (400, 400), (500, 400), (600, 400), (700, 400)),
                ((0, 500), (100, 500), (200, 500), (300, 500), (400, 500), (500, 500), (600, 500), (700, 500)),
                ((0, 600), (100, 600), (200, 600), (300, 600), (400, 600), (500, 600), (600, 600), (700, 600)),
                ((0, 700), (100, 700), (200, 700), (300, 700), (400, 700), (500, 700), (600, 700), (700, 700)))

def get_piece(is_black):
    switcher = {
        True: 2,
        False: 1
    }
    return switcher.get(is_black)

def make_board(is_black=True):
    if is_black:
        return ([0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0])
    if not is_black:
        return ([0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0])


def draw_board(board, gameDisplay):
    gameDisplay.blit(boardImage, [0, 0])
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                gameDisplay.blit(red, coordinates[i][j])
            elif board[i][j] == 2:
                gameDisplay.blit(black, coordinates[i][j])

def where_clicked(board, x, y):
    x = x-(x%100)
    y = y-(y%100)
    position = (x,y)
    for row in coordinates:
        for entry in row:
            if entry == position:
                i=coordinates.index(row)
                j=row.index(entry)
    return i,j

def valid_move(board,indexes,moving_indexes,player_piece_value):
    jumping_indexes = []
    moving_square_value = board[moving_indexes[0]][moving_indexes[1]]
    if moving_square_value == 0:
        x_distance = moving_indexes[1] - indexes[1]
        y_distance = moving_indexes[0] - indexes[0]
        if y_distance == -2:
            if x_distance==2:
                jumping_indexes = [indexes[0]-1,indexes[1]+1]
                jumping_square_value = board[jumping_indexes[0]][jumping_indexes[1]]
            elif x_distance==-2:
                jumping_indexes = [indexes[0]-1,indexes[1]-1]
                jumping_square_value = board[jumping_indexes[0]][jumping_indexes[1]]
            else:
                return False
            if jumping_square_value!=0 and\
               jumping_square_value!=player_piece_value:
                return (True,jumping_indexes)
        elif y_distance == -1:
            if x_distance == 1 or x_distance == -1:
                return True
    return False

if __name__ == "__main__":
    pass

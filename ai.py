from script import get_piece
class ai:
    is_black = None
    board = None
    piece_value = None
    def __init__(self,is_black):
        self.piece_value = get_piece(not is_black)
        self.is_black = is_black

    def next_move(self,board):
        self.board = board
        piece_value = self.piece_value

        def attack_right():
            for i in range(8):
                for j in range(8):
                    if i < 6 and j < 6:
                        if self.board[i][j] == piece_value and\
                        self.board[i+1][j+1] == get_piece(self.is_black) and\
                        self.board[i+2][j+2] == 0:
                            self.board[i+2][j+2] = piece_value
                            self.board[i+1][j+1] = 0
                            self.board[i][j] = 0
                            return self.board
            return None

        def attack_left():
            for i in range(8):
                for j in range(8):
                    if i < 6 and j > 2:
                        if self.board[i][j] == piece_value and\
                        self.board[i+1][j-1] == get_piece(self.is_black) and\
                        self.board[i+2][j-2] == 0:
                            self.board[i+2][j-2] = piece_value
                            self.board[i+1][j-1] = 0
                            self.board[i][j] = 0
                            return self.board
            return None

        def move_right_defense():
            for i in range(8):
                for j in range(8):
                    if i > 1 and j < 6:
                        if self.board[i][j] == piece_value and\
                        self.board[i-1][j+1] == 0 and\
                        self.board[i-2][j+2] == piece_value:
                            self.board[i-1][j+1] = piece_value
                            self.board[i-2][j+2] = 0
                            return self.board
            return None

        def move_left_defense():
            for i in range(8):
                for j in range(8):
                    if i < 6 and j < 6:
                        if self.board[i][j] == piece_value and\
                        self.board[i-1][j-1] == 0 and\
                        self.board[i-2][j-2] == piece_value:
                            self.board[i-1][j-1] = piece_value
                            self.board[i-2][j-2] = 0
                            return self.board
            return None

        def move_right_offense():
            for i in range(8):
                for j in range(8):
                    if i < 7 and j < 7:
                        if self.board[i][j] == piece_value and\
                        self.board[i+1][j+1] == 0:
                            self.board[i+1][j+1] = piece_value
                            self.board[i][j]=0
                            return self.board
            return None

        def move_left_offense():
            for i in range(8):
                for j in range(8):
                    if i < 7 and j > 0:
                        if self.board[i][j] == piece_value and\
                        self.board[i+1][j-1] == 0:
                            self.board[i+1][j-1] = piece_value
                            self.board[i][j]=0
                            return self.board
            return None

        from random import randint
        num = randint(0,1)
        if num == 0:
            board = attack_left()
            if board != None: return board
            board = attack_right()
            if board != None: return board
            board = move_left_defense()
            if board != None: return board
            board = move_right_defense()
            if board != None: return board
            board = move_left_offense()
            if board != None: return board
            board = move_right_offense()
            if board != None: return board
        else:
            board = attack_right()
            if board != None: return board
            board = attack_left()
            if board != None: return board
            board = move_right_defense()
            if board != None: return board
            board = move_left_defense()
            if board != None: return board
            board = move_right_offense()
            if board != None: return board
            board = move_left_offense()
            if board != None: return board

        return self.board

if __name__ == "__main__":
    pass

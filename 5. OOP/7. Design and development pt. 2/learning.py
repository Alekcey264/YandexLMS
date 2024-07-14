WHITE = 1
BLACK = 2

def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8

class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.set_figures()

    def set_figures(self):
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color
    
    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        if color == WHITE:
            c = 'w'
        else:
            c = 'b'
        return c + piece.char()
    
    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not self.field[row1][col1]:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].ger_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True
    
    def print_board(self):
        print('     +----+----+----+----+----+----+----+----+')
        for row in range(7, -1, -1):
            print(' ', row, end="  ")
            for col in range(8):
                print("|", self.cell(row, col), end=' ')
            print('|')
            print('     +----+----+----+----+----+----+----+----+')
        print(end='        ')
        for col in range(8):
            print(col, end='    ')
        print()

    
class Figure:
    def __init__(self, color):
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color


class Pawn(Figure):
    def char(self):
        return 'P'
    
    def can_move(self, board, row, col, row1, col1):
        if self.col != col:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if self.row + direction  == row:
            return True
        if self.row == start_row and row + 2 * direction == row1 and board.field[row + direction][col] is None:
            return True
        return False
    
    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if self.color == WHITE else -1
        return (row + direction == row1 and (col + 1 == col1 or col - 1 == col1))
    

class Rook(Figure):
    def char(self):
        return 'R'
        
    def can_move(self, board, row, col, row1, col1):
        if self.row != row and self.col != col:
            return False
        step = 1 if row1 >= row else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False
        step = 1 if col1 >= col else -1
        for r in range(col + step, col1, step):
            if not (board.get_piece(row, r) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Knight(Figure):
    def char(self):
        return 'N'
    
    def can_move(self, new_row, new_col):
        if abs(new_row - self.row) == 2 and abs(new_col - self.col) == 1:
            return True
        if abs(new_row - self.row) == 1 and abs(new_col - self.col) == 2:
            return True
        return False

class Bishop(Figure):
    def char(self):
        return 'B'
    
    def can_move(self, new_row, new_col):
        if abs(new_row - self.row) == abs(new_col - self.col):
            return True
        return False


class Queen(Figure):
    def char(self):
        return 'Q'
    
    def can_move(self, new_row, new_col):
        if abs(new_row - self.row) == abs(new_col - self.col):
            return True
        if new_col == self.col or new_row == self.row:
            return True
        return False
    

class King(Figure):
    def char(self):
        return 'K'
    
    def can_move(self, new_row, new_col):
        if abs(new_col - self.col) == 1 and abs(new_row - self.row) == 1:
            return True
        if new_col == self.col and abs(new_row - self.row) == 1:
            return True
        if new_row == self.row and abs(new_col - self.col) == 1:
            return True
        return False
        

def main():
    board = Board()
    while True:
        board.print_board()
        print('Commands:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        if board.current_player_color() == WHITE:
            print('Ход белых')
        else:
            print('Ход черных')
        command = input()
        if command == 'exit':
            break
        _, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Success')
        else:
            print('Impossible. Try again')

main()
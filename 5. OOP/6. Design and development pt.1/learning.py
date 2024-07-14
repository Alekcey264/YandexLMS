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
        self.field[1][4] = Pawn(1, 4, WHITE)

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
        if not piece.can_move(row1, col1):
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
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color



class Pawn(Figure):
    def char(self):
        return 'P'
    
    def can_move(self, row, col):
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
        if self.row == start_row and self.row + 2 * direction == row:
            return True
        return False
    

class Rook(Figure):
    def char(self):
        return 'R'
        
    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True


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
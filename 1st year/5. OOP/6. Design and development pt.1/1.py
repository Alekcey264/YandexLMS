class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def correct_coords(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color
    
    def char(self):
        return 'N'
    
    def can_move(self, new_row, new_col):
        if not self.correct_coords(new_row, new_col):
            return False
        if abs(new_row - self.row) == 2 and abs(new_col - self.col) == 1:
            return True
        if abs(new_row - self.row) == 1 and abs(new_col - self.col) == 2:
            return True
        return False
    
WHITE=1
BLACK=2

row0_W = 0
col0_W = 1
knight_W = Knight(row0_W, col0_W, WHITE)

row0_B = 7
col0_B = 6
knight_B = Knight(row0_B, col0_B, BLACK)

print('white' if knight_W.get_color() == WHITE else 'black')
print('white' if knight_B.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if (row0_W, col0_W) == (row, col):
            print(knight_W.char(), end='')
        elif (row0_B, col0_B) == (row, col):
            print(knight_B.char(), end='')
        elif knight_W.can_move(row, col) or knight_B.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()

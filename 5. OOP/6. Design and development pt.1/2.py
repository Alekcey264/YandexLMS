class Bishop:
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
        return 'B'
    
    def can_move(self, new_row, new_col):
        if not self.correct_coords(new_row, new_col):
            return False
        if abs(new_row - self.row) == abs(new_col - self.col):
            return True
        return False
    

WHITE=1
BLACK=2

row0 = 0
col0 = 2
bishop = Bishop(row0, col0, WHITE)

print('white' if bishop.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(bishop.char(), end='')
        elif bishop.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
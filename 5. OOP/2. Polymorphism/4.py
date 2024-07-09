class LineToTable:
    def __init__(self, values, *sizes):
        self.table = values
        self.n = sizes[0]
        self.m = sizes[1]

    def resize(self):
        self.temp_table = list()
        while self.table:
            self.temp_table.append(self.table[:self.m])
            self.table = self.table[self.m:]
        return self.temp_table, self.n, self.m
    
class TableToLine:
    def __init__(self, values):
        self.table = values
        self.n = len(self.table)
        self.m = len(self.table[0])
    
    def resize(self):
        self.temp_table = list()
        for item in self.table:
            self.temp_table.extend(item)
        return self.temp_table, self.n, self.m

ltt = LineToTable([1, 2, 3, 4, 5, 6], 3, 2)
matrix, a, b = ltt.resize()
print(*matrix, sep='\n')
print(f'Sizes: {a}x{b}')

ttl = TableToLine([[1, 2], [3, 4], [5, 6]])
arr, n, m = ttl.resize()
print(arr)
print(f'Resized from {n}x{m}')
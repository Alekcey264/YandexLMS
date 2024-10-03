class RightMirror:
    def __init__(self, arr):
        self.matrix = arr
    
    def reflect(self):
        self.matrix = [item[::-1] for item in self.matrix]
    

class BottomMirror:
    def __init__(self, arr):
        self.matrix = arr

    def reflect(self):
        for i in range(len(self.matrix) // 2):
            self.matrix[i], self.matrix[len(self.matrix) - 1 - i] = self.matrix[len(self.matrix) - 1 - i], self.matrix[i]


arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 0]]
rm = RightMirror(arr)
bm = BottomMirror(arr)
rm.reflect()
for item in rm.matrix:
    print(*item, sep='\t')
print()
bm.reflect()
for item in bm.matrix:
    print(*item, sep='\t')
import sqlite3


level = int(input())
where = input()

con = sqlite3.connect('forest.db')
cur = con.cursor()
result = cur.execute('''SELECT DISTINCT * FROM Events 
                     WHERE place = ? AND suddenness >= ?''', (where, level)).fetchall()

print(*sorted(set(map(lambda x: x[1], result))), sep=', ')
print(*sorted(set(map(lambda x: x[3], result))), sep=', ')
    
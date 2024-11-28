import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()

result = cur.execute('''SELECT DISTINCT year FROM films 
                     WHERE title LIKE "Х%" OR title LIKE "х%"''').fetchall()

for item in result:
    print(item[0])

con.close()
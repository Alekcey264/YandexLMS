import sqlite3


con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute('''SELECT title FROM films WHERE duration <= 85''').fetchall()
con.close()
for item in result:
    print(item[0])

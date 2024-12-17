import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()

result = cur.execute('''SELECT title FROM films WHERE genre = 
                     (SELECT id FROM genres WHERE title = "комедия") AND duration >= 60''').fetchall()

for item in result:
    print(item[0])

con.close()
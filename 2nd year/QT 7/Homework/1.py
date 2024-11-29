import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute('''SELECT title FROM films WHERE 
                     genre = (SELECT id FROM genres WHERE title = "детектив") 
                     AND year BETWEEN 1995 AND 2000''').fetchall()
con.close()
for item in result:
    print(item[0])
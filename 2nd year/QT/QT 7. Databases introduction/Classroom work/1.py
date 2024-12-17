import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

music_id = cur.execute('''SELECT id FROM genres WHERE title = "музыка"''').fetchone()
anima_id = cur.execute('''SELECT id FROM genres WHERE title = "анимация"''').fetchone()


result = cur.execute('''SELECT title FROM films WHERE genre 
                     in (?, ?) and year >= 1997''', (music_id[0], anima_id[0])).fetchall()

for item in result:
    print(item[0])

con.close()
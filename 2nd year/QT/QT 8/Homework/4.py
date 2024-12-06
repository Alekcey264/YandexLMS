import sqlite3


def get_result(name: str):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute(
        '''
        DELETE FROM films
        WHERE year < 2000 AND duration > 90 AND genre = (SELECT id FROM genres WHERE title = "фантастика")
        '''
    )
    con.commit()
    con.close()
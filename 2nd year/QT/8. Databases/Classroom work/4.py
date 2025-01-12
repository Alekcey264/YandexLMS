import sqlite3


def get_result(name: str):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute(
        '''
        DELETE FROM films
        WHERE films.title LIKE "Я%а"
        '''
    )
    con.commit()
    con.close()
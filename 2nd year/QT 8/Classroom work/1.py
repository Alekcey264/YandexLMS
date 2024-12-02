import sqlite3


def get_result(db_name: str):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute(
        '''
        DELETE FROM films
        WHERE films.genre = (SELECT genres.id from genres WHERE genres.title = "комедия")
        ''')
    con.commit()
    con.close()
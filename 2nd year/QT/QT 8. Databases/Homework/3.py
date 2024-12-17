import sqlite3


def get_result(name: str):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute(
        '''
        UPDATE films
        SET duration /= 3
        WHERE year = 1973
        '''
    )
    con.commit()
    con.close()
import sqlite3


def get_result(name: str):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute(
        '''
        UPDATE films
        SET duration = 42
        WHERE duration = ''
        ''')
    con.commit()
    con.close()
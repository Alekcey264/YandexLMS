import sqlite3


def magic_eye(name_db: str, *items) -> list[tuple]:
    con = sqlite3.connect(name_db)
    cur = con.cursor()
    res = []
    for item in items:
        result = cur.execute('''SELECT
                                Events.witness as Witness,
                                Magicians.magician as Mag,
                                Places.place as Place
                            FROM
                                Events
                            LEFT JOIN Magicians ON Events.magician_id = Magicians.id
                            LEFT JOIN Places ON Events.place_id = Places.id
                            WHERE Magicians.tool = ? AND Events.outcome < 0
                            ''', (item ,)).fetchall()
        res.extend(result)
    return sorted(res, key=lambda x: (-ord(x[2][0]), x[1], -ord(x[0][0])))


tools = ['wand', 'beard', 'eye']
print(*magic_eye('eye.db', *tools), sep='\n')
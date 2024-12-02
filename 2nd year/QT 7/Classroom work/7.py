import sqlite3

con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()

result = cur.execute(
    '''
    SELECT DISTINCT
        track.name
    FROM 
        track
    INNER JOIN album ON track.albumid = album.albumid
    INNER JOIN artist ON album.artistid = artist.artistid
    WHERE artist.name = ?
    ORDER BY track.name
    ''', (input(),)).fetchall()

for item in result:
    print(item[0])

cur.close()
import sqlite3

con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()

result = cur.execute(
    '''
    SELECT DISTINCT
        artist.name
    FROM
        artist
    INNER JOIN album ON artist.artistid = album.artistid
    INNER JOIN track ON album.albumid = track.albumid
    INNER JOIN genre ON track.genreid = genre.genreid
    WHERE genre.name = ?
    ORDER BY artist.name
    ''', (input(),)).fetchall()

for item in result:
    print(item[0])

con.close()
import sqlite3

con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()

result = cur.execute(
    '''
    SELECT DISTINCT
        album.title
    FROM 
        album
    INNER JOIN track ON album.albumid = track.albumid
    INNER JOIN genre ON track.genreid = genre.genreid
    WHERE genre.name = ?
    ORDER BY album.artistid, album.title
''', (input(),)).fetchall()

for item in result:
    print(item[0])

con.close()
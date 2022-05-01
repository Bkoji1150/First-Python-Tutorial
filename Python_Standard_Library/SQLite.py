import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
for movie in movies:
    pass

"""write data to a data base."""
'''
with sqlite3.connect("/Users/kojibello/Documents/sqlite3.db") as conn:
    command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies:
       conn.execute(command, tuple(movie.values()))
    conn.commit()   
    # print(dir(sqlite3))
'''
with sqlite3.connect("/Users/kojibello/Documents/sqlite3.db") as conn:
    command = "SELECT * FROM MovieS"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row[0])
    movie = cursor.fetchall()
    print(movie)

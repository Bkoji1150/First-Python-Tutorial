import json
from pathlib import Path

movies = {"id": 1, "title": "Terminator", "year": 1998}, {"id": 2, "title": "Kindergarden", "year": 1993}, {"id": 3, "title": "MoneyHeist", "year": 2018}

data = json.dumps(movies, indent=4)
Path("movies.json").write_text(data)
print(dict(data))
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies[0].get('titile'))


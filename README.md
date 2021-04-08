## flaskapp

Demo of CRUD operations using [Flask](https://palletsprojects.com/p/flask/) and [SQLite](https://sqlite.org/index.html)

Borrowed from https://parzibyte.me/blog/en/2020/11/12/creating-api-rest-with-python-flask-sqlite3/

Editor: https://code.visualstudio.com/

Install Poetry: https://python-poetry.org/docs/#installation

```bash
poetry install
poetry run start
```

### Using Insomnia

https://insomnia.rest/download

Import the Insomnia_....json workspace into Insomnia.

### Using cURL

```bash
# Create
curl --request POST \
  --url http://localhost:8000/games \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "Chess",
	"price": 1234.1234,
	"rate": 10
}'

# Read
curl --request GET --url http://localhost:8000/games
curl --request GET --url http://localhost:8000/games/1

# Update
curl --request PUT \
  --url http://localhost:8000/games/1 \
  --header 'Content-Type: application/json' \
  --data '{
	"id": 1,
	"name": "Cheese",
	"price": 2345.2345,
	"rate": 2
}'

# Delete
curl --request DELETE --url http://localhost:8000/games/1
```
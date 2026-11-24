# Python + SQLite

Three small Python scripts I made which cover fetching data from APIs, storing it in a database, and making a chart.

## What's inside

| File | What it does |
|------|--------------|
| `q1.py` | Fetches a list of books from the Open Library API, saves them in a SQLite database (`books.db`) and prints them |
| `q2.py` | Fetches students' test scores from an API, calculates the average and saves a bar chart (`scores_chart.png`) |
| `mock_api.py` | A tiny local API that returns students' scores as JSON (used by `q2.py`) |
| `q3.py` | Reads users from `users.csv` and inserts them into a SQLite database (`users.db`) |
| `users.csv` | Sample user data (name, email) used by `q3.py` |

## How to run

**1. Install Python 3**

**2. (Optional) Make a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac / Linux
```

**3. Install the libraries**
```bash
pip install requests matplotlib
```

**4. Run each script**
```bash
python q1.py
python q2.py
python q3.py
```

> Keep all files in the same folder. `q2.py` needs `mock_api.py` and `q3.py` needs `users.csv`.

## What each script does

### Q1: Books API to SQLite
1. Calls the Open Library API and gets 10 Python books (title, author, year).
2. Creates a `books` table in `books.db`.
3. Inserts the books (`INSERT OR IGNORE`, so running it again won't add duplicates).
4. Reads them back from the database and prints a table.

### Q2: Student scores, average and chart
1. `mock_api.py` starts a small local API at `http://localhost:8000/students`. It starts automatically when you run `q2.py`.
2. `q2.py` fetches the JSON, which looks like `{"id": 1, "name": "Asha", "score": 78}`.
3. It calculates the average score.
4. It draws a bar chart of all scores with a red dotted line for the average and saves it as `scores_chart.png`.

### Q3: CSV to SQLite
1. Reads `users.csv` row by row.
2. Checks that the name is not empty and the email has an `@`.
3. Inserts into the `users` table in `users.db`. Emails are unique, so duplicates are skipped.
4. Prints how many rows were inserted or skipped, then prints the table.

## Assumptions I made

- **I didn't find any public API that gives student test scores**, so I made my own small API (`mock_api.py`) that returns name and score as JSON. To use a different API, change `API_URL` in `q2.py` (and the keys `"name"` and `"score"` if needed).
- Q1 needs internet, because it calls the live Open Library API. If the API is down, the script will show an error message.
- The CSV file has a header row: `name,email`.
- Emails are unique, so a repeated email is skipped instead of crashing the script.

## Tech used

- Python 3
- SQLite (`sqlite3`, built into Python)
- `requests` for calling APIs
- `matplotlib` for the chart

## Author

**Sharanya Bengoor**

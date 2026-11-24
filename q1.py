import sqlite3
import requests

API_URL = "https://openlibrary.org/search.json?q=python&limit=10&fields=title,author_name,first_publish_year"
DB_NAME = "books.db"

def fetch_books():
    """Step 1: call the API and return a list of books."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()           
        return response.json()["docs"]        
    except Exception as e:
        print(f"[!] API failed ({e}).")
        return SAMPLE_BOOKS

def create_table(conn):
    """Step 2: make the table (only if it doesn't exist)."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title  TEXT NOT NULL,
            author TEXT,
            year   INTEGER,
            UNIQUE(title, author)            -- avoids duplicates on re-run
        )
    """)

def save_books(conn, books):
    """Step 3: insert each book into the table."""
    for b in books:
        title = b.get("title")
        authors = b.get("author_name", ["Unknown"])
        author = ", ".join(authors)          
        year = b.get("first_publish_year")   
        conn.execute(
            "INSERT OR IGNORE INTO books (title, author, year) VALUES (?, ?, ?)",
            (title, author, year),
        )
    conn.commit()

def show_books(conn):
    """Step 4: read from DB and print."""
    rows = conn.execute("SELECT id, title, author, year FROM books").fetchall()
    print(f"\n{'ID':<4}{'Title':<45}{'Author':<30}{'Year':<6}")
    print("-" * 85)
    for r in rows:
        print(f"{r[0]:<4}{str(r[1])[:43]:<45}{str(r[2])[:28]:<30}{str(r[3]):<6}")
    print(f"\nTotal books in DB: {len(rows)}")

if __name__ == "__main__":
    books = fetch_books()
    conn = sqlite3.connect(DB_NAME)
    create_table(conn)
    save_books(conn, books)
    show_books(conn)
    conn.close()

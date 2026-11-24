import csv
import sqlite3

CSV_FILE = "users.csv"
DB_NAME = "users.db"

def main():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    inserted = skipped = 0
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)          
        for row in reader:
            name = row["name"].strip()
            email = row["email"].strip().lower()
            if not name or "@" not in email:  
                skipped += 1
                continue
            cur = conn.execute(
                "INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)",
                (name, email),
            )
            inserted += cur.rowcount           
            skipped += 1 - cur.rowcount
    conn.commit()

    print(f"Inserted: {inserted} | Skipped: {skipped}\n")
    for row in conn.execute("SELECT id, name, email FROM users"):
        print(row)
    conn.close()

if __name__ == "__main__":
    main()

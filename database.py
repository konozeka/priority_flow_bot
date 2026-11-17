import sqlite3

def init_db():
    conn = sqlite3.connect('priority_flow.db')

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    urgent INTEGER NOT NULL,
    important INTEGER NOT NULL,
    done INTEGER DEFAULT 0,
    created_at TEXT,
    done_at TEXT
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("База данных и таблица успешно созданы!")
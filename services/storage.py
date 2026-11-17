import sqlite3
from datetime import datetime
from models.task import Task

def get_connection():
    return sqlite3.connect('priority_flow.db')

def row_to_task(row):
    if not row:
        return None
    return Task(
        user_id=row[1],
        text=row[2],
        urgent=bool(row[3]),
        important=bool(row[4]),
        task_id=row[0],
        done=bool(row[5]),
        created_at=row[6],
        done_at=row[7]
    )

def add_task(user_id: int, text: str, urgent: bool, important: bool) -> Task:
    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now().isoformat()

    cursor.execute(
        "INSERT INTO tasks (user_id, text, urgent, important, created_at) VALUES (?, ?, ?, ?, ?)",
        (user_id, text, int(urgent), int(important), now)
    )
    
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return Task(user_id, text, urgent, important, task_id=task_id, created_at=now)

def get_user_tasks(user_id: int) -> list[Task]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()

    return [row_to_task(row) for row in rows]

def get_tasks_by_quadrant(user_id: int, quadrant: int) -> list[Task]:
    all_tasks = get_user_tasks(user_id)
    return [task for task in all_tasks if task.quadrant() == quadrant and not task.done]

def mark_task_done(user_id: int, task_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now().isoformat()

    cursor.execute(
        "UPDATE tasks SET done = 1, done_at = ? WHERE id = ? AND user_id = ?",
        (now, task_id, user_id)
    )

    success = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return success

def get_stats(user_id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*), SUM(done) FROM tasks WHERE user_id = ?",
        (user_id,)
    )
    result = cursor.fetchone()
    conn.close()

    total = result[0] if result[0] else 0
    completed = result[1] if result[1] else 0

    return {"total": total, "completed": completed}

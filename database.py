import sqlite3


def connect():
    conn = sqlite3.connect('instance/test.db')
    return conn


def fetch_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id, task_name FROM tasks")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

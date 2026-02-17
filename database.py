import sqlite3

def init_db():
    conn = sqlite3.connect("wafer_scans.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT,
            defect_count INTEGER
        )
    """)

    conn.commit()
    conn.close()

def save_scan(image_path, defect_count):
    conn = sqlite3.connect("wafer_scans.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scans (image_path, defect_count) VALUES (?, ?)",
        (image_path, defect_count)
    )

    conn.commit()
    conn.close()

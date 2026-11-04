import sqlite3
from pathlib import Path


DATABASE_PATH = Path("database/mpts.db")


def create_database():

    DATABASE_PATH.parent.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()


    print("Connected to MPTS database")


    # -------------------------
    # Departments
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (

        department_id INTEGER PRIMARY KEY,

        department_name TEXT NOT NULL UNIQUE

    )
    """)


    # -------------------------
    # Machines
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS machines (

        machine_id INTEGER PRIMARY KEY,

        department_id INTEGER,

        machine_number INTEGER,

        machine_name TEXT,

        category TEXT,

        setup_target_days INTEGER,

        active INTEGER DEFAULT 1,

        FOREIGN KEY(department_id)
        REFERENCES departments(department_id)

    )
    """)


    # -------------------------
    # Operators
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS operators (

        operator_id INTEGER PRIMARY KEY,

        employee_id TEXT UNIQUE,

        operator_name TEXT NOT NULL,

        active INTEGER DEFAULT 1

    )
    """)


    # -------------------------
    # Administrator
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin_users (

        admin_id INTEGER PRIMARY KEY,

        username TEXT UNIQUE,

        password_hash TEXT,

        active INTEGER DEFAULT 1

    )
    """)


    # -------------------------
    # Daily Machine Entries
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS machine_entries (

        entry_id INTEGER PRIMARY KEY,

        entry_date TEXT,

        shift TEXT,

        machine_id INTEGER,

        operator_id INTEGER,

        part_number TEXT,

        status TEXT,

        hours_worked REAL,

        setup_day INTEGER,

        down_reason TEXT,

        comments TEXT,

        last_updated_by TEXT,

        updated_timestamp TEXT

    )
    """)


    # -------------------------
    # Setup History
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS setup_history (

        setup_id INTEGER PRIMARY KEY,

        machine_id INTEGER,

        operator_id INTEGER,

        part_number TEXT,

        start_date TEXT,

        end_date TEXT,

        setup_days REAL,

        setup_hours REAL,

        target_days REAL,

        met_target INTEGER

    )
    """)


    # -------------------------
    # Activity Log
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity_log (

        log_id INTEGER PRIMARY KEY,

        timestamp TEXT,

        user TEXT,

        action TEXT,

        details TEXT

    )
    """)


    # -------------------------
    # Shift Notes
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shift_notes (

        note_id INTEGER PRIMARY KEY,

        date TEXT,

        shift TEXT,

        department_id INTEGER,

        notes TEXT,

        entered_by TEXT,

        timestamp TEXT

    )
    """)


    # -------------------------
    # Backup Log
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS backup_log (

        backup_id INTEGER PRIMARY KEY,

        backup_date TEXT,

        filename TEXT,

        status TEXT

    )
    """)


    # -------------------------
    # Settings
    # -------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings (

        setting_name TEXT PRIMARY KEY,

        setting_value TEXT

    )
    """)


    connection.commit()

    connection.close()


    print("MPTS database foundation created successfully")


if __name__ == "__main__":

    create_database()
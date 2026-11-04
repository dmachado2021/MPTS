"""
MPTS - Manufacturing Production Tracking System
Database Migration 001

Adds production record tracking.

Version: 1.0.2
"""

import sqlite3
from pathlib import Path


DATABASE_PATH = Path("database/mpts.db")



def migrate():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()


    print("Running MPTS Database Migration 001...")


    # ---------------------------------
    # Production Records Table
    # ---------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS production_records
    (

        record_id INTEGER PRIMARY KEY AUTOINCREMENT,


        record_date TEXT NOT NULL,


        shift TEXT NOT NULL,


        department_id INTEGER NOT NULL,


        machine_id INTEGER NOT NULL,


        employee_id TEXT,


        operator_name TEXT,


        part_number TEXT,


        status TEXT NOT NULL,


        hours REAL DEFAULT 0,


        down_reason TEXT,


        setup_start_date TEXT,


        setup_end_date TEXT,


        created_timestamp TEXT DEFAULT CURRENT_TIMESTAMP,


        FOREIGN KEY(department_id)
            REFERENCES departments(department_id),


        FOREIGN KEY(machine_id)
            REFERENCES machines(machine_id)

    )
    """)



    connection.commit()


    connection.close()


    print(
        "Migration 001 completed successfully"
    )



if __name__ == "__main__":

    migrate()
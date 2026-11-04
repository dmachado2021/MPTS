"""
MPTS - Manufacturing Production Tracking System
Production Database Service
Version: 1.0.0
"""

import sqlite3
from datetime import datetime

from config import DATABASE_PATH



def get_server_date():

    """
    Gets official MPTS date from database server.
    """

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT date('now')
        """
    )


    result = cursor.fetchone()


    connection.close()


    return result[0]



def save_machine_entry(
    entry_date,
    shift,
    machine_id,
    operator_id,
    part_number,
    status,
    hours,
    setup_day,
    down_reason
):

    """
    Saves one machine shift record.
    """


    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO machine_entries
        (
            entry_date,
            shift,
            machine_id,
            operator_id,
            part_number,
            status,
            hours_worked,
            setup_day,
            down_reason,
            updated_timestamp
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,
        (
            entry_date,
            shift,
            machine_id,
            operator_id,
            part_number,
            status,
            hours,
            setup_day,
            down_reason,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
    )


    connection.commit()

    connection.close()
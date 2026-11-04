"""
MPTS - Manufacturing Production Tracking System
Operator Database Service
Version: 1.0.0
"""

import sqlite3

from config import DATABASE_PATH


def get_operator(employee_id):

    """
    Lookup operator by employee ID.

    Returns:
        Operator name if found
        Unknown Operator if not found
    """

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT operator_name
        FROM operators
        WHERE employee_id = ?
        """,
        (str(employee_id),)
    )


    result = cursor.fetchone()


    connection.close()


    if result:
        return result[0]


    return "Unknown Operator"
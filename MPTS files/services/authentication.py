import sqlite3
import hashlib
from pathlib import Path


DATABASE_PATH = Path("database/mpts.db")


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def create_admin_account():

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    password = "ChangeMe123"

    cursor.execute("""
    INSERT OR IGNORE INTO admin_users
    (
        username,
        password_hash
    )
    VALUES (?,?)
    """,
    (
        "Admin",
        hash_password(password)
    ))

    connection.commit()
    connection.close()


def verify_login(username, password):

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT password_hash
    FROM admin_users
    WHERE username = ?
    AND active = 1
    """,
    (username,))


    result = cursor.fetchone()

    connection.close()


    if result:

        stored_password = result[0]

        if stored_password == hash_password(password):
            return True


    return False
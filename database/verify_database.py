import sqlite3
from pathlib import Path


DATABASE_PATH = Path("database/mpts.db")


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


print("\nMPTS DATABASE VERIFICATION")
print("--------------------------")


# Departments

cursor.execute(
    "SELECT COUNT(*) FROM departments"
)

print(
    "Departments:",
    cursor.fetchone()[0]
)


# Machines

cursor.execute(
    "SELECT COUNT(*) FROM machines"
)

print(
    "Machines:",
    cursor.fetchone()[0]
)


# Operators

cursor.execute(
    "SELECT COUNT(*) FROM operators"
)

print(
    "Operators:",
    cursor.fetchone()[0]
)


# Check machine 13

cursor.execute("""
SELECT COUNT(*)
FROM machines
WHERE machine_number = 13
""")


print(
    "Machine #13 records:",
    cursor.fetchone()[0]
)


# Show department totals

cursor.execute("""
SELECT 
departments.department_name,
COUNT(machines.machine_id)

FROM machines

JOIN departments
ON machines.department_id = departments.department_id

GROUP BY departments.department_name

""")


print("\nMachine Count By Department:")

for row in cursor.fetchall():
    print(row[0], ":", row[1])


connection.close()
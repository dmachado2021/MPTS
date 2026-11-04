import sqlite3
from pathlib import Path


DATABASE_PATH = Path("database/mpts.db")


def load_data():

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    print("Loading MPTS initial data...")


    # -------------------------
    # Departments
    # -------------------------

    departments = [
        "Escomatic",
        "Swiss",
        "CNC"
    ]

    for dept in departments:
        cursor.execute("""
        INSERT OR IGNORE INTO departments (department_name)
        VALUES (?)
        """, (dept,))


    connection.commit()


    # Get department IDs

    cursor.execute(
        "SELECT department_id, department_name FROM departments"
    )

    department_ids = {
        name: dept_id
        for dept_id, name in cursor.fetchall()
    }


    # -------------------------
    # Machines
    # -------------------------

    machines = []


    # Escomatic

    esco_d2 = list(range(18,35)) + [49,52]

    esco_d4 = (
        list(range(1,13))
        + list(range(14,18))
        + [35,50,51,53,54]
    )

    esco_d6 = [44,55]

    esco_d6r = (
        list(range(36,44))
        + list(range(45,49))
        + [56]
    )


    for machine in esco_d2:
        machines.append(
            ("Escomatic", machine, "D2", 1)
        )

    for machine in esco_d4:
        machines.append(
            ("Escomatic", machine, "D4", 2)
        )

    for machine in esco_d6:
        machines.append(
            ("Escomatic", machine, "D6", 2)
        )

    for machine in esco_d6r:
        machines.append(
            ("Escomatic", machine, "D6R", 3)
        )


    # Swiss

    swiss_numbers = list(range(1,13)) + list(range(14,24))

    for machine in swiss_numbers:
        machines.append(
            ("Swiss", machine, "Standard", 4)
        )


    # CNC

    for machine in range(25,34):
        machines.append(
            ("CNC", machine, "Standard", 2)
        )


    for department, number, category, target in machines:

        cursor.execute("""
        INSERT OR IGNORE INTO machines
        (
            department_id,
            machine_number,
            machine_name,
            category,
            setup_target_days
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            department_ids[department],
            number,
            f"{department} #{number}",
            category,
            target
        ))


    # -------------------------
    # Operators
    # -------------------------

    operators = [

        ("413","Matthew Dorosh"),
        ("418","Mark Commendatore"),
        ("422","Daniel Moher"),
        ("426","Robert Nearing"),
        ("440","Hector Rivera"),
        ("458","Joel Otero"),
        ("462","David Bodine"),
        ("505","Ari Alfaro"),
        ("523","Frank Belo"),
        ("524","Stephen Duplessie"),
        ("527","Allen Gordon"),
        ("540","Herion Beshi"),
        ("550","Klodian Beshi"),
        ("582","Martin Thomas"),
        ("595","Thomas Neville"),
        ("601","Steven Kontout"),
        ("634","Christopher Perugini"),
        ("635","Jose Arroyo"),
        ("636","Rosaire Pelletier"),
        ("637","Andres Dela Cruz"),
        ("647","Dashalee Ribot"),
        ("648","Joseph Showers"),
        ("649","Bart Marcoux"),
        ("666","Richard LaBonte")

    ]


    for employee_id, name in operators:

        cursor.execute("""
        INSERT OR IGNORE INTO operators
        (
            employee_id,
            operator_name
        )
        VALUES (?,?)
        """,
        (
            employee_id,
            name
        ))


    connection.commit()

    connection.close()

    print("MPTS initial data loaded successfully")


if __name__ == "__main__":
    load_data()
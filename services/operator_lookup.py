"""
MPTS - Manufacturing Production Tracking System
Operator Lookup Service
Version: 1.0.0
"""


OPERATORS = {

    "413": "Matthew Dorosh",
    "418": "Mark Commendatore",
    "422": "Daniel Moher",
    "426": "Robert Nearing",
    "440": "Hector Rivera",
    "458": "Joel Otero",
    "462": "David Bodine",
    "505": "Ari Alfaro",
    "523": "Frank Belo",
    "524": "Stephen Duplessie",
    "527": "Allen Gordon",
    "540": "Herion Beshi",
    "550": "Klodian Beshi",
    "582": "Martin Thomas",
    "595": "Thomas Neville",
    "601": "Steven Kontout",
    "634": "Christopher Perugini",
    "635": "Jose Arroyo",
    "636": "Rosaire Pelletier",
    "637": "Andres Dela Cruz",
    "647": "Dashalee Ribot",
    "648": "Joseph Showers",
    "649": "Bart Marcoux",
    "666": "Richard LaBonte"

}


def get_operator(employee_id):

    return OPERATORS.get(
        str(employee_id),
        ""
    )
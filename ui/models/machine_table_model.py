"""
MPTS - Manufacturing Production Tracking System
Machine Table Model
Version: 1.0.2
"""

from PySide6.QtCore import (
    Qt,
    QAbstractTableModel,
    QModelIndex
)

from services.operator_service import get_operator


class MachineTableModel(QAbstractTableModel):

    HEADERS = [
        "Machine",
        "Employee ID",
        "Operator",
        "Part Number",
        "Status",
        "Hours",
        "Down Reason",
        "Setup Day",
        "Last Updated"
    ]


    def __init__(self, machines):

        super().__init__()

        self.data_rows = []


        for machine in machines:

            self.data_rows.append(
                [
                    machine,              # Machine
                    "",                   # Employee ID
                    "",                   # Operator
                    "",                   # Part Number
                    "⚪ No Operator",      # Status
                    "0",                  # Hours
                    "",                   # Down Reason
                    "",                   # Setup Day
                    ""                    # Last Updated
                ]
            )


    def rowCount(self, parent=QModelIndex()):

        return len(self.data_rows)



    def columnCount(self, parent=QModelIndex()):

        return len(self.HEADERS)



    def headerData(
        self,
        section,
        orientation,
        role
    ):

        if role == Qt.DisplayRole:

            if orientation == Qt.Horizontal:
                return self.HEADERS[section]

            if orientation == Qt.Vertical:
                return section + 1

        return None



    def data(
        self,
        index,
        role
    ):

        if not index.isValid():

            return None


        row = index.row()
        column = index.column()


        if role == Qt.DisplayRole:

            return self.data_rows[row][column]


        if role == Qt.TextAlignmentRole:

            return Qt.AlignCenter


        return None



    def flags(self, index):

        if not index.isValid():

            return Qt.NoItemFlags


        row = index.row()
        column = index.column()


        # Locked columns

        if column in [0, 2, 8]:

            return (
                Qt.ItemIsEnabled |
                Qt.ItemIsSelectable
            )


        status = self.data_rows[row][4]


        # Down Reason

        if column == 6:

            if status == "🔴 Down":

                return (
                    Qt.ItemIsEnabled |
                    Qt.ItemIsSelectable |
                    Qt.ItemIsEditable
                )

            return (
                Qt.ItemIsEnabled |
                Qt.ItemIsSelectable
            )


        # Setup Day

        if column == 7:

            if status == "🟡 Set-up":

                return (
                    Qt.ItemIsEnabled |
                    Qt.ItemIsSelectable |
                    Qt.ItemIsEditable
                )

            return (
                Qt.ItemIsEnabled |
                Qt.ItemIsSelectable
            )


        return (
            Qt.ItemIsEnabled |
            Qt.ItemIsSelectable |
            Qt.ItemIsEditable
        )



    def apply_status_rules(
        self,
        row,
        status
    ):

        if status == "🟢 Running":

            self.data_rows[row][6] = ""
            self.data_rows[row][7] = ""


        elif status == "🔴 Down":

            self.data_rows[row][7] = ""


        elif status == "🟡 Set-up":

            self.data_rows[row][6] = ""


        elif status == "⚪ No Operator":

            self.data_rows[row][1] = ""
            self.data_rows[row][2] = ""
            self.data_rows[row][5] = "0"
            self.data_rows[row][6] = ""
            self.data_rows[row][7] = ""



    def setData(
        self,
        index,
        value,
        role=Qt.EditRole
    ):


        if role != Qt.EditRole:

            return False


        row = index.row()
        column = index.column()



        # Employee ID lookup

        if column == 1:

            employee_id = str(value).strip()

            operator = get_operator(
                employee_id
            )


            self.data_rows[row][1] = employee_id
            self.data_rows[row][2] = operator


            self.dataChanged.emit(
                self.index(row,1),
                self.index(row,2)
            )


            return True



        # Status logic

        if column == 4:

            status = str(value)


            self.data_rows[row][4] = status


            self.apply_status_rules(
                row,
                status
            )


            self.dataChanged.emit(
                self.index(row,1),
                self.index(row,7),
                [Qt.DisplayRole, Qt.EditRole]
            )


            self.layoutChanged.emit()


            return True



        # Normal edits

        self.data_rows[row][column] = value


        self.dataChanged.emit(
            index,
            index
        )


        return True
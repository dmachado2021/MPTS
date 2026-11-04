"""
MPTS - Manufacturing Production Tracking System
Department Page
Version: 1.0.0
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton
)

from ui.models.machine_table_model import MachineTableModel
from ui.widgets.machine_table_view import MachineTableView
from ui.widgets.date_selector import DateSelector
from ui.widgets.shift_selector import ShiftSelector


class DepartmentPage(QWidget):

    def __init__(self, department, machines):
        super().__init__()

        self.department = department
        self.machines = machines

        self.build_ui()


    def build_ui(self):

        main_layout = QVBoxLayout(self)


        # Department Title
        title = QLabel(
            self.department
        )

        title.setStyleSheet(
            """
            QLabel {
                font-size: 26px;
                font-weight: bold;
            }
            """
        )


        main_layout.addWidget(title)


        # Controls Area
        controls = QHBoxLayout()


        self.date_selector = DateSelector()

        self.shift_selector = ShiftSelector()


        save_button = QPushButton(
            "Save Shift"
        )

        save_button.clicked.connect(
            self.save_shift
        )


        controls.addWidget(
            self.date_selector
        )

        controls.addWidget(
            self.shift_selector
        )

        controls.addStretch()

        controls.addWidget(
            save_button
        )


        main_layout.addLayout(
            controls
        )


        # Machine Table

        self.model = MachineTableModel(
            self.machines
        )

        self.table = MachineTableView(
            self.model
        )


        main_layout.addWidget(
            self.table
        )


    def save_shift(self):

        print(
            f"Saving {self.department}"
        )

        print(
            "Date:",
            self.date_selector.get_date()
        )

        print(
            "Shift:",
            self.shift_selector.get_shift()
        )
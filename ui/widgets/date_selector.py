"""
MPTS - Manufacturing Production Tracking System
Date Selector Widget
Version: 1.0.0
"""

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QDateEdit
)

from PySide6.QtCore import QDate


class DateSelector(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()


    def build_ui(self):

        layout = QHBoxLayout(self)

        label = QLabel("Date:")

        self.date_box = QDateEdit()

        # Default to today's date
        self.date_box.setDate(
            QDate.currentDate()
        )

        # Enable calendar popup
        self.date_box.setCalendarPopup(True)

        # Display format
        self.date_box.setDisplayFormat(
            "MM/dd/yyyy"
        )


        layout.addWidget(label)

        layout.addWidget(self.date_box)


        layout.addStretch()


    def get_date(self):

        return self.date_box.date().toString(
            "yyyy-MM-dd"
        )


    def set_date(self, value):

        date = QDate.fromString(
            value,
            "yyyy-MM-dd"
        )

        self.date_box.setDate(date)
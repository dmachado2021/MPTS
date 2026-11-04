"""
MPTS - Manufacturing Production Tracking System
Main Window
Version: 1.0.0
"""

from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTabWidget,
    QStatusBar
)

from config import APP_NAME, VERSION, SHIFTS

from ui.department_page import DepartmentPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            f"{APP_NAME}  v{VERSION}"
        )

        # Full HD design target
        self.showMaximized()

        # Manual shift selection for now
        self.current_shift = SHIFTS[0]

        self.build_ui()


    def build_ui(self):

        self.tabs = QTabWidget()

        # Dashboard
        self.tabs.addTab(
            self.dashboard_page(),
            "Dashboard"
        )


        # Escomatic
        self.tabs.addTab(
            DepartmentPage(
                "Escomatic",
                list(range(1, 57))
            ),
            "Escomatic"
        )


        # Swiss (skip machine 13)
        self.tabs.addTab(
            DepartmentPage(
                "Swiss",
                [x for x in range(1, 24) if x != 13]
            ),
            "Swiss"
        )


        # CNC
        self.tabs.addTab(
            DepartmentPage(
                "CNC",
                list(range(25, 34))
            ),
            "CNC"
        )


        # Administrator placeholder
        self.tabs.addTab(
            self.admin_page(),
            "🔒 Administrator"
        )


        self.setCentralWidget(self.tabs)


        # Status Bar
        status = QStatusBar()

        status.showMessage(
            f"🟢 Database Connected   |   "
            f"Date: {date.today()}   |   "
            f"Version {VERSION}"
        )

        self.setStatusBar(status)



    def dashboard_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)


        title = QLabel(
            "MPTS\nManufacturing Production Tracking System"
        )

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet(
            """
            QLabel {
                font-size: 28px;
                font-weight: bold;
            }
            """
        )


        date_label = QLabel(
            f"Current Date: {date.today()}"
        )

        date_label.setAlignment(Qt.AlignCenter)

        date_label.setStyleSheet(
            "font-size:18px;"
        )


        shift_label = QLabel(
            f"Current Shift: {self.current_shift}"
        )

        shift_label.setAlignment(Qt.AlignCenter)

        shift_label.setStyleSheet(
            "font-size:18px;"
        )


        layout.addStretch()

        layout.addWidget(title)

        layout.addSpacing(20)

        layout.addWidget(date_label)

        layout.addWidget(shift_label)

        layout.addStretch()


        return page



    def admin_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)


        label = QLabel(
            "🔒 Administrator Login Required\n\n"
            "Reports and Administration\n"
            "will be available after login."
        )

        label.setAlignment(Qt.AlignCenter)

        label.setStyleSheet(
            """
            QLabel {
                font-size: 22px;
                font-weight: bold;
            }
            """
        )


        layout.addWidget(label)


        return page
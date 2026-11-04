"""
MPTS - Manufacturing Production Tracking System
Main Application Entry Point
Version: 1.0.0
"""

import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
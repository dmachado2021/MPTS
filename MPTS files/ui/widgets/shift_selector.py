"""
MPTS - Manufacturing Production Tracking System
Shift Selector Widget
Version: 1.0.0
"""

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QComboBox
)

from config import SHIFTS


class ShiftSelector(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()


    def build_ui(self):

        layout = QHBoxLayout(self)

        label = QLabel("Shift:")

        self.shift_box = QComboBox()

        self.shift_box.addItems(SHIFTS)

        self.shift_box.setCurrentIndex(0)

        layout.addWidget(label)

        layout.addWidget(self.shift_box)

        layout.addStretch()


    def get_shift(self):

        return self.shift_box.currentText()


    def set_shift(self, shift):

        index = self.shift_box.findText(shift)

        if index >= 0:
            self.shift_box.setCurrentIndex(index)
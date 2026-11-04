"""
MPTS - Manufacturing Production Tracking System
Machine Table View
Version: 1.0.0
"""

from PySide6.QtWidgets import QTableView
from PySide6.QtCore import Qt

from ui.delegates.status_delegate import StatusDelegate
from ui.delegates.down_reason_delegate import DownReasonDelegate


class MachineTableView(QTableView):

    def __init__(self, model):
        super().__init__()

        self.setModel(model)


        # Status dropdown
        self.setItemDelegateForColumn(
            4,
            StatusDelegate()
        )


        # Down Reason dropdown
        self.setItemDelegateForColumn(
            6,
            DownReasonDelegate()
        )


        # No row coloring
        self.setAlternatingRowColors(False)


        # Hide row numbers
        self.verticalHeader().setVisible(False)


        # Cell selection
        self.setSelectionBehavior(
            QTableView.SelectItems
        )


        # Editing
        self.setEditTriggers(
            QTableView.DoubleClicked
            |
            QTableView.EditKeyPressed
            |
            QTableView.SelectedClicked
        )


        # Keyboard navigation
        self.setTabKeyNavigation(True)


        # Header settings
        header = self.horizontalHeader()

        header.setStretchLastSection(False)

        header.setDefaultAlignment(
            Qt.AlignCenter
        )


        # Column widths
        widths = [
            80,    # Machine
            100,   # Employee ID
            180,   # Operator
            150,   # Part Number
            150,   # Status
            80,    # Hours
            170,   # Down Reason
            100,   # Setup Day
            150    # Last Updated
        ]


        for index, width in enumerate(widths):

            self.setColumnWidth(
                index,
                width
            )


        self.verticalHeader().setDefaultSectionSize(
            28
        )


        self.setHorizontalScrollMode(
            QTableView.ScrollPerPixel
        )

        self.setVerticalScrollMode(
            QTableView.ScrollPerPixel
        )
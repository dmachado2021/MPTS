"""
MPTS - Manufacturing Production Tracking System
Status Dropdown Delegate
Version: 1.0.0
"""

from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import Qt


class StatusDelegate(QStyledItemDelegate):

    STATUSES = [
        "🟢 Running",
        "🟡 Set-up",
        "🔴 Down",
        "⚪ No Operator"
    ]


    def createEditor(
        self,
        parent,
        option,
        index
    ):

        combo = QComboBox(parent)

        combo.addItems(
            self.STATUSES
        )

        return combo



    def setEditorData(
        self,
        editor,
        index
    ):

        current = index.data()

        editor.setCurrentText(
            current
        )



    def setModelData(
        self,
        editor,
        model,
        index
    ):

        model.setData(
            index,
            editor.currentText(),
            Qt.EditRole
        )
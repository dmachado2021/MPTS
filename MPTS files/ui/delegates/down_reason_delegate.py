"""
MPTS - Manufacturing Production Tracking System
Down Reason Dropdown Delegate
Version: 1.0.0
"""

from PySide6.QtWidgets import (
    QStyledItemDelegate,
    QComboBox
)

from PySide6.QtCore import Qt


class DownReasonDelegate(QStyledItemDelegate):

    REASONS = [
        "Repair",
        "Maintenance",
        "No Material",
        "Electrical Problems",
        "No Job"
    ]


    def createEditor(
        self,
        parent,
        option,
        index
    ):

        combo = QComboBox(parent)

        combo.addItems(
            self.REASONS
        )

        return combo



    def setEditorData(
        self,
        editor,
        index
    ):

        editor.setCurrentText(
            index.data()
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
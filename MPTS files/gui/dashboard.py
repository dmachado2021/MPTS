import tkinter as tk

from gui.escomatic_tab import EscomaticTab
from gui.swiss_tab import SwissTab
from gui.cnc_tab import CNCTab


class Dashboard:


    def __init__(self, root):

        self.root = root

        self.root.title(
            "MPTS Production Tracker Dashboard"
        )

        self.root.geometry(
            "1000x600"
        )


        title = tk.Label(
            root,
            text="MPTS Production Tracker Dashboard",
            font=("Arial", 20, "bold")
        )

        title.pack(pady=20)


        button_frame = tk.Frame(root)

        button_frame.pack(pady=30)



        buttons = [
            ("Escomatic", self.open_escomatic),
            ("Swiss", self.open_swiss),
            ("CNC", self.open_cnc),
            ("Administration", None)
        ]



        for text, command in buttons:

            tk.Button(
                button_frame,
                text=text,
                width=20,
                height=2,
                command=command
            ).pack(
                pady=5
            )



    def open_escomatic(self):

        EscomaticTab()



    def open_swiss(self):

        SwissTab()



    def open_cnc(self):

        CNCTab()
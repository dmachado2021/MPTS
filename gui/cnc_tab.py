import tkinter as tk

from gui.department_grid import DepartmentGrid


class CNCTab:


    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title(
            "MPTS - CNC Department"
        )

        self.window.geometry(
            "1400x700"
        )


        machines = list(range(25,34))


        DepartmentGrid(
            self.window,
            "CNC",
            [
                f"CNC #{machine}"
                for machine in machines
            ]
        )
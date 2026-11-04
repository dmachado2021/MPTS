import tkinter as tk

from gui.department_grid import DepartmentGrid


class SwissTab:


    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title(
            "MPTS - Swiss Department"
        )

        self.window.geometry(
            "1400x700"
        )


        machines = list(range(1,24))

        machines.remove(13)


        DepartmentGrid(
            self.window,
            "Swiss",
            [
                f"Swiss #{machine}"
                for machine in machines
            ]
        )
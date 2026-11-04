import tkinter as tk

from gui.department_grid import DepartmentGrid


class EscomaticTab:


    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title(
            "MPTS - Escomatic Department"
        )

        self.window.geometry(
            "1400x700"
        )


        machines = list(range(1,57))

        machines.remove(13)


        DepartmentGrid(
            self.window,
            "Escomatic",
            [
                f"Escomatic #{machine}"
                for machine in machines
            ]
        )
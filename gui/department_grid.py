import tkinter as tk
from datetime import datetime

from gui.entry_row import EntryRow


class DepartmentGrid:


    def __init__(self, parent, department_name, machines):

        self.parent = parent
        self.department_name = department_name
        self.machines = machines

        self.rows = []


        self.frame = tk.Frame(parent)

        self.frame.pack(
            fill="both",
            expand=True
        )


        self.create_header()

        self.create_column_headers()

        self.create_rows()



    def create_header(self):

        header = tk.Frame(self.frame)

        header.pack(
            fill="x",
            pady=10
        )


        tk.Label(
            header,
            text=f"{self.department_name} Department",
            font=("Arial",18,"bold")
        ).pack()



        tk.Label(
            header,
            text=f"Date: {datetime.now().strftime('%m/%d/%Y')}"
        ).pack()



        shift_frame = tk.Frame(header)

        shift_frame.pack(
            pady=5
        )


        tk.Label(
            shift_frame,
            text="Shift:"
        ).pack(
            side="left"
        )


        self.shift = tk.StringVar()

        self.shift.set(
            "Shift 1"
        )


        tk.OptionMenu(
            shift_frame,
            self.shift,
            "Shift 1",
            "Shift 2"
        ).pack(
            side="left"
        )



        tk.Button(
            header,
            text="Save Shift"
        ).pack(
            pady=5
        )



    def create_column_headers(self):

        header = tk.Frame(self.frame)

        header.pack(
            fill="x"
        )


        columns = [
            "Machine",
            "Employee ID",
            "Operator",
            "Part Number",
            "Status",
            "Hours",
            "Down Reason",
            "Setup Day"
        ]


        widths = [
            15,
            10,
            18,
            15,
            15,
            8,
            18,
            10
        ]


        for text, width in zip(columns, widths):

            tk.Label(
                header,
                text=text,
                width=width,
                relief="ridge"
            ).pack(
                side="left"
            )



    def create_rows(self):

        for machine in self.machines:

            row = EntryRow(
                self.frame,
                machine
            )


            row.frame.pack(
                fill="x",
                pady=2
            )


            self.rows.append(row)
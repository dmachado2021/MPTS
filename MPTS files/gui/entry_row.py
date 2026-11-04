import tkinter as tk
from tkinter import ttk

from services.operator_lookup import get_operator_name


class EntryRow:


    def __init__(self, parent, machine_name):

        self.machine_name = machine_name


        self.frame = tk.Frame(parent)


        # Machine Name

        tk.Label(
            self.frame,
            text=machine_name,
            width=15
        ).grid(
            row=0,
            column=0,
            padx=2
        )


        # Employee ID

        self.employee_id = tk.Entry(
            self.frame,
            width=10
        )

        self.employee_id.grid(
            row=0,
            column=1,
            padx=2
        )

        self.employee_id.bind(
            "<FocusOut>",
            self.lookup_operator
        )


        # Operator Name

        self.operator_name = tk.Label(
            self.frame,
            text="",
            width=18,
            anchor="w"
        )

        self.operator_name.grid(
            row=0,
            column=2,
            padx=2
        )


        # Part Number

        self.part_number = tk.Entry(
            self.frame,
            width=15
        )

        self.part_number.grid(
            row=0,
            column=3,
            padx=2
        )


        # Status Dropdown

        self.status = ttk.Combobox(
            self.frame,
            width=15,
            values=[
                "🟢 Running",
                "🔴 Down",
                "🟡 Set-up",
                "⚪ No Operator"
            ],
            state="readonly"
        )

        self.status.current(3)

        self.status.grid(
            row=0,
            column=4,
            padx=2
        )


        self.status.bind(
            "<<ComboboxSelected>>",
            self.status_changed
        )


        # Hours Worked

        self.hours = tk.Entry(
            self.frame,
            width=8
        )

        self.hours.grid(
            row=0,
            column=5,
            padx=2
        )


        # Down Reason

        self.down_reason = ttk.Combobox(
            self.frame,
            width=18,
            values=[
                "Repair",
                "Maintenance",
                "No Material",
                "Electrical Problems",
                "No Job"
            ],
            state="disabled"
        )

        self.down_reason.grid(
            row=0,
            column=6,
            padx=2
        )


        # Setup Day

        self.setup_day = tk.Label(
            self.frame,
            text="",
            width=10
        )

        self.setup_day.grid(
            row=0,
            column=7,
            padx=2
        )



    def lookup_operator(self, event):

        employee_id = self.employee_id.get()


        if employee_id:

            name = get_operator_name(
                employee_id
            )


            self.operator_name.config(
                text=name
            )



    def status_changed(self, event):

        status = self.status.get()



        if status == "🔴 Down":

            self.down_reason.config(
                state="readonly"
            )


        else:

            self.down_reason.set("")

            self.down_reason.config(
                state="disabled"
            )



        if status == "🟢 Running":

            self.setup_day.config(
                text=""
            )
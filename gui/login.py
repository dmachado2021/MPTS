import tkinter as tk
from tkinter import messagebox

from services.authentication import verify_login
from gui.dashboard import Dashboard


class Login:


    def __init__(self, root):

        self.root = root

        self.root.title("MPTS Administrator Login")

        self.root.geometry("400x300")


        title = tk.Label(
            root,
            text="MPTS Administrator Login",
            font=("Arial",16,"bold")
        )

        title.pack(pady=20)


        tk.Label(
            root,
            text="Username"
        ).pack()


        self.username = tk.Entry(root)

        self.username.pack()



        tk.Label(
            root,
            text="Password"
        ).pack()


        self.password = tk.Entry(
            root,
            show="*"
        )

        self.password.pack()



        tk.Button(
            root,
            text="Login",
            width=15,
            command=self.login
        ).pack(pady=20)



    def login(self):

        username = self.username.get()

        password = self.password.get()


        if verify_login(username, password):

            self.root.destroy()

            new_window = tk.Tk()

            Dashboard(new_window)

            new_window.mainloop()


        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password"
            )
import tkinter as tk
from tkinter import Tk, ttk, messagebox

class Mainapp:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Thousandeyes Interface")

        ttk.Label(root, text="User").grid(row=0)
        ttk.Label(root, text="Token").grid(row=1)
        ttk.Label(root, text="Start Date").grid(row=2)
        ttk.Label(root, text="End Date").grid(row=3)
        ttk.Label(root, text="TestID").grid(row=4)
        ttk.Label(root, text="agendId").grid(row=5)

        self.user = tk.StringVar()
        self.token = tk.StringVar()
        self.start_time = tk.StringVar()
        self.end_time = tk.StringVar()
        self.testId = tk.StringVar()
        self.agendId = tk.StringVar()

        User_Entry = ttk.Entry(root, textvariable=self.user)
        Token_Entry = ttk.Entry(root, textvariable=self.token)
        Start_Time_Entry = ttk.Entry(root, textvariable=self.start_time)
        End_Time_Entry = ttk.Entry(root, textvariable=self.end_time)
        TestId_Entry = ttk.Entry(root, textvariable=self.testId)
        AgendId = ttk.Entry(root, textvariable=self.agendId)

        User_Entry.grid(row=0, column=1)
        Token_Entry.grid(row=1, column=1)
        Start_Time_Entry.grid(row=2, column=1)
        End_Time_Entry.grid(row=3, column=1)
        TestId_Entry.grid(row=4, column=1)
        AgendId.grid(row=5, column=1)

        submit_button = ttk.Button(root, text='Submit', command=self.save_credintals)
        submit_button.grid(row=6, column=1)

    def save_credintals(self):
        thousandeyes_json = {'User': self.user.get(), 'Token': self.token.get(), 'Start': self.start_time.get(), 'End': self.end_time.get(),
                             'TestId': self.testId.get(), 'agendId': self.agendId.get()}
        print(thousandeyes_json)
        for key,value in thousandeyes_json.items():
            if value == '':
                messagebox.showerror("Missing Values", f"The value {key} was left blank")
                return
        return thousandeyes_json

root = Tk()
Mainapp(root)
root.mainloop()
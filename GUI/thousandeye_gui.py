import tkinter as tk
from tkinter import Tk, ttk, messagebox
from api_for_thousandeyes.thousandeyes_agentid import get_agentid
from api_for_thousandeyes.thousandeyes_testid import get_testid

class MainApp:
    def __init__(self, parent):
        self.parent = parent

        parent.title("Thousandeyes Interface")
        parent['background']='#E7E7E7'

        ttk.Label(root, text="User").grid(row=0)
        ttk.Label(root, text="Token").grid(row=1)
        ttk.Label(root, text="Start Date").grid(row=2)
        ttk.Label(root, text="End Date").grid(row=3)
        ttk.Label(root, text="TestID").grid(row=4)
        ttk.Label(root, text="AgendId").grid(row=5)

        self.user = tk.StringVar()
        self.token = tk.StringVar()
        self.start_time = tk.StringVar()
        self.end_time = tk.StringVar()
        self.testId = tk.StringVar()
        self.agendId = tk.StringVar()

        user_entry = ttk.Entry(root, textvariable=self.user)
        token_entry = ttk.Entry(root, textvariable=self.token)
        start_time_entry = ttk.Entry(root, textvariable=self.start_time)
        end_time_entry = ttk.Entry(root, textvariable=self.end_time)
        testid_entry = ttk.Combobox(root, width=27, textvariable=self.testId)
        agendid_entry = ttk.Combobox(root, width=27, textvariable=self.agendId)

        testid_entry['values'] = self.get_list_of_test()
        agendid_entry['values'] = self.get_list_of_cities()

        user_entry.grid(row=0, column=1)
        token_entry.grid(row=1, column=1)
        start_time_entry.grid(row=2, column=1)
        end_time_entry.grid(row=3, column=1)
        testid_entry.grid(row=4, column=1)
        agendid_entry.grid(row=5, column=1)

        submit_button = ttk.Button(root, text='Submit', command=self.save_credentials)
        submit_button.grid(row=6, column=1)

    def save_credentials(self):
        thousandeyes_json = {'User': self.user.get(), 'Token': self.token.get(),
                             'Start': self.start_time.get(), 'End': self.end_time.get(),
                             'TestId': self.testId.get(), 'agendId': self.agendId.get()}
        print(thousandeyes_json)
        for key, value in thousandeyes_json.items():
            if value == '':
                messagebox.showerror("Missing Values", f"The value {key} was left blank")
                return
        return thousandeyes_json

    def get_list_of_cities(self):
        list_of_cities = get_agentid().get_the_data
        cities = tuple(key['agentName'] for key in list_of_cities)
        return cities

    def get_list_of_test(self):
        list_of_test = get_testid().get_the_data
        test = tuple(key['type'] for key in list_of_test)
        return test


root = Tk()
MainApp(root)
root.mainloop()

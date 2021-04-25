import tkinter as tk
from tkinter import ttk, Tk, Listbox, END

class updating_box():
    def __init__(self, list, root, gridx, gridy):

        self.list = list
        self.gridx = gridx
        self.gridy =gridy

        self.basic_frame = ttk.Frame(root)
        self.basic_frame.grid(row=self.gridx, column = self.gridy)

        self.input = tk.StringVar()
        self.input_entry = ttk.Entry(self.basic_frame, textvariable=self.input)
        self.input_entry.grid(row=0, column=1)

        self.lb = Listbox(self.basic_frame, width=20, height=4)
        self.lb.insert(0, *self.list)

        self.input_entry.bind('<KeyRelease>',lambda e: self.update_list())
        self.lb.bind('<Return>', lambda e:self.selected_item())
        self.lb.bind('<Double-Button-1>', lambda e:self.selected_item())
        self.input_entry.bind('<Button-1>',lambda e: self.show_me())
        self.input_entry.bind('<Return>', lambda e:self.hide_me())

    def hide_me(self):
        self.lb.grid_forget()
    def show_me(self):
        self.lb.grid(row = 1, column = 1)
    def update_list(self):
        temp = []
        for value in list:
            if self.input.get().lower() in value.lower():
                temp.append(value)
        self.lb.delete(0,END)
        self.lb.insert(0, *temp)
    def selected_item(self):
        for i in self.lb.curselection():
            text = self.lb.get(i)
            self.input.set(text)
        self.lb.tk_focusNext().focus()
        self.lb.grid_forget()

list = ['apple','oragne','grape','strawberry','banana','kiwi', 'dragon fruit', 'pinapple']

root = Tk()
root.geometry("400x600")
ttk.Label(root, text="User").grid(row=0)
updating_box(list, root, 0, 1)

root.mainloop()
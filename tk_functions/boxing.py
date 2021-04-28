from tkinter import ttk, Tk, Listbox, END
class updating_box():
    def __init__(self, root, widget, li, gridx, gridy):

        self.li = li
        self.widget = widget
        gridx = gridx
        gridy = gridy

        self.basic_frame = ttk.Frame(root)
        self.basic_frame.grid(row=gridx, column=gridy)

        self.input_entry = ttk.Entry(self.basic_frame, textvariable=self.widget)
        self.input_entry.grid(row=0, column=1)

        self.lb = Listbox(self.basic_frame, width=20, height=4)
        self.lb.insert(0, *self.li)

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
        temp = list(filter(lambda x: x if self.widget.get().lower() in x.lower() else '', self.li))
        self.lb.delete(0,END)
        self.lb.insert(0, *temp)
    def selected_item(self):
        for i in self.lb.curselection():
            self.widget.set(self.lb.get(i))
        self.lb.tk_focusNext().focus()
        self.lb.grid_forget()
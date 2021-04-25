import tkinter as tk
from tkinter import ttk, Tk, Listbox, END

def hide_me(event):
    lb.grid_forget()
def show_me(event):
    lb.grid(row = 1, column = 1)
def update_list(event):
    temp = []
    for value in list:
        if user.get().lower() in value.lower():
            temp.append(value)
    lb.delete(0,END)
    lb.insert(0, *temp)
def selected_item(event):
    for i in lb.curselection():
        text = lb.get(i)
        user.set(text)
    event.widget.tk_focusNext().focus()
    lb.grid_forget()

list = ['apple','oragne','grape','strawberry','banana','kiwi', 'dragon fruit', 'pinapple']

root = Tk()
root.geometry("400x600")
ttk.Label(root, text="User").grid(row=0)

basic_frame = ttk.Frame(root)
basic_frame.grid(row = 0, column = 1)


user = tk.StringVar()
user_entry = ttk.Entry(basic_frame, textvariable = user)
user_entry.grid(row = 0, column = 1)

lb = Listbox(basic_frame, width=20, height=4)
lb.insert(0, *list)



user_entry.bind('<KeyRelease>', update_list)
lb.bind('<Return>', selected_item)
lb.bind('<Double-Button-1>', selected_item)
user_entry.bind('<Button-1>', show_me)
user_entry.bind('<Return>', hide_me)
root.mainloop()
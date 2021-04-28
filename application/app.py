'''
This is a python script that run the thousndeyes applaiction interface.
The application only runs if this
'''

from tkinter import Tk
from gui.function import function

if __name__ == '__main__':
    root = Tk()
    function(root)
    root.mainloop()

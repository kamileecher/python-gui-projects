import tkinter as tk
from tkinter import ttk

# install pillow for images
from PIL import Image, ImageTk

# for nice looking font
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry ("600x400")
root.resizable(False, False)
root.title("Check Button Example")



selected_option = tk.StringVar()

def print_current_option():
    print(selected_option.get())

check_button = ttk.Checkbutton(
    root, 
    text="check me!",
    variable = selected_option,
    command=print_current_option,
    onvalue= "checked",
    offvalue="unchecked"
    
    )

check_button.pack()


root.mainloop()
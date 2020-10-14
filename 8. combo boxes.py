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
root.title("Combo boxes Example")

selected_weekday = tk.StringVar()

weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"]=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")


weekday.pack()

def handle_weekday(event):
    print("today is " , selected_weekday.get())
    selected_weekday.set("friday")
    print(weekday.current())

weekday.bind("<<ComboboxSelected>>", handle_weekday)

root.mainloop()

print(selected_weekday.get(), "was selected")
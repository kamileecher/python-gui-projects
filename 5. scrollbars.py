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
root.title("Scrollbar Example")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = tk.Text(root, height=6)
text.grid(row=0, column=0, sticky="ew")

text.insert("1.0", "Enter your name")

scroll_bar = ttk.Scrollbar(root, orient="vertical", command = text.yview)
scroll_bar.grid(row=0, column=1, sticky="ns")
text["yscrollcommand"] =scroll_bar.set
# text.pack()
root.mainloop()
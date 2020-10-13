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
root.title("Text Example")

text = tk.Text(root, height=6)
text.pack()

text.insert("1.0", "Enter your name")

text_content = text.get("1.0", "end")
print(text_content)
root.mainloop()
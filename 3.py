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
root.title("Labels Example")

# label = ttk.Label(root, text="Hello", padding=20)
# # font with 2 parameter
# label.config(font=("Segoe UI", 20))
# # pack() should always be at end
# label.pack()

image = Image.open("subs.png").resize((350,350))
photo = ImageTk.PhotoImage(image)

label = ttk.Label(root, text="My Subscriber's count :",image=photo, padding=5, compound = "right")
label.config(font=("Segoe UI", 10))
label.pack()

root.mainloop()
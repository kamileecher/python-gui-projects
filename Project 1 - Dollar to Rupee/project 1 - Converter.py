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
root.geometry ("400x150")
# root.resizable(False, False)
root.title("Dollar to Rupee Conversion")

root.columnconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding = (30,15))
main_frame.grid()

dollar_value = tk.StringVar()
rupee_value = tk.StringVar()

def calculate_rupee(*args):
    try:
        dollar = float(dollar_value.get())
        rupee = dollar*73.36
        rupee_value.set(rupee)
    except:
        pass


dollar_label = ttk.Label(main_frame, text ="Dollar : ")
dollar_input = ttk.Entry(main_frame, width = 10, textvariable=dollar_value)

rupee_label  = ttk.Label(main_frame, text="Rupee : ")
rupee_display = ttk.Label(main_frame, textvariable=rupee_value)

convert_button = ttk.Button(main_frame, text="Convert!", command=calculate_rupee)

dollar_label.grid(column=0, row=0 ,sticky="W")
dollar_input.grid(column=1, row=0 ,sticky="EW")
dollar_input.focus()


rupee_label.grid(column=0, row=1 , sticky="W")
rupee_display.grid(column=1, row=1, sticky="EW")

convert_button.grid(column=0, row=2, columnspan=2, sticky="EW")

for child in main_frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.bind("<Return>", calculate_rupee)
root.bind("<KP_Enter>", calculate_rupee)


root.mainloop()

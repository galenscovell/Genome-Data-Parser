
from tkinter import *
from tkinter import ttk


# Initial window setup
root = Tk()
root.title("Genome Data Parser")


# Main content frame, height/width determined by inner content
content_frame = ttk.Frame(root, padding=20)
content_frame.grid(column=0, row=0, sticky=(N, W, E, S))
content_frame.columnconfigure(0, weight=1)
content_frame.rowconfigure(0, weight=1)


# Label creation
content_variable = StringVar()
ex_label = ttk.Label(content_frame, anchor=CENTER, textvariable=content_variable)
content_variable.set("Enter path/to/file.csv")
ex_label.pack()


# Entry creation
file_entry = StringVar()
file_path_entry = ttk.Entry(content_frame, textvariable=file_entry, width=50)
file_path_entry.pack()


# Button creation
exit_button = ttk.Button(content_frame, text='Exit', command='')
exit_button.state(['disabled'])
exit_button.pack(side=RIGHT, padx=8, pady=8)
open_button = ttk.Button(content_frame, text='Open', command='')
open_button.pack(side=RIGHT)


root.mainloop()

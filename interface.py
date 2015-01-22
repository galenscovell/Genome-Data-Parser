
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class OpenFileWindow():
    def __init__(self, root):
        self.root = root
        self.root.title("Genome Data Parser")

        # Widgets
        self.frame = ttk.Frame(self.root, padding=20)
        self.label = ttk.Label(self.frame, anchor=CENTER, text="Choose the file to open:")
        self.entry = Text(self.frame, width=40, height=2)
        self.exit_button = ttk.Button(self.frame, text='Exit', command='', width=16)
        self.exit_button.state(['disabled'])
        self.open_button = ttk.Button(self.frame, text='Open', command='', width=16)
        # browser = askopenfilename(parent=root)

        # Layout
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.label.grid(column=1, row=1)
        self.entry.grid(column=1, row=2)
        self.open_button.grid(column=1, row=3, sticky=W)
        self.exit_button.grid(column=1, row=3, sticky=E)

        # Grid Configuration
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=3)
        self.frame.columnconfigure(1, weight=3)
        self.frame.columnconfigure(2, weight=3)
        self.frame.rowconfigure(0, weight=3)
        self.frame.rowconfigure(1, weight=3)
        self.frame.rowconfigure(2, weight=3, pad=6)
        self.frame.rowconfigure(3, weight=3, pad=6)

    def close_window(self):
        print("Nothin' yet")


class MainWindow():
    def __init__(self, root):
        self.root = root




def main():
    root = Tk()
    app = OpenFileWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
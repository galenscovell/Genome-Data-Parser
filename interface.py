
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class MainWindow():
    def __init__(self, root):
        self.root = root

        # Widgets
        self.mainframe = ttk.Frame(self.root, padding=10)

        self.consoleframe = ttk.Frame(self.mainframe, padding=10)
        self.consoleframe['borderwidth'] = 2
        self.consoleframe['relief'] = 'solid'

        self.console_label = ttk.Label(self.consoleframe, text="Console Output:")

        self.console_text = Text(self.consoleframe, width=60, height=20)

        self.button_frame = ttk.Frame(self.mainframe)
        self.button_frame['borderwidth'] = 2
        self.button_frame['relief'] = 'solid'


        self.option_label = ttk.Label(self.button_frame, text="Open some data!")

        self.exit_button = ttk.Button(self.button_frame, width=18, text='Exit', command=self.close_window)
        # self.exit_button.state(['disabled'])
        self.open_button = ttk.Button(self.button_frame, width=18, text='Open', command=self.file_browser)


        # Layout
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.consoleframe.grid(column=0, row=0, sticky=N)
        self.button_frame.grid(column=0, row=3, columnspan=3, sticky=S)

        self.console_label.grid(column=0, row=0, sticky=W)
        self.console_text.grid(column=0, row=2)

        self.option_label.grid(column=1, row=0, pady=(0, 10))
        self.open_button.grid(column=0, row=1, padx=(0, 10), sticky=W)
        self.exit_button.grid(column=2, row=1, padx=(10, 0), sticky=E)


        # Grid Configuration
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.mainframe.columnconfigure(0, weight=3)
        self.mainframe.rowconfigure(0, weight=3)
        self.mainframe.rowconfigure(1, weight=3)

        self.consoleframe.columnconfigure(0, weight=3)
        self.consoleframe.rowconfigure(0, weight=3)

        self.button_frame.columnconfigure(0, weight=3)
        self.button_frame.columnconfigure(1, weight=3)
        self.button_frame.columnconfigure(2, weight=3)
        self.button_frame.rowconfigure(0, weight=3)
        self.button_frame.rowconfigure(1, weight=3)


    def close_window(self):
        self.root.destroy()

    def file_browser(self):
        browser = askopenfilename(parent=self.root)


class FigureWindow():
    def __init__(self, root):
        self.root = root




def main():
    root = Tk()
    img = PhotoImage(file='icon.gif')
    root.call('wm', 'iconphoto', root._w, '-default', img)
    root.title('Genome Data Parser')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width, window_height = 600, 480
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))
    root.resizable(FALSE, FALSE)

    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()

from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.filedialog import askopenfilename


class MainWindow():
    def __init__(self, root):
        self.root = root
        self.custom_font = font.Font(family='Source Code Pro', size=9)

        # Widgets
        self.main_frame = ttk.Frame(self.root, padding=20)

        self.console_frame = ttk.Frame(self.main_frame)
        self.console_frame['borderwidth'] = 8
        self.console_frame['relief'] = 'solid'

        self.console_label = ttk.Label(self.console_frame, text="Console Output:")
        self.console_text = Text(self.console_frame, width=70, height=20, font=self.custom_font)
        self.console_scrollbar = ttk.Scrollbar(self.console_frame, command=self.console_text.yview)
        self.console_text.config(yscrollcommand=self.console_scrollbar.set)
        self.console_input_label = ttk.Label(self.console_frame, text="Input:")
        self.console_input = ttk.Entry(self.console_frame, width=50, font=self.custom_font)
        # self.console_input.state(['disabled'])

        self.button_frame = ttk.Frame(self.main_frame)


        self.option_text = StringVar()
        self.option_label = ttk.Label(self.button_frame, textvariable=self.option_text)
        self.update_option_label('Waiting for csv/xls/xlsx file to begin...')

        self.exit_button = ttk.Button(self.button_frame, width=18, text='Exit', command=self.close_window)
        # self.exit_button.state(['disabled'])
        self.open_button = ttk.Button(self.button_frame, width=18, text='Open', command=self.file_browser)
        self.save_button = ttk.Button(self.button_frame, width=18, text='Save', command=self.save_output)


        # Layout
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.console_frame.grid(column=0, row=0, sticky=N)
        self.button_frame.grid(column=0, row=3, columnspan=3, sticky=S)

        self.console_label.grid(column=0, row=0, sticky=W)
        self.console_text.grid(column=0, row=1)
        self.console_scrollbar.grid(column=1, row=1, sticky=NS)
        self.console_input_label.grid(column=0, row=2, pady=6, sticky=W)
        self.console_input.grid(column=0, row=2, pady=6)

        self.option_label.grid(column=1, row=0, pady=(0, 10))
        self.exit_button.grid(column=2, row=1, sticky=E)
        self.open_button.grid(column=1, row=1, padx=(20, 20))
        self.save_button.grid(column=0, row=1, sticky=W)


        # Grid Configuration
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.rowconfigure(0, weight=3)
        self.main_frame.rowconfigure(1, weight=3)

        self.console_frame.columnconfigure(0, weight=3)
        self.console_frame.columnconfigure(1, weight=3)
        self.console_frame.rowconfigure(0, weight=3)
        self.console_frame.rowconfigure(1, weight=3)
        self.console_frame.rowconfigure(2, weight=3)

        self.button_frame.columnconfigure(0, weight=3)
        self.button_frame.columnconfigure(1, weight=3)
        self.button_frame.columnconfigure(2, weight=3)
        self.button_frame.rowconfigure(0, weight=3)
        self.button_frame.rowconfigure(1, weight=3)


        # Key bindings
        root.bind("<Return>", lambda x: self.update_console())


    def update_option_label(self, textvar):
        self.option_text.set(textvar)

    def close_window(self):
        self.root.destroy()

    def file_browser(self):
        data_file = askopenfilename(parent=self.root)
        if data_file.endswith('.csv'):
            print("File ends with csv.")
        elif data_file.endswith('.xls') or data_file.endswith('.xlsx'):
            print("File ends with xls or xlsx.")
        else:
            print("File extension needs to be .csv, .xls, or .xlsx")

    def save_output(self):
        print("Nothin' yet!")

    def update_console(self):
        message = self.console_input.get()
        if message:
            self.console_text.insert(END, "\n"+message)
            self.console_input.delete(0, END)





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
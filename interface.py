
from cmd_parser import DataParser
from tkinter import *
from tkinter import ttk, font, messagebox
from tkinter.filedialog import askopenfilename
import time, os.path


class MainWindow():

    def __init__(self, root, parser):
        self.root = root
        self.parser = parser
        self.custom_font = font.Font(family='Source Code Pro', size=9)


        # -------------------------------------------------- #
        # -                    Widgets                     - #
        # -------------------------------------------------- #
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.console_frame = ttk.Frame(self.main_frame)
        self.console_frame['borderwidth'] = 20
        self.console_frame['relief'] = 'solid'
        self.button_frame = ttk.Frame(self.main_frame)


        self.console_label = ttk.Label(self.console_frame, text="Console Output:")
        self.console_text = Text(self.console_frame, width=70, height=20, font=self.custom_font)
        self.console_scrollbar = ttk.Scrollbar(self.console_frame, command=self.console_text.yview)
        self.console_text.config(yscrollcommand=self.console_scrollbar.set)
        self.input_label = StringVar()
        self.console_input_label = ttk.Label(self.console_frame, textvariable=self.input_label)
        self.console_input = ttk.Entry(self.console_frame, width=50, font=self.custom_font)
        self.update_input_label('User Input:', 'disabled')
        self.console_text.insert(END, "[ Parser Ready ]" + (" " * 44) + time.strftime("%d/%m/%Y"))
        self.console_text.insert(END, "\n" + "-" * 70)
        self.console_text.insert(END, "\nWaiting for csv/xls/xlsx file...")
        self.console_text.config(state=DISABLED)


        self.exit_button = ttk.Button(self.button_frame, width=18, text='Exit', command=self.close_window)
        self.open_button = ttk.Button(self.button_frame, width=18, text='Open', command=self.file_browser)
        self.save_button = ttk.Button(self.button_frame, width=18, text='Save', command=self.save_output)



        # -------------------------------------------------- #
        # -                     Layout                     - #
        # -------------------------------------------------- #
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.console_frame.grid(column=0, row=0, sticky=N)
        self.button_frame.grid(column=0, row=3, columnspan=3, sticky=S)


        self.console_label.grid(column=0, row=0, sticky=W)
        self.console_text.grid(column=0, row=1)
        self.console_scrollbar.grid(column=1, row=1, sticky=NS)
        self.console_input_label.grid(column=0, row=2, pady=(20, 0), sticky=W)
        self.console_input.grid(column=0, row=2, pady=(20, 0))


        self.exit_button.grid(column=2, row=0, sticky=E)
        self.open_button.grid(column=1, row=0, padx=(20, 20))
        self.save_button.grid(column=0, row=0, sticky=W)



        # -------------------------------------------------- #
        # -               Grid Configuration               - #
        # -------------------------------------------------- #
        self.root.columnconfigure(0, weight=3)
        self.root.rowconfigure(0, weight=3)

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



        # -------------------------------------------------- #
        # -                  Key Bindings                  - #
        # -------------------------------------------------- #
        # root.bind('<Return>', lambda x: # User input to console)
        root.bind('<Escape>', self.close_window)
        root.protocol('WM_DELETE_WINDOW', self.close_window)



    def update_input_label(self, textvar, state):
        self.input_label.set(textvar)
        self.console_input.state([state])

    def update_option_label(self, textvar):
        self.option_text.set(textvar)

    def close_window(self, event=0):
        if messagebox.askyesno(message='Are you sure you want to quit? Any unsaved results will be lost.', title='Close Parser', icon='info'):
            self.root.destroy()

    def file_browser(self):
        data_file = askopenfilename(parent=self.root, filetypes=(("CSV files", "*.csv"),("Excel files", "*.xls;*.xlsx")))
        allowed_types = ('.csv', '.xls', '.xlsx')
        if data_file.endswith(allowed_types):
            self.parser.check_file(data_file)
            load_message = "File loaded: " + os.path.basename(data_file)
            self.update_console(load_message)
        elif not data_file:
            pass
        else:
            self.update_console("File extension must be .csv, .xls, or .xlsx")

    def save_output(self):
        print("Nothin' yet!")

    def update_console(self, output):
        self.console_text.config(state=NORMAL)
        self.console_text.insert(END, "\n" + output)
        self.console_input.delete(0, END)
        self.console_text.config(state=DISABLED)



def create_interface():
    root = Tk()
    
    img = PhotoImage(file='assets/icon.gif')
    root.call('wm', 'iconphoto', root._w, '-default', img)
    root.title('Genome Data Parser')

    screen_x = root.winfo_screenwidth()
    screen_y = root.winfo_screenheight()
    window_x, window_y = 600, 480
    x_pos = (screen_x / 2) - (window_x / 2)
    y_pos = (screen_y / 2) - (window_y / 2)
    root.geometry('%dx%d+%d+%d' % (window_x, window_y, x_pos, y_pos))
    root.resizable(FALSE, FALSE)
    return root





def main():
    root = create_interface()
    parser = DataParser()
    app = MainWindow(root, parser)
    root.mainloop()


if __name__ == '__main__':
    main()
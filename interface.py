
from cmd_parser import DataParser
from tkinter import *
from tkinter import ttk, font, messagebox
from tkinter.filedialog import askopenfilename
import sys, os.path, time


class MainWindow():

    def __init__(self, root, parser):
        self.root = root
        self.parser = parser
        self.custom_font = font.Font(family='Source Code Pro', size=9)


        # -------------------------------------------------- #
        # -                    Widgets                     - #
        # -------------------------------------------------- #
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.console_frame = ttk.Frame(self.main_frame)
        self.console_frame['borderwidth'] = 20
        self.console_frame['relief'] = 'solid'
        self.btn_frame = ttk.Frame(self.main_frame)


        self.console_label = ttk.Label(self.console_frame, text='Console Output:')
        self.console_text = Text(self.console_frame, width=70, height=20, font=self.custom_font, wrap=WORD)
        self.console_scrollbar = ttk.Scrollbar(self.console_frame, command=self.console_text.yview)
        self.console_text.config(yscrollcommand=self.console_scrollbar.set)
        self.console_text.insert(END, 'Transcriptome Data Parser' + (' ' * 35) + time.strftime('%d/%m/%Y'))

        self.options_list = StringVar()
        self.options_box = Listbox(self.console_frame, height=8, width=50, listvariable=self.options_list)
        self.options_scrollbar = ttk.Scrollbar(self.console_frame, command=self.options_box.yview)
        self.options_box.config(yscrollcommand=self.options_scrollbar.set)

        self.console_text.insert(END, '\n' + ('-' * 70))
        self.console_text.insert(END, '\nWaiting for csv/xls/xlsx file...')
        self.console_text.config(state=DISABLED)
        self.console_text.tag_configure('green', foreground='green')


        self.exit_btn = ttk.Button(self.btn_frame, width=18, text='Exit', command=self.close_window)
        self.open_btn = ttk.Button(self.btn_frame, width=18, text='Open', command=self.file_browser)
        self.save_btn = ttk.Button(self.btn_frame, width=18, text='Save', command=self.save_output)



        # -------------------------------------------------- #
        # -                     Layout                     - #
        # -------------------------------------------------- #
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.console_frame.grid(column=0, row=0, sticky=N)
        self.btn_frame.grid(column=0, row=3, columnspan=3, pady=10, sticky=S)


        self.console_label.grid(column=0, row=0, sticky=W)
        self.console_text.grid(column=0, row=1)
        self.console_scrollbar.grid(column=1, row=1, sticky=NS)
        self.options_box.grid(column=0, row=2, columnspan=2, pady=(10, 0))
        self.options_scrollbar.grid(column=1, row=2, sticky=NS)

        self.exit_btn.grid(column=2, row=0, sticky=E)
        self.open_btn.grid(column=1, row=0, padx=(20, 20))
        self.save_btn.grid(column=0, row=0, sticky=W)



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

        self.btn_frame.columnconfigure(0, weight=3)
        self.btn_frame.columnconfigure(1, weight=3)
        self.btn_frame.columnconfigure(2, weight=3)
        self.btn_frame.rowconfigure(0, weight=3)



        # -------------------------------------------------- #
        # -                  Key Bindings                  - #
        # -------------------------------------------------- #
        self.root.protocol('WM_DELETE_WINDOW', self.close_window)



    def close_window(self):
        if messagebox.askyesno(message='Are you sure you want to quit? Any unsaved results will be lost.', title='Close Parser', icon='info'):
            self.root.destroy()
            sys.exit()

    def save_output(self):
        print('Nothin\' yet!')

    def update_console(self, output, tag=None):
        self.console_text.config(state=NORMAL)
        self.console_text.insert(END, '\n' + output, tag)
        self.console_text.config(state=DISABLED)

    def file_browser(self):
        datafile = askopenfilename(parent=self.root, filetypes=(('CSV files', '*.csv'),('Excel files', '*.xls;*.xlsx')))
        allowed_types = ('.csv', '.xls', '.xlsx')
        if datafile.endswith(allowed_types):
            dataframe = self.parser.check_file(datafile)
            load_message = '\nFile loaded: ' + os.path.basename(datafile) + ' (' + str(len(dataframe)) + ' rows in file)'
            self.update_console(load_message)
            self.program_main(dataframe)
        elif not datafile:
            pass
        else:
            self.update_console('File extension must be .csv, .xls, or .xlsx')

    def program_main(self, df):
        running = True
        while running:
            choice = ' '
            self.update_console('Options: Keyword Search, Scan Column Composition', 'green')
            self.options_list.set(('Keyword Search', 'Scan Column Composition'))
            while len(choice) == 0 or choice[0].lower() not in ('c', 'k'):
                choice = input(' > ')
                if len(choice) > 0:
                    if choice[0].lower() == 'c':
                        column = self.parser.pick_column(df)
                        self.parser.scan_column(df, column)
                    elif choice[0].lower() == 'k':
                        column = self.parser.pick_column(df)
                        term = self.parser.term_prompt()
                        self.parser.search_keyword(df, column, term, len(df))



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
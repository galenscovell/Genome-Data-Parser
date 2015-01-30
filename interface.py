
import sys, os.path, time, xlrd

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import ttk, font, messagebox


class MainWindow():

    def __init__(self, root):
        self.root = root
        self.regular_font = font.Font(family='DejaVu Sans Mono', size=10)
        self.dataframe = ''
        self.state = ''


        # -------------------------------------------------- #
        # -                    Widgets                     - #
        # -------------------------------------------------- #
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.console_frame = ttk.Frame(self.main_frame)
        self.console_frame['borderwidth'] = 12
        self.console_frame['relief'] = 'groove'
        self.btn_frame = ttk.Frame(self.main_frame)

        self.console_label = ttk.Label(self.console_frame, text='Console Output:')
        self.current_file = StringVar()
        self.current_label = ttk.Label(self.console_frame, textvariable=self.current_file)
        self.current_file.set('No file loaded.')
        self.console_text = Text(self.console_frame, width=70, height=20, font=self.regular_font, wrap=WORD, fg='#2c3e50')
        self.console_scrollbar = ttk.Scrollbar(self.console_frame, command=self.console_text.yview)
        self.console_text.config(yscrollcommand=self.console_scrollbar.set)
        self.console_text.insert(END, 'Transcriptome Data Parser' + (' ' * 35) + time.strftime('%d/%m/%Y'))

        self.search_input = ttk.Entry(self.console_frame, width=40)
        self.search_input.config(state=DISABLED)
        self.options_list = StringVar()
        self.options_box = Listbox(self.console_frame, height=8, width=50, listvariable=self.options_list, activestyle='none', selectbackground='#2ecc71', font=self.regular_font)
        self.options_scrollbar = ttk.Scrollbar(self.console_frame, command=self.options_box.yview)
        self.options_box.config(yscrollcommand=self.options_scrollbar.set)

        self.console_text.insert(END, '\n' + ('-' * 70))
        self.console_text.insert(END, '\nReady, Waiting for csv/xls/xlsx file...')
        self.console_text.config(state=DISABLED)
        self.console_text.tag_configure('green', foreground='#27ae60')
        self.console_text.tag_configure('blue', foreground='#2980b9')

        self.exit_btn = ttk.Button(self.btn_frame, width=18, text='Close Parser', command=self.close_window)
        self.open_btn = ttk.Button(self.btn_frame, width=18, text='Open Data', command=self.file_browser)
        self.save_btn = ttk.Button(self.btn_frame, width=18, text='Save to CSV', command=self.save_output)
        self.save_btn.config(state=DISABLED)


        # -------------------------------------------------- #
        # -                     Layout                     - #
        # -------------------------------------------------- #
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.console_frame.grid(column=0, row=0, sticky=N)
        self.btn_frame.grid(column=0, row=3, columnspan=3, pady=10, sticky=S)

        self.console_label.grid(column=0, row=0, sticky=W)
        self.current_label.grid(column=0, row=0, sticky=E, ipady=10)
        self.console_text.grid(column=0, row=1)
        self.console_scrollbar.grid(column=1, row=1, sticky=NS)
        self.search_input.grid(column=0, row=2, pady=4, ipady=10, columnspan=2)
        self.options_box.grid(column=0, row=3, columnspan=2)
        self.options_scrollbar.grid(column=1, row=3, sticky=NS)

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
        self.console_frame.rowconfigure(3, weight=3)

        self.btn_frame.columnconfigure(0, weight=3)
        self.btn_frame.columnconfigure(1, weight=3)
        self.btn_frame.columnconfigure(2, weight=3)
        self.btn_frame.rowconfigure(0, weight=3)


        # -------------------------------------------------- #
        # -                  Key Bindings                  - #
        # -------------------------------------------------- #
        self.root.protocol('WM_DELETE_WINDOW', self.close_window)
        self.options_box.bind('<Double-Button-1>', self.select_list_item)
        self.options_box.bind('<Return>', self.select_list_item)
        self.search_input.bind('<Return>', self.get_search_input)
        



    # -------------------------------------------------- #
    # -                GUI Functions                   - #
    # -------------------------------------------------- #
    def close_window(self):
        # Popup message on exit attempts
        if messagebox.askyesno(message='Are you sure you want to quit? Any unsaved results will be lost.', title='Close Parser', icon='info'):
            self.root.destroy()
            sys.exit()


    def save_output(self):
        # Open save file dialog, automatically set extension to csv
        # After output, reset program to initial state
        file_path = filedialog.asksaveasfile(mode='w', defaultextension='.csv')
        self.dataframe.to_csv(file_path)
        self.dataframe = ''
        self.state = ''
        self.save_btn.config(state=DISABLED)
        self.options_list.set('')
        self.current_file.set('No file loaded.')
        self.update_console('\n\nData saved.', 'green')
        self.update_console('-' * 70)
        self.update_console('Ready, Waiting for csv/xls/xlsx file...')


    def update_console(self, output, tag=None):
        # Handle text display for console widget
        self.console_text.config(state=NORMAL)
        self.console_text.insert(END, '\n' + output, tag)
        self.console_text.see(END)
        self.console_text.config(state=DISABLED)


    def select_list_item(self, event):
        # Handle user selection within listbox widget depending on program state
        widget = event.widget
        selection = widget.curselection()
        if len(selection) > 0:
            value = widget.get(selection[0])
            self.update_console(' > ' + value, 'green')
            if self.state == 'beginning':
                if value == 'Scan Column Composition':
                    self.state = 'column_for_scan'
                    self.pick_column(self.dataframe)
                elif value == 'Keyword Search':
                    self.state = 'column_for_keyword'
                    self.pick_column(self.dataframe)
            else:
                self.column_choice = value
                self.options_list.set('')
                if self.state == 'column_for_scan':
                    self.scan_column(self.dataframe)
                    self.program_begin()
                elif self.state == 'column_for_keyword':
                    self.term_prompt()


    def get_search_input(self, event):
        # Collect user search term while entry is enabled
        self.search_term = self.search_input.get()
        self.search_input.delete(0, END)
        self.search_input.config(state=DISABLED)
        self.update_console(' > ' + self.search_term, 'green')
            

    def file_browser(self):
        # Open file browser, allow selection of csv/xls/xlsx only
        if len(self.dataframe) == 0:
            self.data_file = filedialog.askopenfilename(parent=self.root, filetypes=(('CSV files', '*.csv'),('Excel files', '*.xls;*.xlsx')))
            allowed_types = ('.csv', '.xls', '.xlsx')
            if self.data_file.endswith(allowed_types):
                self.dataframe = self.create_dataframe(self.data_file)
                load_message = '\nFile loaded: ' + os.path.basename(self.data_file) + ' (' + str(len(self.dataframe)) + ' rows in file)'
                self.update_console(load_message)
                self.current_file.set('File in use: ' + os.path.basename(self.data_file))
                self.save_btn.config(state=NORMAL)
                self.program_begin()
            elif not self.data_file:
                pass
            else:
                # If user somehow breaks it (as is their wont)
                self.update_console('File extension must be .csv, .xls, or .xlsx')
        else:
            # If dataframe currently loaded, confirmation to close and open new
            if messagebox.askyesno(message='Open new data? This will cause previous unsaved data to be lost.', title='Open New', icon='info'):
                self.dataframe = ''
                self.file_browser()


    def program_begin(self):
        # Greet user with initial options and set program state
        self.update_console('Select [Keyword Search] or [Scan Column Composition]', 'blue')
        self.options_list.set(('Keyword Search', 'Scan Column Composition'))
        self.state = 'beginning'



    # -------------------------------------------------- #
    # -                Parser Functions                - #
    # -------------------------------------------------- #
    def create_dataframe(self, data_file):
        # Create dataframe via different methods depending on extension type
        if data_file.endswith('.csv'):
            dataframe = pd.read_csv(data_file, header=0)
        elif data_file.endswith('.xls') or data_file.endswith('.xlsx'):
            dataframe = pd.read_excel(data_file, header=0)
        return dataframe


    def pick_column(self, df):
        # Create list of column headers within df and push them to listbox
        header_info = list(df)
        header_message = ', '.join(list(df))
        self.update_console('\nSelect Column of Interest', 'blue')
        self.update_console(header_message)
        self.options_list.set(tuple(header_info))


    def term_prompt(self):
        # Enable entry widget and set program to wait for user search term
        self.update_console('\nEnter Search Term Below (Case-Sensitive)', 'blue')
        self.search_input.config(state=NORMAL)
        self.search_input.focus()
        self.state = ''


    def scan_column(self, df):
        # Scan for all unique elements in column and push them to chart creation
        column_total = []
        column_unique = []
        for row in df[self.column_choice]:
            if row not in column_total:
                column_unique.append(row)
            column_total.append(row)
        self.create_graph(column_unique, column_total)


    def create_graph(self, analyzed, total):
        # Pie chart creation and output
        labels = []
        sizes = []
        colors = ['#f1c40f', '#2ecc71', '#1abc9c', '#e74c3c', '#9b59b6', '#e67e22']
        if type(analyzed) is list:
            for element in analyzed:
                percentage = (total.count(element) / len(total)) * 100
                title = element + ': ' + str(round(percentage, 2)) + '%'
                labels.append(title)
                sizes.append(percentage)
        else:
            percentage = (analyzed / total) * 100
            labels = ['Searched: ' + str(round(percentage, 2)) + '%', 'Remaining: ' + str(round(100 - percentage, 2)) + '%']
            sizes = [percentage, 100 - percentage]
        patches, texts = plt.pie(sizes, colors=colors, startangle=0)
        plt.legend(patches, labels, loc='best')
        plt.axis('equal')
        plt.tight_layout()
        plt.ion()
        plt.show()
        self.update_console('\nChart Output ------------------------------\n', 'green')






def create_interface():
    # Init GUI root; set icon, dimensions and properties
    root = Tk()
    
    img = PhotoImage(file='assets/icon.gif')
    root.call('wm', 'iconphoto', root._w, '-default', img)
    root.title('Genome Data Parser')

    screen_x = root.winfo_screenwidth()
    screen_y = root.winfo_screenheight()
    window_x, window_y = 640, 580
    x_pos = (screen_x / 2) - (window_x / 2)
    y_pos = (screen_y / 2) - (window_y / 2)
    root.geometry('%dx%d+%d+%d' % (window_x, window_y, x_pos, y_pos))
    root.resizable(FALSE, FALSE)
    return root


def main():
    root = create_interface()
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
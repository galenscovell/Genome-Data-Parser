

# This is the parser component for the GUI, interface.py.
# Not to be used on its own!


import sys, os.path, xlrd, time
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt



class DataParser():

    def check_file(self, data_file): 
        if data_file.endswith('.csv'):
            dataframe = pd.read_csv(data_file, header=0)
        elif data_file.endswith('.xls') or data_file.endswith('.xlsx'):
            dataframe = pd.read_excel(data_file, header=0)
        print("Why, yes.")
        return dataframe

    def file_output(self, final_df):
        save_name = ""
        while len(save_name) == 0:
            save_name = input("\n\tSave file as: ")
        save_path = "results/" + time.strftime("%d_%m_%Y") + "/"
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file_path = save_path + save_name + ".csv"
        final_df.to_csv(file_path)

    def create_graph(self, analyzed, total):
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

        plt.rcParams['font.size'] = 9.0
        patches, texts = plt.pie(sizes, colors=colors, startangle=0)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
        print("\nChart Output-------------------------")

    def pick_column(self, df):
        # Pick column from available headers
        column_choice = " "
        header_info = list(df)
        print("\nFollowing column headers found:")
        print(header_info)
        print("\n\tColumn of interest (case-sensitive):")
        while column_choice not in header_info:
            column_choice = input("\t > ")
        return column_choice


    def scan_column(self, df, chosen_column):
        # Scan for all unique elements in column
        column_total = []
        column_unique = []
        for row in df[chosen_column]:
            if row not in column_total:
                column_unique.append(row)
            column_total.append(row)

        graph = " "
        print("\n\tCreate pie-chart with collected data (Y/N)?")
        while len(graph) == 0 or graph[0].lower() not in ('y', 'n'):
            graph = input("\t > ")
            if len(graph) > 0:
                if graph[0].lower() == 'y':
                    self.create_graph(column_unique, column_total)
                elif graph[0].lower() == 'n':
                    break

    def term_prompt(self):
        # Ask for search term of interest
        print("\n\tEnter search term (case-sensitive):")
        term = input("\t > ")
        print("")
        return term

    def search_keyword(self, df, chosen_column, search_term, total_length):
        # Return all rows with term in specified column
        row_index = -1
        row_list = []
        search_results = 0
        for row in df[chosen_column]:
            row_index += 1
            if type(row) is list and ';' in row:
                row_subarray = row.split(';')
                if search_term in row_subarray:
                    search_results += 1
                    row_list.append(row_index)
            else:
                if search_term in row:
                    search_results += 1
                    row_list.append(row_index)

        output_choice = " "
        print("\tShow output (Y/N)?")
        while len(output_choice) == 0 or output_choice[0].lower() not in ('y', 'n'):
            output_choice = input("\t > ")
            if output_choice[0].lower() == 'y':
                if search_results > 0:
                    for index in row_list:
                        print("\n\n---------------------Row index:", index, "---------------")
                        print(df.irow(index))
                    print("\n\n[", search_results, "results found for '" + search_term + "' in '" + chosen_column + "' ]")
                    # print("\tIndices:", row_list)
                else:
                    print("\n\n[ No results found for '" + search_term + "' in '" + chosen_column + "']")
            elif output_choice[0].lower() == 'n':
                break

        searched_data = []
        for index in row_list:
            searched_data.append(df.irow(index))
        new_df = pd.DataFrame(data=searched_data)

        graph = " "
        print("\n\tCreate pie-chart with collected data (Y/N)?")
        while len(graph) == 0 or graph[0].lower() not in ('y', 'n'):
            graph = input("\t > ")
            if len(graph) > 0:
                if graph[0].lower() == 'y':
                    self.create_graph(search_results, total_length)
                elif graph[0].lower() == 'n':
                    break

        refine = " "
        print("\n\t[S]ave this data or [R]efine?")
        while len(refine) == 0 or refine[0].lower() not in ('s', 'r'):
            refine = input("\t > ")
            if len(refine) > 0:
                if refine[0].lower() == 's':
                    self.file_output(new_df)
                elif refine[0].lower() == 'r':
                    new_column = self.pick_column(new_df)
                    new_t = self.term_prompt()
                    self.search_keyword(new_df, new_column, new_t, total_length)
        print("\n-------------------------")

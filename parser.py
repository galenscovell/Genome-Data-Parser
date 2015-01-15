'''
TODO:
[X] 1. Search rows by column
    [X] a. Using sub-array terms
    [X] b. Filter by further search terms (refinement)
    [X] c. Output results as CSV

[.] 2. Scan composition of columns
    [X] a. Pie-chart creation
    [ ] b. Ratio of rows containing keyword within column
        [ ] i. Using subarray terms
    [ ] c. Output figures

[ ] 3. Cmdline interface -> GUI
[ ] 4. Create packaged executable for easy use across systems
'''

import sys, os.path, xlrd, time
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt




def filePrompt():
    # Ask for file path, check that file exists
    file_path = input("Enter the file path ('path/to/file.csv'): ")
    if os.path.exists(file_path):
        return file_path
    else:
        print("\tUnable to locate file.\n")
        sys.exit()


def fileOutput(final_df):
    save_name = input("\n\tFile name for output: ")
    file_path = "results/" + time.strftime("%d_%m_%Y__") + save_name + ".csv"
    final_df.to_csv(file_path)
    print("\n-------------------------")


def createGraph(analyzed, total):
    # Pie-chart output init
    labels = []
    sizes = []
    colors = ['#2ecc71', '#f1c40f', '#1abc9c', '#e74c3c', '#9b59b6', '#e67e22']
    explode = []

    # Create 'explode' pie piece effect
    for n in analyzed:
        explode.append(0.05)

    # Fill pie-chart output with ratios of column of interest
    for element in analyzed:
        percentage = total.count(element) / len(total) * 100
        labels.append(element)
        sizes.append(percentage)

    # Display completed pie-chart
    plt.rcParams['font.size'] = 9.0
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()
    print("\n-------------------------")


def pickColumn(df):
    # Pick column from available headers
    column_choice = " "
    header_info = list(df)
    print("\nFollowing column headers found:")
    print(header_info)
    print("\n\tColumn of interest:")
    while column_choice not in header_info:
        column_choice = input("\t > ")
    return column_choice


def scanColumn(df, chosenColumn):
    # Scan for all unique elements in column
    column_total = []
    column_unique = []
    for row in df[chosenColumn]:
        if row not in column_total:
            column_unique.append(row)
        column_total.append(row)

    graph = " "
    print("\n\tCreate pie-chart with collected data (Y/N)?")
    while len(graph) == 0 or graph[0].lower() not in ('y', 'n'):
        graph = input("\t > ")
        if len(graph) > 0:
            if graph[0].lower() == 'y':
                createGraph(column_unique, column_total)
            elif graph[0].lower() == 'n':
                break


def termPrompt():
    # Ask for search term of interest
    print("\n\tEnter search term")
    term = input("\t > ")
    print("")
    return term


def searchKeyword(df, chosenColumn, search):
    row_index = -1
    row_list = []
    results = 0
    for row in df[chosenColumn]:
        row_index += 1
        if ';' in row:
            row_subarray = row.split(';')
            if search in row_subarray:
                results += 1
                row_list.append(row_index)
        else:
            if search in row:
                results += 1
                row_list.append(row_index)

    if results > 0:
        for index in row_list:
            print("\n\n\t---------------Row index:", index, "---------------")
            print(df.irow(index))
        print("\n\n[", results, "results found for '" + search + "' in '" + chosenColumn + "' ]")
        print("\tIndices:", row_list)
    else:
        print("\n\n[ No results found for '" + search + "' in '" + chosenColumn + "']")

    searched_data = []
    for index in row_list:
        searched_data.append(df.irow(index))
    new_df = pd.DataFrame(data=searched_data)

    refine = " "
    print("\n\tOutput this data or further refine?")
    print("\t(Options: [O]utput or [R]efine)")
    while len(refine) == 0 or refine[0].lower() not in ('o', 'r'):
        refine = input("\t > ")
        if len(refine) > 0:
            if refine[0].lower() == 'o':
                fileOutput(new_df)
            elif refine[0].lower() == 'r':
                new_column = pickColumn(new_df)
                new_t = termPrompt()
                searchKeyword(new_df, new_column, new_t)

    print("\n-------------------------")
    
    


def main():
    f = filePrompt()

    print("\n____________[ GENOMIC DATA PARSER ]____________\n")
    if f.endswith('.csv'):
        dataframe = pd.read_csv(f, header=0)
    elif f.endswith('.xls') or f.endswith('.xlsx'):
        dataframe = pd.read_excel(f, header=0)
    else:
        print("\tFile extension needs to be .csv, .xls, or .xlsx")
        sys.exit()

    running = True
    while running:
        choice = " "
        print("\nFILE IN USE: " + f + " (" + str(len(dataframe)) + " rows)")
        print("(Options: Scan [C]olumns, Search [K]eyword, [E]xit)")
        while len(choice) == 0 or choice[0].lower() not in ('c', 'k', 'e'):
            choice = input(" > ")
            if len(choice) > 0:
                if choice[0].lower() == 'c':
                    column = pickColumn(dataframe)
                    scanColumn(dataframe, column)
                elif choice[0].lower() == 'k':
                    column = pickColumn(dataframe)
                    t = termPrompt()
                    searchKeyword(dataframe, column, t)
                elif choice[0].lower() == 'e':
                    running = False
                    break


    print("\n______________[ CLOSING PARSER ]______________\n")
    sys.exit()


if __name__ == '__main__':
    main()
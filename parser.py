'''
TODO:
[X] 1. Find composition of columns as percentages
    [X] a. Pie-chart representation
    [ ] b. Using subarray terms
        [ ] i. Visual representation of results
[X] 2. Find individual row by search term
    [ ] a. Using subarray terms
    [ ] b. Filter by further search terms
[ ] 3. Search by column, filter results with further search terms
    [ ] a. Using subarray terms
[ ] 4. Output results (as CSV) and figures with date/time
[ ] 5. Cmdline interface -> GUI
[ ] 6. Create packaged executable for easy use across systems
'''

import sys, os.path, xlrd
import pandas as pd
import matplotlib.pyplot as plt



def filePrompt():
    # Ask for file path, check that file exists
    file_path = input("Enter the file path ('path/to/file.csv'): ")
    if os.path.exists(file_path):
        return file_path
    else:
        print("Unable to locate file.\n")
        sys.exit()


def scanColumn(df):
    # Scan for unique elements in column
    column_entry = " "
    header_info = list(df)
    while column_entry not in header_info:
        print("\nFollowing column headers found:")
        print(header_info)
        print("\nEnter the column header to return info on")
        column_entry = input(" > ")
    column_list = []
    column_unique = []
    for row in df[column_entry]:
        if row not in column_list:
            column_unique.append(row)
        column_list.append(row)
    
    # Pie-chart output init
    labels = []
    sizes = []
    colors = ['#2ecc71', '#f1c40f', '#1abc9c', '#e74c3c', '#9b59b6', '#e67e22']
    explode = []

    # Create 'explode' pie piece effect
    for n in column_unique:
        explode.append(0.05)

    # Fill pie-chart output with ratios of column of interest
    for element in column_unique:
        percentage = column_list.count(element) / len(column_list) * 100
        labels.append(element)
        sizes.append(percentage)

    # Show completed pie-chart
    plt.rcParams['font.size'] = 9.0
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()
    print("\n---------------------")


def termPrompt():
    # Ask for search term of interest
    print("\nEnter the term to return info on")
    term = input(" > ")
    return term


def searchRow(df, search):
    # Return rows with term anywhere in columns
    for column in df.columns:
        if len(df[df[column] == search]) > 0:
            print(df[df[column] == search])
    print("\n---------------------")
    
    


def main():
    f = filePrompt()

    print("\n____________[ PYTHON DATA PARSER ]____________\n")
    if f.endswith('.csv'):
        dataframe = pd.read_csv(f, header=0)
    elif f.endswith('.xls') or f.endswith('.xlsx'):
        dataframe = pd.read_excel(f, header=0)
    else:
        print("File extension needs to be .csv, .xls, or .xlsx")
        sys.exit()

    running = True
    while running:
        choice = " "
        print("\nFILE IN USE: " + f)
        print("(Options: Scan [C]olumns, Search [R]ows, [E]xit)")
        while choice[0].lower() != 'c' and choice[0].lower() != 'r':
            choice = input(" > ")
            if choice[0].lower() == 'c':
                scanColumn(dataframe)
            elif choice[0].lower() == 'r':
                t = termPrompt()
                searchRow(dataframe, t)
            elif choice[0].lower() == 'e':
                running = False
                break


    print("\n______________[ CLOSING PARSER ]______________\n")
    sys.exit()


if __name__ == '__main__':
    main()
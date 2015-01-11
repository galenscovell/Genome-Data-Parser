'''
Functions to implement:
1. Find composition of columns (function, location) as percentages
    a. Create data representations
2. Find individual row by search term
3. Compare two rows next to one another by two search terms
4. Output results to file for later viewing with date/time
'''



import sys, os.path, xlrd
import pandas as pd
import matplotlib.pyplot as plt


def filePrompt():
    # Ask for file path and check that it exists
    file_path = input("Enter the file path ('path/to/file.csv'): ")
    if os.path.exists(file_path):
        return file_path
    else:
        print("Unable to locate file.\n")
        sys.exit()


def termPrompt():
    # Ask for search term of interest
    print("\nEnter the term to return info on")
    term = input(" > ")
    return term


def scanColumn(df):
    # Scan for unique elements in column, return percentage out of total
    print("\nFollowing column headers found:")
    print(df.columns)
    print("\nEnter the column header to return info on")
    column_name = input(" > ")
    column_list = []
    column_unique = []
    for row in df[column_name]:
        if row not in column_list:
            column_unique.append(row)
        column_list.append(row)
    print("\n---------------------")
    for element in column_unique:
        percentage = column_list.count(element) / len(column_list) * 100
        print(element + ": %.2f %%" % percentage)
    print("---------------------")


def searchRow(df, search):
    # Return rows with term anywhere in columns
    for column in df.columns:
        if len(df[df[column] == search]) > 0:
            print(df[df[column] == search])
    
    


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
        print("\nWhat would you like to do with the data?")
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

    sys.exit()


if __name__ == '__main__':
    main()
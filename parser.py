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
    file_path = input("Enter the file path ('path/to/file.csv'): ")
    if os.path.exists(file_path):
        return file_path
    else:
        print("Unable to locate file.\n")
        sys.exit()

def termPrompt():
    term = input("Enter the term to return info on: ")
    return term

def scanColumn(df):
    # Scan for unique elements in column, return percentage out of total
    print("\nEnter the column header to return info on.")
    columnName = input(" > ")
    column_list = []
    column_unique = []
    for row in df[columnName]:
        if row not in column_list:
            column_unique.append(row)
        column_list.append(row)
    print("\n---------------------")
    for element in column_unique:
        percentage = column_list.count(element) / len(column_list) * 100
        print(element + ": %.2f %%" % percentage)
    print("---------------------")

def fileParse(f, searchTerm):
    df = pd.read_csv(f, header=0)
    scanColumn(df)

    # All column headers
    #print(df.columns)
    # All rows with term in column
    #print(df[df.function == searchTerm])
    # All data under specific column
    #print(df.function)
   # All data from specific number of rows
    #print(df[:2])
    # Search individual element
    #for element in df.gene_name:
        #if element == searchTerm:
            #print(element)



def main():
    f = filePrompt()

    print("\n###### Python Data Parser loaded ######\n")
    if f.endswith('.csv'):
        dataframe = pd.read_csv(f, header=0)
    elif f.endswith('.xls') or f.endswith('.xlsx'):
        dataframe = pd.read_excel(f, header=0)
    else:
        print("File extension needs to be .csv, .xls, or .xlsx")
        print("\n###### Python Data Parser finished ###### \n")
        sys.exit()

    print("What would you like to do with the data?")
    print("(Options: Scan [C]olumns, Search [R]ows, [E]xit)")
    choice = ""
    while choice != 'c' and choice != 'r':
        choice = input(" > ")
        if choice[0].lower() == 'c':
            scanColumn(dataframe)
        elif choice[0].lower() == 'r':
            t = termPrompt()
            fileParse(f, t)
        else:
            break

    print("\n###### Python Data Parser finished ###### \n")


if __name__ == '__main__':
    main()
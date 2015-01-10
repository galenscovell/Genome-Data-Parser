'''
Functions to implement:
1. Find composition of columns (function, location) as percentages
    a. Create data representations
2. Find individual row by search term
3. Compare two rows next to one another by two search terms
4. Output results to file for later viewing with date/time
'''



import sys
import pandas as pd
import matplotlib.pyplot as plt


def filePrompt():
    file_path = input("Enter the file path ('path/to/file.csv'): ")
    return file_path

def termPrompt():
    term = input("Enter the term to return info on: ")
    return term

def fileParse(f, searchTerm):
    df = pd.read_csv(f, header=0)

    # Scan for unique elements in column, return percentage out of total
    function_list = []
    function_unique = []
    for row in df.function:
        if row not in function_list:
            function_unique.append(row)
        function_list.append(row)

    for element in function_unique:
        print(element, (function_list.count(element) / len(function_list)) * 100)
    

    # All rows with term in column
    print(df[df.function == searchTerm])
    # All data under specific column
    print(df.function)
    # All column headers
    print(df.columns)
    # All data from specific number of rows
    print(df[:2])
    # Search individual element
    for element in df.gene_name:
        if element == searchTerm:
            print(element)



def main():
    print("\nPython CSV Parser loaded.")
    f = filePrompt()
    t = termPrompt()
    fileParse(f, t)


if __name__ == '__main__':
    main()
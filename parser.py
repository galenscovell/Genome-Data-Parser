
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
    datafile = pd.read_csv(f, header=0)
    print(datafile[datafile['gene_name'] == searchTerm]) # Specific row
    print(datafile['function']) # Specific column



def main():
    print("\nPython CSV Parser loaded.")
    f = filePrompt()
    t = termPrompt()
    fileParse(f, t)


if __name__ == '__main__':
    main()
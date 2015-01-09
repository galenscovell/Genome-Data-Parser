
import csv, sys


def filePrompt():
    file_path = input("Enter the file path ('path/to/file.csv'): ")
    return file_path

def termPrompt():
    term = input("Enter the term to return info on: ")
    return term

def fileParse(file, searchTerm):
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            if searchTerm in row:
                print(row)

def main():
    print("\nPython CSV Parser loaded.")
    f = filePrompt()
    t = termPrompt()
    fileParse(f, t)


if __name__ == '__main__':
    main()
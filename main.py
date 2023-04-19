import csv

def open_file():
    ask = input("Enter CSV Filename: ")
    while True:
        try:
            fp = open(ask + ".csv")
            return fp
        except:
            print("\nError: File not found.")
            ask  = input("Enter CSV Filename: ")

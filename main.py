<<<<<<< HEAD
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
=======
def main():
    print("Hello World")
    print("Hello World yay screw you H")
    for i in range(10):
        print("Hello Wrld")
    #lezz go
>>>>>>> 7077890c2f8ed58c2d82fe7d4af9dfe898a0faf0

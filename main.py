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

def main():
    csv_file = open_file()
    
    if csv_file:
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            print(row)
        
        csv_file.close()
    else:
        print("Failed to open CSV file.")

if __name__ == '__main__':
    main()

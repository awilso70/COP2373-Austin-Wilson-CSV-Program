#imports csv for text files
import csv

def read_grades():
    #opens grades file in read mode
    with open("grades.csv", mode="r") as file:
        #creates object to read file
        reader = csv.reader(file)
        #reads header row and stores in header variable
        header = next(reader)
        #prints the header in a formatted way
        print(f"{header[0]:<15} {header[1]:<15} {header[2]:<10} {header[3]:<10} {header[4]:<10}")
        print("-" * 60) #seperator line
        #loops through the rows of the csv file
        for row in reader:
            #prints rows in a table format
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")

if __name__ == "__main__":
    read_grades()
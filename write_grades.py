#allows for creation of csv text file
import csv

#function for writing grades
def write_grades():
    #asks for number of students in class
    student_total = int(input("Enter number of students: "))
    #opens file in write mode and formats new lines
    with open("grades.csv", mode="w", newline="") as file:
        #create object to write data on file
        writer = csv.writer(file)
        #header row in file
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
        #loop with number of students to collect data
        for _ in range(student_total):
            full_name = input("Enter student's full name (First Last): ")
            #Split the name into first and last name
            name_parts = full_name.split()  #add space
            #ensures there are at least two parts (first and last name)
            if len(name_parts) != 2:
                print("Please enter both first and last names.")
                continue
            # Assign first and last names based on split input
            first_name, last_name = name_parts
            # collects info
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            #write student data as a row
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

#calls function
if __name__ == "__main__":
    write_grades()

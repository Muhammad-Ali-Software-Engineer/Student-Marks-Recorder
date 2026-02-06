''' Q1: Student Record System (FAST VERSION)
Features:
    Add student (name, marks)
    View students
    Find average
    Find highest marks
    Exit
Concepts used:
    dictionary
    loop
    functions
    file save & load
💡 Hint:
    reuse what you already built
    no need fancy UI
'''

students = {}
import os
if os.path.exists("students.txt"):
    with open("students.txt") as f:
        lines = f.readlines()
    for line in lines:
        name,marks = line.strip().split(":")
        students[name] = int(marks)
def ShowMenu():
    print("\n1. Add Student")
    print("2. Delete student")
    print("3. View all students")
    print("4. Find highest marks")
    print("5. Find lowest marks")
    print("6. Find average marks")
    print("7. Delete all students")
    print("0. Exit\n")
    choice = int(input("Enter choice between 0 to 7: "))
    if choice == 0:
        print("Program terminated.")
        return 
    elif choice == 1:
        AddStudent()
    elif choice == 2:
        DeleteStudent()
    elif choice == 3:
        ViewStudents()
    elif choice == 4:
        HighestMarks()
    elif choice == 5:
        LowestMarks()
    elif choice == 6:
        AverageMarks()
    elif choice == 7:
        DeleteAll()
    else:
        print("Choose between 0 to 7")
        ShowMenu()
def AddStudent():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    with open("students.txt", "a") as f:
        f.write(name+":"+ str(marks)+"\n")
    print("\nStudent added successfully!")
    ShowMenu()
# def DeleteStudent():
#     name = input("Enter student name to delete: ")
#     if name in students:
#         students.pop(name)
#         print("\nStudent deleted successfully.")
#     else:
#         print("No student to delete.")
#     ShowMenu()
# def DeleteStudent():
#     if not students:
#         print("No student available.")
#     else:
#         name = input("Enter student name to delete: ")
#         if name in students:
#             students.pop(name)
#             print("\nStudent deleted successfully.")

#             with open("students.txt","w") as f:
#                 for n,marks in students.items():
#                     f.write(n+";"+str(marks)+"\n")
#         else:
#             print("Student not found.")
def DeleteStudent():
    if not students:
        print("No student available.")
    else:
        name = input("Enter student name to delete: ")
        if name in students:
            students.pop(name)
            print("\nStudent deleted successfully.")

            with open("students.txt") as f:
                lines = f.readlines()
            with open("students.txt", "w") as f:
                for line in lines:
                    if not line.startswith(name + ":"):   # skip the deleted student
                        f.write(line)
        else:
            print("Student not found.")
    ShowMenu()
def ViewStudents():
    print("----------------------------")
    for name,marks in students.items():
        print(name,":",marks)
    print("----------------------------")
    ShowMenu()
def DeleteAll():
    students.clear()
    with open("students.txt","w") as f:
        f.write("")
    print("\nAll students deleted.")
    ShowMenu()
def HighestMarks():
    if not students:
        print("No students available")
    else:
        highest = max(students.values())
        print("----------------------------")
        print("Highest marks =",highest)
        print("----------------------------")
    ShowMenu()
def LowestMarks():
    if not students:
        print("No students available")
    else:
        lowest = min(students.values())
        print("----------------------------")
        print("Lowest marks =",lowest)
        print("----------------------------")
    ShowMenu()
def AverageMarks():
    if not students:
        print("No students available")
    else:
        total = sum(students.values())
        average = total/len(students.values())
        print("----------------------------")
        print("Average marks =",average)
        print("----------------------------")
    ShowMenu()
print("===============================")
print("     Student Record System")
print("===============================")

# print("======= Welcome =======")
# print("------- Welcome -------")
ShowMenu()
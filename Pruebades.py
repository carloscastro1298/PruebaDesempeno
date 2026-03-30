import json
import os

FILE_PATH = "students.json"


# LOAD STUDENTS
def load_students():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# SAVE STUDENTS
def save_students(students):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


# FIND STUDENT BY ID
def find_student_by_id(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


# REGISTER STUDENT
def register_student(students):
    print("===== Register Student =====")

    student_id = input("Enter student ID: ").strip()
    if student_id == "":
        print("ID cannot be empty.")
        return

    if find_student_by_id(students, student_id):
        print("Student with this ID already exists.")
        return

    name = input("Enter name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    age_text = input("Enter age: ").strip()
    if not age_text.isdigit():
        print("Age must be a number.")
        return
    age = int(age_text)

    course = input("Enter course: ").strip()

    status = input("Enter status (active/inactive): ").strip().lower()
    if status not in ("active", "inactive"):
        print("Invalid status.")
        return

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "status": status,
    }

    students.append(new_student)
    save_students(students)

    print("Student registered successfully.")


# LIST STUDENTS
def list_students(students):
    print("===== STUDENT LIST =====")

    if len(students) == 0:
        print("No students registered.")
        return

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Status: {student['status']}")
        print("-------------------------")


# SEARCH STUDENT
def search_student(students):
    print("----- Search Student -----")
    print("1. Search by ID")
    print("2. Search by Name")

    option = input("Choose an option: ").strip()

    if option == "1":
        student_id = input("Enter student ID: ").strip()
        student = find_student_by_id(students, student_id)

        if student:
            print("Student found:")
            print(student)
        else:
            print("Student not found.")

    elif option == "2":
        name = input("Enter name: ").strip().lower()
        found = False

        for student in students:
            if student["name"].lower() == name:
                print(student)
                found = True

        if not found:
            print("Student not found.")
    else:
        print("Invalid option.")


# UPDATE STUDENT
def update_student(students):
    print("----- Update Student -----")

    student_id = input("Enter student ID: ").strip()
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("Leave blank to keep current value")

    new_name = input(f"New name ({student['name']}): ").strip()
    new_age = input(f"New age ({student['age']}): ").strip()
    new_course = input(f"New course ({student['course']}): ").strip()
    new_status = input(f"New status ({student['status']}): ").strip().lower()

    if new_name != "":
        student["name"] = new_name

    if new_age != "":
        if new_age.isdigit():
            student["age"] = int(new_age)
        else:
            print("Invalid age.")

    if new_course != "":
        student["course"] = new_course

    if new_status != "":
        if new_status in ("active", "inactive"):
            student["status"] = new_status
        else:
            print("Invalid status.")

    save_students(students)
    print("Student updated successfully.")


# DELETE STUDENT
def delete_student(students):
    print("----- Delete Student -----")

    student_id = input("Enter student ID: ").strip()
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    save_students(students)

    print("Student deleted successfully.")


# MENU
def show_menu():
    print("\n====== MAIN MENU ======")
    print("1. Register student")
    print("2. List students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")


# MAIN
def main():
    students = load_students()

    option = ""
    while option != "6":
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "1":
            register_student(students)
        elif option == "2":
            list_students(students)
        elif option == "3":
            search_student(students)
        elif option == "4":
            update_student(students)
        elif option == "5":
            delete_student(students)
        elif option == "6":
            print("Goodbye")
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
def find_student_by_id(student, student_id):
    """
    Search for a student by ID.

    Returns:
    dict: student if found
    None: if not found
    """

def register_student(student):
    """"
    Register a new student:
    
    Validates that:
    -ID is unique
    -age is numeric
    -status is active or inactive
    """


print("=====Register student =====") #Headed


student_id= input("Enter the student ID"). strip() #Request the student ID
if student_id=="" #Make sure there is no empty space
print("ID cannot be empty.")
return


existing_student = find_student_by_id(student, student_id) #Check if the ID already exists
print("There is already a student with this identification.")
return

name=input("Enter the student's name").strip() #Ask for the name
if name== "" ##Make sure there is no empty space
    print("Name cannot be empty")

age_text= input("Enter client age:").strip() #Ask for the age
if not age_text. isdigit(): #Validate if number
    print("Age must be a number")
return
age= int(age_text) #Convert to integer

course= input("Enter the course")
print("Course not valid")
return

status= input("Enter status(active/inactive):")
if status not in ("active", "inactive"): 
    print("invalid status. ")

new_student={ #Create a dictionary for a new student
    "id:"student_id,
    "name": student_name,
    "age": age,
    "course": course,
    "status": status,
}

students.append(new_student) #Add new student to the list
save_students(student) #Save the list updated

print("Student registered sucessfully.")


def student_list(students)
    """
    Print all students registered
    """
    print("No students registered")

    if len (students)== 0: #If there are no students
        print("No students registered. ")
        return
    
    for students in student: #Find and display each student
        print(f"ID{student['ID']}")
        print(f"Name{student['name']}")
        print(f"Age{student['age']}")
        print(f"Course{student['course']}")
        print(f"Status{student['status']}")


def search_students(student):
    """
    Search student by ID or name
    """
    print("-----Search student-----") #Header
    print("Search by ID") #Option search by ID
    print("Search by name") #Option search by name

    option= input("Choose an option ").strip()

    if option== "1": #If you search by ID
        student_id=input("Enter student ID "). strip()
        student = find_student_by_id(student_id)

        if student is None:
            print("Student not found") #No founded
        else:
            print("Student found")
            print(student)
    
    elif option== "2" #If search by name
        name=input("Enter the student name: "). strip().lower()
        found= False

        for student in load_students
            if student["name"].lower() == name:
                print(student)
                found= True
        if not found:
            print("Student not found")
    else:
        print("Invalid option.") 


def update_student(students):
    """
    Update an exiting student by ID
    """
    print("----Update Student") #Header

    student_id= input("Enter student ID to update").strip()
    student = find_student_by_id(student)

    if student is None:
        print("student not found")
        return
    
    print("Leave blank if you do not want to change a field") #Instruction
    
    new_name= input(f"New name ({student[name]}"): #new name
    new_age= input(f"New age ({student[age]}"): #new age
    new_course= input(f"New course ({student[course]}"): #new course
    new_status= input(f"New status ({student[status]}"): #new status

    if new_name != "": #Name added sucessfully
        student["name"]=new_name
    if new_age != "": #Age added sucessfully
        if new_age.isdigit():
            student["age"]= int(new_age)
        else: 
            print("Invalid age. Age was not updated")
    if new_course != "": #If 
        student["course"]=new_course
    if new_status != "": 
        if new_status in ("active", "inactive"):
            student["status"]= new_status
        else:
            print("Invalid status. Status was not updated. ")
    
    save_students(student) #Save the changes
    print("Student updated sucessfully") #Sucessfully message


def delete_students(students):
        """
        Delete a student by ID
        """
        print("---Delete student---") #Header

        student_id=input("Enter student ID to delete"). strip() #Ask for the ID
        student=find_student_by_id(students, student_id) #Search the student

        if student is None:
            print("Student not found.") #Not found
            return
        
        student.remove(student) #Delete student for the list
        save_students(student) #Save the list updated

        print("Student deleted successfully")

def main()
            """
            MAIN PROGRAM FUNCTION
            """

            students= load_students() #Load the student list from the file
            option= ""

            while option !"6" #Main loop until you choose to exit
                show_menu() #Show the menu
                option= input("Choose an option"). strip()

                if option == "1"
                    register_student(student) #Register student
                elif option == "2"
                    list_students(student) #List students
                elif option == "3"
                    search_student(student) #Search client
                elif option == "4"
                    update_student(student) #Update student
                elif option == "5"
                    remove_students(student) #Remove student
                elif option == "6"
                    print("Goodbye")
                else:
                    print("invalid option. Please try again") #Invalid option
if __name__ == "__main__": #If the file is executed directly
    main() #Call the main function

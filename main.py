from archivos import *
from Funciones import*

def show_menu():
    print("\n====== MENU ======")
    print("1. Register student")
    print("2. List students")
    print("3. Delete students")
    print("4. Exit")


def main():
    students = load_students()

    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "1":
            register_student(students)
        elif option == "2":
            list_students(students)
        elif option == "3":
            delete_student(students)
        elif option == "4":
            print("Goodbye")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
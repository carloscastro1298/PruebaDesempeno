from archivos import *

def load_students():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_students(students):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)


def find_student_by_id(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def register_student(students):
    print("\n--- Register Student ---")

    student_id = input("ID: ").strip()
    if student_id == "":
        print("ID cannot be empty")
        return

    if find_student_by_id(students, student_id):
        print("ID already exists")
        return

    name = input("Name: ").strip()
    if name == "":
        print("Name cannot be empty")
        return

    age_text = input("Age: ").strip()
    if not age_text.isdigit():
        print("Age must be numeric")
        return
    age = int(age_text)

    course = input("Course: ").strip()

    status = input("Status (active/inactive): ").strip().lower()
    if status not in ("active", "inactive"):
        print("Invalid status")
        return

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "status": status
    }

    students.append(new_student)
    save_students(students)

    print("Student registered successfully")


def list_students(students):
    print("\n--- Student List ---")

    if not students:
        print("No students registered")
        return

    for s in students:
        print(f"ID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Course: {s['course']}")
        print(f"Status: {s['status']}")
        print("----------------------")

def delete_student(students):
    id_delete= int(input("Enter Id student delete"))
    for student in students:
        if students == id_delete: 
            students.remove(student)
            print(f"The student was delete sucessfully {"student"}")
        else:
            print("Id not found")
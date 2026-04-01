import json
import os

FILE_PATH = "students.json"

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
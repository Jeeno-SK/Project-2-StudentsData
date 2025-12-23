students = []

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")
    
    student = (sid, name, marks)
    students.append(student)
    print("✅ Student Added Successfully")

def view_students():
    if not students:
        print("No students found")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

def search_student():
    sid = input("Enter Student ID to Search: ")
    for s in students:
        if s[0] == sid:
            print("Student Found:", s)
            return
    print("❌ Student Not Found")

def update_student():
    sid = input("Enter Student ID to Update: ")
    for i in range(len(students)):
        if students[i][0] == sid:
            name = input("Enter New Name: ")
            marks = input("Enter New Marks: ")
            students[i] = (sid, name, marks)
            print("Student Updated")
            return
    print("❌ Student Not Found")

def delete_student():
    sid = input("Enter Student ID to Delete: ")
    for s in students:
        if s[0] == sid:
            students.remove(s)
            print("Student Deleted")
            return
    print("❌ Student Not Found")

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("👋 Exiting Program")
        break
    else:
        print("⚠ Invalid Choice")

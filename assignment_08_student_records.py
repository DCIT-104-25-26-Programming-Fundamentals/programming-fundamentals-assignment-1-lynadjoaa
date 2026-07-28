def calculate_average(scores):
    if len(scores) == 0:
        return 0
    total = 0
    for score in scores:
        total = total + score
    return round(total / len(scores), 2)

def add_student(students):
    name = input("Student name: ")
    id_num = input("Student ID: ")
    
    # Check if ID already exists
    for student in students:
        if student["id"] == id_num:
            print("Error: Student ID already exists.")
            return
    
    num_scores = int(input("How many scores? "))
    scores = []
    for i in range(num_scores):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)
    
    student = {
        "name": name,
        "id": id_num,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')

def display_students(students):
    if len(students) == 0:
        print("No students have been added yet.")
        return
    
    print("-----------------------------------------------------------------")
    print(f"{'Name':<15} {'ID':<10} {'Scores':<20} {'Average'}")
    print("-----------------------------------------------------------------")
    for student in students:
        scores_str = ", ".join([str(s) for s in student["scores"]])
        avg = calculate_average(student["scores"])
        print(f"{student['name']:<15} {student['id']:<10} {scores_str:<20} {avg}")
    print("-----------------------------------------------------------------")

def calculate_average_for_student(students):
    id_num = input("Enter student ID: ")
    for student in students:
        if student["id"] == id_num:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg}")
            return
    print("Error: Student ID not found.")

def show_menu():
    print("\n==================================")
    print(" STUDENT RECORD SYSTEM MENU")
    print("==================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def main():
    students = []
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter 1-4.")

main()

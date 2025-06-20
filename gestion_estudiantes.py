# Student Management
# This program allows managing student records including their grades and calculating averages.
# Modified version that requires registering 3 students at program start

# Main dictionary to store students
# Structure: {student_id: {'name': str, 'age': int, 'grades': [float]}}
students = {}
next_id = 1  # Auto-incremented ID counter for new students

def main():
    """
    Main function that first requires registering 3 students,
    then displays the menu and manages user selections.
    Continuously runs until the user chooses to exit.
    """
    # Require 3 initial student registrations
    print("\n--- Initial Setup ---")
    print("Please register 3 students to begin:")
    for i in range(3):
        print(f"\nRegistering student {i+1} of 3:")
        register_student()
    
    # Main program loop
    running = True
    while running:
        print("\n--- Student Management System ---")
        print("1. Register student")
        print("2. Consult student")
        print("3. Update grades")
        print("4. Delete student")
        print("5. List all students")
        print("6. Exit")

        option = input("Select an option: ")

        # Menu option handling
        if option == "1":
            register_student()
        elif option == "2":
            list_students_brief()  # Show brief list before consulting
            consult_student()
        elif option == "3":
            update_grades()
        elif option == "4":
            delete_student()
        elif option == "5":
            list_students()
        elif option == "6":
            print("Exiting the program...")
            running = False
        else:
            print("Invalid option. Please try again.")


def register_student():
    """
    Registers a new student in the system.
    Collects and validates student data including:
    - Auto-generated ID
    - Name
    - Age (validated between 0-120)
    - At least 3 grades (validated between 0-5)
    """
    global next_id  # Access the global ID counter
    
    print("\n--- Student Registration ---")

    # Auto-assign ID and increment counter
    student_id = str(next_id)
    next_id += 1
    print(f"Assigned Student ID: {student_id}")

    name = input("Full name: ")

    # Validate age input (must be between 0 and 120)
    while True:
        try:
            age = int(input("Age (0-120): "))
            if age < 0 or age > 120:
                print("Age must be between 0 and 120.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for age.")

    # Collect at least 3 valid grades (between 0 and 5)
    grades = []
    print("Enter at least 3 student grades (0-5):")
    while len(grades) < 3:
        try:
            grade = float(input(f"Grade {len(grades) + 1}: "))
            if grade < 0 or grade > 5:
                print("Grades must be between 0 and 5.")
                continue
            grades.append(grade)
        except ValueError:
            print("Please enter a valid number for the grade.")

    # Optional: Allow adding more grades
    while True:
        more = input("Add another grade? (y/n): ").lower()
        if more == 'n':
            break
        elif more == 'y':
            try:
                grade = float(input(f"Grade {len(grades) + 1}: "))
                if grade < 0 or grade > 5:
                    print("Grades must be between 0 and 5.")
                    continue
                grades.append(grade)
            except ValueError:
                print("Please enter a valid number for the grade.")
        else:
            print("Please enter 'y' or 'n'.")

    # Store the student data in the dictionary
    students[student_id] = {
        'name': name,
        'age': age,
        'grades': grades
    }

    print(f"\nStudent {name} registered successfully!")


def list_students_brief():
    """
    Displays a brief list of all registered students.
    Shows only ID and Name for quick reference.
    """
    if not students:
        print("\nNo students registered yet.")
        return
    
    print("\n--- Registered Students ---")
    for student_id, data in students.items():
        print(f"ID: {student_id} - Name: {data['name']}")


def consult_student():
    """
    Displays complete information for a specific student.
    Shows ID, name, age, all grades, and calculated average.
    """
    print("\n--- Consult Student ---")
    list_students_brief()  # Show available students
    
    student_id = input("Enter the student ID: ")

    if student_id not in students:
        print("No student found with that ID.")
        return

    student = students[student_id]
    average = sum(student['grades']) / len(student['grades'])

    print("\n--- Student Information ---")
    print(f"ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print(f"Average: {average:.2f}")


def update_grades():
    """
    Provides interface for modifying a student's grades.
    Options include:
    - Adding new grades
    - Modifying existing grades
    - Deleting grades
    """
    print("\n--- Update Grades ---")
    list_students_brief()  # Show available students
    
    student_id = input("Enter the student ID: ")
    
    if student_id not in students:
        print("No student found with that ID.")
        return
    
    student = students[student_id]
    print(f"\nStudent: {student['name']}")
    print(f"Current grades: {', '.join(map(str, student['grades']))}")
    
    # Grade modification menu
    while True:
        print("\nOptions:")
        print("1. Add new grade")
        print("2. Modify existing grade")
        print("3. Delete grade")
        print("4. Finish updating")
        
        option = input("Select an option: ")
        
        if option == "1":
            try:
                new_grade = float(input("Enter the new grade: "))
                if new_grade < 0 or new_grade > 5:
                    print("Grades must be between 0 and 5.")
                    continue
                student['grades'].append(new_grade)
                print("Grade added successfully!")
            except ValueError:
                print("Please enter a valid number for the grade.")
                
        elif option == "2":
            if not student['grades']:
                print("This student has no grades to modify.")
                continue
                
            print(f"Current grades (index: value):")
            for i, grade in enumerate(student['grades']):
                print(f"{i}: {grade}")
                
            try:
                index = int(input("Index of the grade to modify: "))
                if index < 0 or index >= len(student['grades']):
                    print("Index out of range.")
                    continue
                    
                new_grade = float(input("New grade value: "))
                if new_grade < 0 or new_grade > 5:
                    print("Grades must be between 0 and 5.")
                    continue
                    
                student['grades'][index] = new_grade
                print("Grade modified successfully!")
            except ValueError:
                print("Please enter a valid number.")
                
        elif option == "3":
            if not student['grades']:
                print("This student has no grades to delete.")
                continue
                
            print(f"Current grades (index: value):")
            for i, grade in enumerate(student['grades']):
                print(f"{i}: {grade}")
                
            try:
                index = int(input("Index of the grade to delete: "))
                if index < 0 or index >= len(student['grades']):
                    print("Index out of range.")
                    continue
                    
                deleted_grade = student['grades'].pop(index)
                print(f"Grade {deleted_grade} deleted successfully!")
            except ValueError:
                print("Please enter a valid number.")
                
        elif option == "4":
            break
        else:
            print("Invalid option. Please try again.")
    
    print("\nUpdated grades:")
    print(f"Final grades: {', '.join(map(str, student['grades']))}")


def delete_student():
    """
    Removes a student from the system based on their ID.
    Provides confirmation by displaying the deleted student's name.
    """
    print("\n--- Delete Student ---")
    list_students_brief()  # Show available students
    
    student_id = input("Enter the student ID: ")
    
    if student_id not in students:
        print("No student found with that ID.")
        return
    
    name = students[student_id]['name']
    del students[student_id]
    print(f"Student {name} deleted successfully!")


def list_students():
    """
    Displays complete information for all registered students.
    Includes individual averages and calculates the general average.
    """
    print("\n--- Student List ---")
    
    if not students:
        print("No students registered.")
        return
    
    for student_id, data in students.items():
        average = sum(data['grades']) / len(data['grades'])
        print(f"\nID: {student_id}")
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Grades: {', '.join(map(str, data['grades']))}")
        print(f"Average: {average:.2f}")
    
    # Calculate and display general average of all students
    all_averages = [sum(data['grades']) / len(data['grades']) for data in students.values()]
    general_average = sum(all_averages) / len(all_averages) if all_averages else 0
    print(f"\nGeneral average of all students: {general_average:.2f}")


if __name__ == "__main__":
    main()

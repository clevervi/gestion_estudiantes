# Student Management System

A Python program for managing student records, including their grades and calculating averages.

## Features

-  Register new students with auto-generated IDs
-  Consult complete student information
-  Update student grades (add, modify, delete)
-  Delete student records
-  List all students with individual and general averages
-  Data validation for ages (0-120) and grades (0-5)

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/clevervi/gestion_estudiantes.git
   ```
2. Navigate to the project directory:
   ```bash
   cd student-management-system
   ```

## Usage

Run the program with Python:
```bash
python gestion_estudiantes.py
```

The program will:
1. First ask you to register 3 students (initial setup)
2. Then display a menu with the following options:

```
--- Student Management System ---
1. Register student
2. Consult student
3. Update grades
4. Delete student
5. List all students
6. Exit
```

## Data Structure

The program uses a dictionary to store student records with the following structure:
```python
{
    'student_id': {
        'name': str,
        'age': int,
        'grades': [float]
    }
}
```

## Example Usage

1. When starting, you'll be prompted to register 3 students:
   ```
   --- Initial Setup ---
   Please register 3 students to begin:
   
   Registering student 1 of 3:
   --- Student Registration ---
   Assigned Student ID: 1
   Full name: John Doe
   Age (0-120): 20
   Enter at least 3 student grades (0-5):
   Grade 1: 4.5
   Grade 2: 3.8
   Grade 3: 4.2
   Add another grade? (y/n): n
   ```

2. After registration, you can use the menu to manage records.

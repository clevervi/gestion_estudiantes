```markdown
# Student Management System

## Overview
A Python-based command-line application for managing student records, grades, and academic statistics. The system provides comprehensive tools for educational administration with data validation and intuitive navigation.

## Features

### Core Functionality
- **Auto-ID Generation**: Unique student IDs assigned sequentially
- **Comprehensive Records**: Store names, ages, and multiple grades
- **Data Validation**: Ensures age (0-120) and grades (0-5) are within valid ranges
- **Statistical Analysis**: Calculates individual and class-wide averages

### Operational Modules
1. **Student Registration**
   - Collects name, validated age
   - Requires minimum 3 grades (0-5 scale)
   - Optional additional grade entry

2. **Student Consultation**
   - Displays complete student profiles
   - Shows calculated grade average
   - Brief listing available before consultation

3. **Grade Management**
   - Add new grades
   - Modify existing grades by index
   - Delete specific grades
   - Real-time grade updates

4. **Student Deletion**
   - Remove students by ID
   - Confirmation with student name

5. **Reporting**
   - Detailed student listings with statistics
   - General average calculation
   - Formatted output display

## Data Structure
```python
{
    "student_id": {
        "name": "Student Full Name",
        "age": 20,  # Validated integer (0-120)
        "grades": [4.5, 3.2, 4.8]  # Minimum 3, validated (0-5)
    }
}
```

## Usage Instructions

### Launching the Application
```bash
python gestion_estudiantes.py
```

### Navigation Guide
| Option | Functionality                      |
|--------|------------------------------------|
| 1      | Register new student               |
| 2      | Consult student details            |
| 3      | Update student grades              |
| 4      | Delete student record              |
| 5      | Generate complete student report   |
| 6      | Exit the application               |

### Input Requirements
- **Names**: Free text input
- **Ages**: Integers between 0-120
- **Grades**: Numbers between 0-5 (minimum 3 required)
- **Menu Selections**: Numbers 1-6

## Technical Specifications
- **Language**: Python 3.x
- **Dependencies**: None (standard library only)
- **Data Persistence**: Runtime only (no database)
- **Validation**: Comprehensive input checking

## Best Practices
1. Register students with complete grade sets
2. Verify data accuracy during consultation
3. Maintain minimum grade requirements
4. Review averages before making academic decisions

## Limitations
- No data persistence between sessions
- Single-user operation
- No export functionality

## Future Enhancements
- Database integration for persistence
- Additional statistical calculations
- Export capabilities (CSV, PDF)
- Graphical user interface
```

This README provides:
1. Clear feature documentation
2. Technical specifications
3. Usage instructions
4. Data structure explanation
5. Future improvement roadmap

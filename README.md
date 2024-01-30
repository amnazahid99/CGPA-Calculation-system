# CGPA-Calculation-system
This is the code for CGPA calculation in Lahore College for Women University in Python.
Description: 
1. Object-Oriented Approach:
    The code employs an object-oriented approach with a `Student` class to encapsulate data and functionality related to each student, such as marks, attendance, and GPA calculations. This allows for cleaner organization and management of student data.
2. User Input Handling:
    The program prompts the user to input the number of students, the number of subjects, total marks for each subject, previous semesters, student marks, and attendance.
    It validates and processes user input to ensure accurate calculation of GPA and CGPA.
3. GPA Calculation:
    The `Student` class contains methods to calculate GPA based on the provided marks and attendance for each student.
    It follows a predefined grading scale to determine the corresponding GPA for a given percentage of marks.
    GPA calculation considers attendance as a factor, adjusting the GPA based on the student's attendance percentage.
4. CGPA Calculation:
    The script calculates the CGPA for each student by considering the GPAs of previous semesters and the current semester.
    It calculates the average CGPA for all students at the end of the process.
5. Pass/Fail Determination:
    After calculating the GPA for each student, the program determines whether the student has passed or failed based on the calculated GPA percentage.
6. Output Formatting:
    The script formats the output to display relevant information such as student details, GPA, pass/fail status, CGPA, and the number of pass/fail students in a readable tabular format.
7. Error Handling:
    While not explicitly shown in the provided code, error-handling mechanisms such as input validation can be implemented to handle unexpected user input gracefully.
8. Main Function Execution:
   The code structure includes a conditional block `if __name__ == "__main__":` to ensure that the `main()` function is executed only when the script is run directly, allowing the code to be both reusable as a module and executable as a standalone script.

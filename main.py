class Student:
    def __init__(self, student_id, subjects, semesters):
        self.student_id = student_id
        self.subjects = subjects
        self.semesters = semesters
        self.marks = []
        self.attendance = []
        self.gpa = []
        self.cgpa = []

    def input_marks(self):
        for i in range(self.subjects):
            mark = int(input(f"Enter marks of subject {i + 1}: "))
            self.marks.append(mark)

    def input_attendance(self):
        for i in range(self.subjects):
            att = float(input(f"Enter attendance of subject {i + 1}: "))
            self.attendance.append(att)

    def calculate_gpa(self, total):
        gpa_sum = 0.0
        attendance_sum = sum(self.attendance)

        print("\nReport Card")
        print("-" * 70)
        print("| Student | Subject | Marks | Total | Percentage | Grade | GPA | Result |")
        print("-" * 70)

        for i in range(self.subjects):
            percentage = (self.marks[i] * 100.0) / total
            grade, gpa_val = self.get_grade_gpa(percentage)
            self.gpa.append(gpa_val * self.attendance[i])
            gpa_sum += self.gpa[i]
            result = "pass" if grade != "F" else "fail"
            print(f"|   {self.student_id + 1:6} |   {i + 1:6} | {self.marks[i]:5} | {total:5} |"
                  f" {percentage:10.1f}% | {grade:5} | {gpa_val:3.1f} | {result:5} |")

        print("-" * 70)
        overall_gpa = gpa_sum / attendance_sum
        print(f"GPA is {overall_gpa:.2f}\n")
        return overall_gpa

    def input_previous_gpa(self):
        for j in range(self.semesters):
            semester_gpa = float(input(f"Enter GPA of semester {j + 1} for Student {self.student_id + 1}: "))
            self.cgpa.append(semester_gpa)

    def calculate_cgpa(self, current_gpa):
        cgpa_sum = current_gpa + sum(self.cgpa)
        overall_cgpa = min(cgpa_sum / (self.semesters + 1), 4.0)
        print(f"CGPA is {overall_cgpa:.2f}\n")
        return overall_cgpa

    @staticmethod
    def get_grade_gpa(percentage):
        if percentage >= 85:
            return "A+", 4.0
        elif percentage >= 80:
            return "A", 3.7
        elif percentage >= 75:
            return "B+", 3.3
        elif percentage >= 70:
            return "B", 3.0
        elif percentage >= 65:
            return "B-", 2.7
        elif percentage >= 60:
            return "C+", 2.3
        elif percentage >= 55:
            return "C", 2.0
        elif percentage >= 51:
            return "C-", 1.7
        elif percentage == 50:
            return "D", 1.0
        else:
            return "F", 0.0


def main():
    n = int(input("Enter number of Students: "))
    s = int(input("Enter number of Subjects: "))
    total = int(input("Enter total marks of subject: "))
    a1 = int(input("Enter previous number of semesters: "))

    students = [Student(i, s, a1) for i in range(n)]
    
    for student in students:
        print(f"\n--- Enter marks of Student {student.student_id + 1} ---")
        student.input_marks()
        student.input_attendance()

    pass_count = 0
    fail_count = 0

    for student in students:
        current_gpa = student.calculate_gpa(total)
        student.input_previous_gpa()
        current_cgpa = student.calculate_cgpa(current_gpa)
        if current_gpa < 1.0:
            print("Fail")
            fail_count += 1
        else:
            print("Pass")
            pass_count += 1

    print(f"| Number of Pass students in semester {a1 + 1} is {pass_count} |")
    print(f"| Number of Fail students in semester {a1 + 1} is {fail_count} |")

if __name__ == "__main__":
    main()

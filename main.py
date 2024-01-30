class Student:
  def __init__(self, num_subjects):
      self.marks = []
      self.attendance = []
      self.num_subjects = num_subjects
      self.total_marks = 0

  def add_marks(self, marks):
      self.marks.append(marks)
      self.total_marks += marks

  def add_attendance(self, att):
      self.attendance.append(att)

  def calculate_gpa(self, total):
      total_attendance = sum(self.attendance)
      total_percentage = (self.total_marks / (self.num_subjects * total)) * 100
      gpa = 0.0
      if total_percentage >= 85:
          gpa = 4.0
      elif total_percentage >= 80:
          gpa = 3.7
      elif total_percentage >= 75:
          gpa = 3.3
      elif total_percentage >= 70:
          gpa = 3.0
      elif total_percentage >= 65:
          gpa = 2.7
      elif total_percentage >= 60:
          gpa = 2.3
      elif total_percentage >= 55:
          gpa = 2.0
      elif total_percentage >= 51:
          gpa = 1.7
      elif total_percentage == 50:
          gpa = 1.0
      return gpa * total_attendance, total_percentage

def main():
  n = int(input("Enter number of Students: "))
  s = int(input("Enter number of Subjects: "))
  total = int(input("Enter total marks of subject: "))
  a1 = int(input("Enter previous number of semesters: "))

  students = []

  for _ in range(n):
      student = Student(s)
      students.append(student)

  for i, student in enumerate(students, start=1):
      print(f"---Enter marks of Student {i}---")
      for j in range(s):
          marks = int(input(f"Enter marks of subject {j + 1}: "))
          student.add_marks(marks)

  print("-------------------------------------")
  print("Enter attendance of each subject")

  for i in range(s):
      att = int(input(f"Enter attendance of subject {i + 1}: "))
      for student in students:
          student.add_attendance(att)

  print("------------------------------------------")
  print("Calculating GPA and CGPA")

  pass_count = 0
  fail_count = 0
  total_cgpa = 0.0

  for i, student in enumerate(students, start=1):
      total_gpa, percentage = student.calculate_gpa(total)
      cgpa = (total_gpa + sum(float(input(f"Enter GPA of semester {j + 1} for Student {i}: ")) for j in range(a1))) / (a1 + 1)
      print(f"Student {i}:")
      print(f"GPA is {total_gpa:.2f}")
      if percentage < 50:
          print("Fail")
          fail_count += 1
      else:
          print("Pass")
          pass_count += 1
      print(f"CGPA is {cgpa:.2f}")
      total_cgpa += cgpa

  print(f"Number of Pass students in semester {a1 + 1} is {pass_count}")
  print(f"Number of Fail students in semester {a1 + 1} is {fail_count}")
  print("Average CGPA:", total_cgpa / n)

if __name__ == "__main__":
  main()

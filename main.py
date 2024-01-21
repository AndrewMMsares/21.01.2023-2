# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def get_details(self):
#         return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
#
#
# class Teacher(Person):
#     def __init__(self, name, age, gender, subject_taught):
#         super().__init__(name, age, gender)
#         self.subject_taught = subject_taught
#
#     def teach(self):
#         return f"{self.name} is teaching {self.subject_taught}"
#
#
# class Student(Person):
#     def __init__(self, name, age, gender, student_id):
#         super().__init__(name, age, gender)
#         self.student_id = student_id
#         self.courses = []
#
#     def enroll(self, subject):
#         self.courses.append(subject)
#         return f"{self.name} enrolled in {subject.name}"
#
#     def list_courses(self):
#         return f"{self.name}'s enrolled courses: {', '.join(course.name for course in self.courses)}"
#
#
# class Subject:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# class Academy:
#     def __init__(self, name):
#         self.name = name
#         self.teachers = []
#         self.students = []
#         self.subjects = []
#
#     def add_teacher(self, teacher):
#         self.teachers.append(teacher)
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def add_subject(self, subject):
#         self.subjects.append(subject)
#
#     def list_teachers(self):
#         return [teacher.get_details() for teacher in self.teachers]
#
#     def list_students(self):
#         return [student.get_details() for student in self.students]
#
#     def list_subjects(self):
#         return [subject.name for subject in self.subjects]

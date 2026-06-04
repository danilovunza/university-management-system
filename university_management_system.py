"""
University Management System

Author: Danilo Vunza
Course: COSC 2436

Description:
University management system using
Object-Oriented Programming concepts.
"""


class Student:

    def __init__(
        self,
        student_id,
        name,
        major
    ):

        self.student_id = student_id
        self.name = name
        self.major = major


class Professor:

    def __init__(
        self,
        professor_id,
        name,
        department
    ):

        self.professor_id = professor_id
        self.name = name
        self.department = department


class Course:

    def __init__(
        self,
        course_code,
        course_name,
        professor
    ):

        self.course_code = course_code
        self.course_name = course_name
        self.professor = professor


class Enrollment:

    def __init__(
        self,
        student,
        course
    ):

        self.student = student
        self.course = course

        self.grade = None


class University:

    def __init__(self):

        self.students = []

        self.professors = []

        self.courses = []

        self.enrollments = []

    def add_student(
        self,
        student_id,
        name,
        major
    ):

        student = Student(
            student_id,
            name,
            major
        )

        self.students.append(student)

        print("\nStudent added successfully.")

    def add_professor(
        self,
        professor_id,
        name,
        department
    ):

        professor = Professor(
            professor_id,
            name,
            department
        )

        self.professors.append(professor)

        print("\nProfessor added successfully.")

    def add_course(
        self,
        course_code,
        course_name,
        professor_id
    ):

        professor = None

        for p in self.professors:

            if p.professor_id == professor_id:

                professor = p

                break

        if professor is None:

            print("\nProfessor not found.")

            return

        course = Course(
            course_code,
            course_name,
            professor
        )

        self.courses.append(course)

        print("\nCourse added successfully.")

    def enroll_student(
        self,
        student_id,
        course_code
    ):

        student = None

        course = None

        for s in self.students:

            if s.student_id == student_id:

                student = s

        for c in self.courses:

            if c.course_code == course_code:

                course = c

        if student and course:

            enrollment = Enrollment(
                student,
                course
            )

            self.enrollments.append(
                enrollment
            )

            print(
                "\nEnrollment successful."
            )

        else:

            print(
                "\nStudent or course not found."
            )

    def assign_grade(
        self,
        student_id,
        course_code,
        grade
    ):

        for enrollment in self.enrollments:

            if (
                enrollment.student.student_id
                ==
                student_id
                and
                enrollment.course.course_code
                ==
                course_code
            ):

                enrollment.grade = grade

                print(
                    "\nGrade assigned successfully."
                )

                return

        print("\nEnrollment not found.")

    def view_transcript(
        self,
        student_id
    ):

        print("\nTRANSCRIPT")

        print("-" * 70)

        found = False

        for enrollment in self.enrollments:

            if (
                enrollment.student.student_id
                ==
                student_id
            ):

                found = True

                print(
                    f"{enrollment.course.course_code} | "
                    f"{enrollment.course.course_name} | "
                    f"Grade: {enrollment.grade}"
                )

        if not found:

            print(
                "No academic records found."
            )

    def display_students(self):

        print("\nSTUDENTS")

        print("-" * 70)

        for student in self.students:

            print(
                f"{student.student_id} | "
                f"{student.name} | "
                f"{student.major}"
            )

    def display_courses(self):

        print("\nCOURSES")

        print("-" * 70)

        for course in self.courses:

            print(
                f"{course.course_code} | "
                f"{course.course_name} | "
                f"{course.professor.name}"
            )


def display_menu():

    print("\n" + "=" * 60)

    print("UNIVERSITY MANAGEMENT SYSTEM")

    print("=" * 60)

    print("1. Add Student")
    print("2. Add Professor")
    print("3. Add Course")
    print("4. Enroll Student")
    print("5. Assign Grade")
    print("6. View Transcript")
    print("7. View Students")
    print("8. View Courses")
    print("9. Exit")

    print("=" * 60)


def main():

    university = University()

    while True:

        display_menu()

        choice = input(
            "Select an option: "
        )

        if choice == "1":

            university.add_student(
                input("Student ID: "),
                input("Name: "),
                input("Major: ")
            )

        elif choice == "2":

            university.add_professor(
                input("Professor ID: "),
                input("Name: "),
                input("Department: ")
            )

        elif choice == "3":

            university.add_course(
                input("Course Code: "),
                input("Course Name: "),
                input("Professor ID: ")
            )

        elif choice == "4":

            university.enroll_student(
                input("Student ID: "),
                input("Course Code: ")
            )

        elif choice == "5":

            university.assign_grade(
                input("Student ID: "),
                input("Course Code: "),
                input("Grade: ")
            )

        elif choice == "6":

            university.view_transcript(
                input("Student ID: ")
            )

        elif choice == "7":

            university.display_students()

        elif choice == "8":

            university.display_courses()

        elif choice == "9":

            print(
                "\nThank you for using the system."
            )

            break

        else:

            print(
                "\nInvalid option."
            )


main()

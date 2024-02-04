from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):

    def test_constructor(self):
        student1 = Student("Martin")
        student3 = Student('', {"Math": [1, 2, 3, 4]})
        self.assertEqual(student1.name, "Martin")
        self.assertEqual(student1.courses, {})
        student2 = Student("Dani", {"Math": ["a", "b", "c"], "PE": [""]})
        self.assertEqual(student2.name, "Dani")
        self.assertEqual(student2.courses, {"Math": ["a", "b", "c"], "PE": [""]})
        self.assertEqual(student3.name, "")
        self.assertEqual(student3.courses, {"Math": [1, 2, 3, 4]})

    def test_enroll_method1(self):
        student1 = Student("Martin")
        result = student1.enroll("Math", ["A", "B", "C"], "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(student1.courses, {"Math": []})

    def test_enroll_method2(self):
        student1 = Student("Martin")
        result1 = student1.enroll("Math", ["A", "B", "C", 1], "Y")
        result2 = student1.enroll("Physics", ["Newton", "Einstein", "Tesla"], "")
        self.assertEqual(result1, "Course and course notes have been added.")
        self.assertEqual(result2, "Course and course notes have been added.")
        self.assertEqual(student1.courses, {"Math": ["A", "B", "C", 1], "Physics": ["Newton", "Einstein", "Tesla"]})

    def test_enroll_method3(self):
        student1 = Student("Martin")
        student1.enroll("Math", ["A", "B", "C", 1], "Y")
        result = student1.enroll("Math", ["sin", "cos", "tan", -1], "N")
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(student1.courses, {"Math": ["A", "B", "C", 1, "sin", "cos", "tan", -1]})

    def test_add_notes_positive(self):
        student1 = Student("Martin")
        student1.enroll("Math", ["A", "B", "C", 1], "Y")
        result = student1.add_notes("Math", ["sin", "cos", "tan", -1])
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_negative(self):
        student1 = Student("Martin")
        student1.enroll("Math", ["A", "B", "C", 1], "Y")
        student2 = Student("Dani", {"Something": [1, 2, 3, 4, 5]})
        with self.assertRaises(Exception) as context:
            student1.add_notes("Physics", ["Newton", "Einstein", "Tesla"])
        with self.assertRaises(Exception) as context1:
            student2.add_notes("Minecraft", ["diamonds", 64])
        self.assertEqual(str(context1.exception), "Cannot add notes. Course not found.")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_course_positive(self):
        student1 = Student("Martin")
        student2 = Student("Dani", {"Something": [1, 2, 3, 4, 5]})
        student1.enroll("Math", ["A", "B", "C", 1], "Y")
        student1.enroll("Physics", [1, 2, 3])
        result = student1.leave_course("Math")
        result2 = student2.leave_course("Something")
        with self.assertRaises(Exception) as a:
            student1.leave_course("Math")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(student1.courses, {"Physics": [1, 2, 3]})
        self.assertEqual(student2.courses, {})
        self.assertEqual(result2, "Course has been removed")
        self.assertEqual(str(a.exception), "Cannot remove course. Course not found.")

    def test_leave_course_negative(self):
        student1 = Student("Martin")
        student2 = Student("Dani", {"Something": [1, 2, 3, 4, 5]})
        student1.enroll("Math", ["A", "B", "C", 1], "Y")
        with self.assertRaises(Exception) as context:
            student1.leave_course("Physics")
        with self.assertRaises(Exception) as ve:
            student2.leave_course("IDK")
        self.assertEqual(str(ve.exception), "Cannot remove course. Course not found.")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")

    def test_constructor_default_courses(self):
        student = Student("John")
        self.assertEqual(student.courses, {})

    def test_enroll_multiple_courses(self):
        student = Student("Alice")
        student.enroll("Math", ["A", "B"])
        student.enroll("Physics", ["Newton", "Einstein"])
        student.enroll("IDK", [])
        self.assertEqual(student.courses, {"Math": ["A", "B"], "Physics": ["Newton", "Einstein"], "IDK": []})
        student1 = Student("Alice")
        student1.enroll("Math", ["A", "B"])
        student1.enroll("Physics", ["Newton", "Einstein"])
        self.assertEqual(student1.courses, {"Math": ["A", "B"], "Physics": ["Newton", "Einstein"]})

    def test_add_notes_to_nonexistent_course(self):
        student = Student("Bob")
        with self.assertRaises(Exception) as context:
            student.add_notes("History", ["Ancient", "Modern"])
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_nonexistent_course(self):
        student = Student("Charlie")
        with self.assertRaises(Exception) as context:
            student.leave_course("Chemistry")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")

    def test_empty_notes(self):
        student = Student("David")
        result = student.enroll("Math", [], "Y")
        self.assertEqual(result, "Course and course notes have been added.")


if __name__ == '__main__':
    main()

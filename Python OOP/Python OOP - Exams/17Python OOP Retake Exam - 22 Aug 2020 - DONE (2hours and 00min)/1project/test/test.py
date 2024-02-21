from project.student_report_card import StudentReportCard
from unittest import TestCase


class TestStudentReportCard(TestCase):
    def test_constructor(self):
        student = StudentReportCard("Martin", 12)
        self.assertEqual(student.student_name, "Martin")
        self.assertEqual(student.school_year, 12)
        self.assertEqual(student.grades_by_subject, {})
        with self.assertRaises(ValueError) as ve:
            StudentReportCard("", 11,)
        self.assertEqual(str(ve.exception), "Student Name cannot be an empty string!")
        with self.assertRaises(ValueError) as ve2:
            StudentReportCard("Dani", 13)
        self.assertEqual(str(ve2.exception), "School Year must be between 1 and 12!")
        with self.assertRaises(ValueError) as ve3:
            StudentReportCard("Marti", 0)
        self.assertEqual(str(ve3.exception), "School Year must be between 1 and 12!")
        with self.assertRaises(ValueError) as ve4:
            StudentReportCard("Marti", -5)
        self.assertEqual(str(ve4.exception), "School Year must be between 1 and 12!")

    def test_add_grade_case1(self):
        student = StudentReportCard("Martin", 12)
        student.add_grade("Math", 6.00)
        self.assertEqual(student.grades_by_subject, {"Math": [6.00]})
        student.add_grade("English", 6.00)
        self.assertEqual(student.grades_by_subject, {"Math": [6.00], "English": [6.00]})
        student.add_grade("Math", 5.00)
        self.assertEqual(student.grades_by_subject, {"Math": [6.00, 5.00], "English": [6.00]})
        message = student.average_grade_by_subject()
        self.assertEqual(message, "Math: 5.50\nEnglish: 6.00")
        message2 = student.average_grade_for_all_subjects()
        self.assertEqual(message2, "Average Grade: 5.67")
        student2 = StudentReportCard("Maik", 1)
        student2.add_grade("Math", 4)
        report1 = student.__repr__()
        report2 = student2.__repr__()
        self.assertEqual(report1, "Name: Martin\nYear: 12\n----------\nMath: 5.50\nEnglish: 6.00\n----------\nAverage Grade: 5.67")
        self.assertEqual(report2, "Name: Maik\nYear: 1\n----------\nMath: 4.00\n----------\nAverage Grade: 4.00")

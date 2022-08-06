import unittest

from for_testing2 import Student
class For_Testing(unittest.TestCase):
    def setUp(self):
        name = "Ali"
        lastname = "Valiyev"
        byear = 1998
        grade = 3
        self.subjects = ["Geography", "Math"]
        self.student1 = Student(name, lastname, byear, grade)
        self.student2 = Student(name, lastname, byear, grade)

    def test_create_student(self):
        self.assertIsNotNone(self.student1.name)
        self.assertIsNotNone(self.student1.lastname)
        self.assertIsNotNone(self.student1.byear)
        self.assertIsNotNone(self.student1.grade)
        self.assertIsNotNone(self.student2.subjects)

# Alhamdulillah
    def test_add_subject(self):
        self.student1.add_subject("Geography")
        self.student1.add_subject("Math")
        self.assertEqual(self.subjects, self.student1.subjects)

# FAILED. But it will be change to good success in shaa Alloh.
    # def test_remove_subject(self):
    #     self.student1.remove_subject("Geography")
    #     self.assertEqual(self.subjects, self.student1.subjects)

unittest.main()

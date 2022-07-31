'''
This is a program that can check the parametres and 
functions of claasses named "Person" and "Student"
'''
import unittest

# FAILED. But it will be change to good success in shaa Alloh.
from for_testing import Person, Student
class Student_test(unittest.TestCase):
    def setUp(self):
        name = "Ali"
        lastname = "Valiyev"
        byear = 1998
        self.subjects = ["Mathematics"]
        self.student2 = Student(name, lastname, byear)
        self.student1 = Student(name, lastname, byear)
        self.person1 = Person(name, lastname)

    # def test_student_create(self):
    #     # Is available
    #     self.assertIsNotNone(self.student1.name)
    #     self.assertIsNotNone(self.student1.lastname)
    #     self.assertIsNotNone(self.student1.byear)
    #     # Is not available
    #     self.assertIsNone(self.student1.idnumber)
    #     self.assertIsNone(self.student2.idnumber)

    # def test_student_add_subject(self):
    #     self.student1.add_subject("Mathematics")
    #     self.assertEqual(self.subjects, self.student1.subjects)

    def test_remove_subject(self):
        self.student1.remove_subject("Mathematics")
        self.assertEqual(self.subjects, self.student1.subjects)

    # def test_get_nifo_student(self):
    #     student1_info = 'Ali Valiyev, born in 1998'
    #     self.assertEqual(student1_info, self.student1.get_info())

unittest.main()
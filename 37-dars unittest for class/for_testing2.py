class Student:
    def __init__(self, name, lastname, byear, grade):
        self.name = name
        self.lastname = lastname
        self.byear = byear
        self.grade = grade
        self.subjects = []

    def get_info(self):
        return f"Student: {self.name} {self.lastname}, born in {self.byear}.\nGrade: {self.grade}"

    def add_subject(self, *subjects):
        self.subjects.append(*subjects)
    
    def remove_subject(self, *subjects):
        self.subjects.remove(*subjects)

'''
# FAILED. But it will be change to good success in shaa Alloh.
# class Subject:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Subject name: {self.name}\n"

# sub1 = Subject("mathematics")
# sub2 = Subject("physics")
# sub3 = Subject("english")
# sub4 = Subject("history")
# sub5 = Subject("algorithms & data structure")
'''

student1 = Student("Ali", "Valiyev", 1998, 3)
student2 = Student("Salim", "Olimov", 1999, 2)

student1.add_subject("Math")
student1.add_subject("Physics")
student1.add_subject("English")
student1.add_subject("History")

student2.add_subject("English")
student2.add_subject("Math")
student2.add_subject("Physics")
student2.add_subject("History")
student2.add_subject("Algorithms & data structure")

student1.remove_subject("English")
student2.remove_subject("History")

# print(student1.get_info())        #temporary commented for testing via unittest
# print(student1.subjects[:])       #temporary commented for testing via unittest
# print("* * * * * * * * * * * *")  #temporary commented for testing via unittest
# print(student2.get_info())        #temporary commented for testing via unittest
# print(student2.subjects[:])       #temporary commented for testing via unittest


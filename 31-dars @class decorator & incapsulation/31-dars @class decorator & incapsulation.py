from uuid import uuid4
from random import choice
from data_colors import colors

class Person:
    __num_persons = 0
    __person_color = choice(colors)
    def __init__(self, name, lastname, byear):
        self.name = name
        self.lastname = lastname
        self.byear = byear
        self.__languages = ["Uzbek"]
        Person.__num_persons += 1

    @classmethod
    def get_person_color(cls):
        return cls.__person_color

    def set_language(self):
        self.__languages.append("English")

    def get_languages(self):
        return self.__languages




class Student(Person):
    __num_students = 0
    def __init__(self, name, lastname, byear):
        super().__init__(name, lastname, byear)
        self.__id = uuid4()
        Student.__num_students += 1

    def get_id(self):
        return f"Student ID: {self.__id}"

    @classmethod
    def get_num_students(cls):
        return cls.__num_students


    


stu1 = Student("olim".capitalize(), "qosimov".title(), 2002)
stu2 = Student("Karim", "Salimov", 2000)
stu3 = Student("Vali", "Azizov", 1997)

pers1 = Person("Big", "Boss", 1999)
print(f"{pers1.name}'s t-shirt color: {pers1.get_person_color()}\n\n")


# print(f"Name: {stu3.name}\n{stu3.get_id()}\n\n")
# print(f"Name: {stu1.name}\n{stu1.get_id()}\n\n")
# print(f"Name: {stu2.name}\n{stu2.get_id()}\n\n")

# print(f"* * * * *\nHow much: {Student.get_num_students()}\n* * * * *\n")

# print(stu1.get_languages())
# stu2.set_language()
# print(stu2.get_languages())
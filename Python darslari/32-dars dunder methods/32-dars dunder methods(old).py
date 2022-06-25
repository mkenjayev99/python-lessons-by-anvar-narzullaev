from uuid import uuid4

class Person:
    __num_persons = 0
    def __init__(self, name, lastname, age, country):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.country = country
        Person.__num_persons += 1

    def __repr__(self):
        return f"Name: {self.name}; Last name: {self.lastname}; Age: {self.age}"

person1 = Person("Ali", "Valivev", 18, "Tashkent")
# print(person1)


class Student(Person):
    def __init__(self, name, lastname, age, country, course):
        super().__init__(name, lastname, age, country)
        self.id = uuid4()
        self.course = course

    def __eq__(self, another_obj):
        """ EQual """
        return self.course == another_obj.course

    def __lt__(self, another_obj):
        """ Lower Than"""
        return self.course < another_obj.course

    def __le__(self, another_obj):
        """ Lower (or) Equal """
        return self.course <= another_obj.course

st1 = Student("Xobil", "Qobilov", 30, "India", 4)
st2 = Student("Salim", "Karimov", 23, "USA", 2)
st3 = Student("Olim", "Naimov", 16, "Uzbekistan", 1)

# print(st1 == st2) #False
# print(st1 < st2) #False
# print(st1 <= st2) #False


class StudentsGroup:
    def __init__(self, name):
        self.name = name
        self.students = []

    def __repr__(self):
        return f"Group: {self.name}"

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            return f"Enter the Student object "

    

gr1 = StudentsGroup("Stars")


for student in [st1, st2, st3]:
    gr1.add_student(student)


print(gr1)

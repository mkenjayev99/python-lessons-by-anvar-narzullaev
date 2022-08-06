from turtle import st
from uuid import uuid4



class Person:
    
    def __init__(self, name, lastname, bornyear): # constructor
        self.name = name
        self.lastname = lastname
        self.bornyear = bornyear
        self.id = uuid4()

    def get_info(self):
        return f"Person: {self.name} {self.lastname}\n{self.id}"

    def __repr__(self):
        return f"{self.name} {self.lastname}"



class Student(Person):
    def __init__(self, name, lastname, institute, bornyear):
        super().__init__(name, lastname, bornyear)
        self.institute = institute
    def get_info(self): # overwrite method
        return f"Person: {self.name} {self.lastname}\nInstitute: {self.institute}"
    
    def __repr__(self):
        return f"Student: {self.name} {self.lastname}, {self.bornyear}, {self.institute}\n"


person1 = Person("Tomas", "Edison", 1887)
person2 = Person("Albert", "Einstein", 1788)
person3 = Person("Issaac", "Newton", 1685)
person4 = Person("Olim", "Olmosov", 1887)

student1 = Student("Salim", "Karimov", "FSU", 1990)
student2 = Student("Eric", "Monroe", "FSU", 1995)
student3 = Student("Ahmad", "Ziyoyev", "FSU", 2000)
student4 = Student("Qambar", "Odilov", "Yale", 2000)
student5 = Student("To'lqin", "Boltayev", "Yale", 1999)
student6 = Student("Oqil", "Qorayev", "Yale", 1998)


class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def __repr__(self):
        return f"University name: {self.name}"

    def __len__(self):
        return len(self.students)

    # def add_student(self, student): # funksiyadan atshqarida for bilan aylanib obyekt qo'shadi
    #     if isinstance(student, Student):
    #         self.students.append(student)
    #     else:
    #         return "Enter the Student object "

    def add_student2(self, *value): # funksiyani ichida for bilan aylanib obyekt qo'shadi
        for student in value:
            if isinstance(student, Student):
                self.students.append(student)
            else:
                print("Enter the student object!")

    def del_student(self, *value):
        for student in value:
            if isinstance(student, Student):
                self.students.remove(student)

    def __delattr__(self, *value):
        for student in value:
            if student in self.students:
                self.students.remove(student)
            else:
                print("Object does not exist")

    def __getitem__(self, index):
        return self.students[index]

    def __setitem__(self, index, value):
        if isinstance(value, Student):
            self.students[index] = value

    def __add__(self, value):
        if isinstance(value, University):
            new_university = University(f"{self.name} {value.name}")
            new_university.students = self.students + value.students
            return new_university
        elif isinstance(value, Student):
            self.add_student2(value)
        else:
            print(f"It is impossible to add {type(value)}")
    def __len__(self):
        return len(self.students)

    def __call__(self, *param):
        if param:
            for student in param:
                self.add_student2(student)
        else:
            return [student for student in self.students]


uni1 = University("FSU")
uni2 = University("Yale")
# for student in [student1, student2, student3]: # funksiyadan tashqarida for bilan aylanib obyekt qo'shadi
#     uni1.add_student(student)

# for student in [student4, student5, student6]: # funksiyadan tashqarida for bilan aylanib obyekt qo'shadi
#     uni2.add_student(student)


# print(len(uni1), '\n', len(uni2))

# print(uni1.students, '\n', uni2.students)

# print(uni1[1], ' and ', uni2[0])

# student7 = Student("Sarvar", "Japarov", "TJTSI",1993)
# uni1[0] = student7 # index bo'yicha ob'ektlarni o'zgartirish

# print(uni1[0]) # ob'ektni index bo'yicha chiqaradi

uni1.add_student2(student1, student2, student3)
uni2.add_student2(student4, student5, student6)

# uni3 = uni1 + uni2
# print(uni3) # yangi uni ning ismini console ga chiqaradi
# print(uni3[:]) # yangi uni dagi talabalar ro'yxatini chiqaradi

# student8 = Student("Arevat", "Grigoryan", "TDJU", 1989) # university ga qo'shish operatori yordan=mida yangi qiymat qo'shadi
# uni1 + student8
# print(uni1[:])

# print(uni1) # shu unining **ismini** ko'rsatadi
# print(uni1()) # shu uni ichidagi **qiymat (ob'ektni)** ko'rsatadi

student_new = Student("Alimardon", "Bobojonov", "SNU", 2000)
student_new2 = Student("Mardon", "Qobil", "TAQI", 1998)
uni1(student_new, student_new2)
print(uni1())

# uni1.del_student(student_new2, student_new) # 2ta yangi qo'shilgan studentni o'chiradi
# print("\n* * * * * * * * * * * * * *\n")
# print(uni1())

print("\n* * * * * * * * * * * * * *\n")
uni1.__delattr__(student_new2)
print(uni1[:])



"""
Creating simple class object
"""

class Student:
    def __init__(self, name, surname, email, age):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age

    def introduce(self): #following this steps <object> can introduce itself
        return f"I am {self.name, self.surname}, {self.age} years. \nYou can contact my email typing by {self.email}"

    def get_full_name(self): #following this steps <object> can say it's name and surname
        """gets name and surname form __init__"""
        return f"{self.name} {self.surname}" # agar shu {argument1} {argument2} holatida emas {argument1, argument2} holatida yozilsa konsolga tuple qaytaradi

    def get_byear(self, year): #following this steps <object> can say it's age
        return year - self.age

    def get_age_email(self): #following this steps <object> can say both of age and email using <list>
        return [self.age, self.email]


# case 4:
# student1 = Student('Ali', 'Valiyev', 'alivaliyev@vk.com', 23)
# print(student1.introduce())

# case 3:
# student2 = Student('musilmonxon'.title(), 'kenjayev'.title(), 'abcbca@gmail.com', 23)
# print(student2.get_full_name())

# case 2:
# student3 = Student('ali'.title(), 'karimov'.title(), 'kali@vk.ru', 15)
# print(student3.get_byear(2022))

# case 1:
student4 = Student('salim'.title(), 'olimov'.title(), 'salimolimov@bk.ru', 24)
print('age: ', student4.get_age_email()[0], '\nemail:', student4.get_age_email()[1])
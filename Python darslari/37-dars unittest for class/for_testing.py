# FAILED. But it will be change to good success in shaa Alloh.
class Person:
    def __init__(self, name, lastname, byear):
        self.name = name
        self.lastname = lastname
        self.byear = byear

    def get_info(self):
        return f"{self.name} {self.lastname}, born in {self.byear}" #Ali Valiyev, born in 1998


class Student(Person):
    def __init__(self, name, lastname, byear):
        super().__init__(name, lastname, byear)
        self.subjects = []
        self.quantity_subjects = 0
        self.grade = 1
        self.byear = byear

    def add_subject(self, subject): #fanga_yozil() function
        self.subjects.append(subject)
        self.quantity_subjects += 1

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
            self.quantity_subjects -= 1    
        else:
            return f"you are not enrolled in this science"



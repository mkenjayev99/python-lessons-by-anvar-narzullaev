class Person:
    def __init__(self, name, lastname, byear):
        self.name = name
        self.lastname = lastname
        self.byear = byear


class Student(Person):
    def __init__(self, name, lastname, byear, idnumber):
        super().__init__(name, lastname, byear)
        self.idnumber = idnumber
        self.subjects = []
        self.quantity_subjects = 0
        self.grade = 1

    def add_subject(self, subject): #fanga_yozil() function
        self.subjects.append(subject)
        self.quantity_subjects += 1

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
            self.quantity_subjects -= 1    
        else:
            return f"you are not enrolled in this science"

class Subject:
    def __init__(self, name, pages, duration, difficulty):
        self.name = name
        self.pages = pages
        self.duration = duration
        self.difficulty = difficulty

student1 = Student("salim".capitalize(), "olimov".capitalize(), 2000, "ise12304")

# creating 'Student' objects
subject1 = Subject("History of companions", 1049, "5 month", "Elementary")
subject2 = Subject("Atomic habits", 600, "3 month", "Elementary")
subject3 = Subject("Aqida ilmi", 900, "6 month", "Intermediate")
subject4 = Subject("Deep work", 300, "2 month", "Elementary")

# adding subjects to student class
student1.add_subject(subject1)
student1.add_subject(subject2)
student1.add_subject(subject3)
student1.add_subject(subject4)

# removing subjects from stodent class
student1.remove_subject(subject4)

# ********************************************

class Professor(Person):
    def __init__(self, name, lastname, university, science):
        super().__init__(name, lastname)
        self.science = science
        self.university = university

    def get_fullname(self):
        return f"Name: {self.name}, Lastname: {self.lastname}"

    def get_specialization(self):
        return f"University: {self.university}, Science: {self.science}"
    


class User(Person):
    def __init__(self, name, lastname, byear, passport_data):
        super().__init__(name, lastname, byear)
        self.passport_data = passport_data

    def get_user_info(self):
        return f"Name: {self.name}, Lastname: {self.lastname}, Born year: {self.byear}, Passport data: {self.passport_data}"

    def get_info(self):
        return f"Name: {self.name}, Lastname: {self.lastname}"


class Merchant(Person):
    def __init__(self, name, lastname, byear, bank_accaunt, phone):
        super().__init__(name, lastname, byear)
        self.bank_accaunt = bank_accaunt
        self.phone = phone

    def get_merchant_bank_accaunt(self):
        return f"Bank accaunt: {self.bank_accaunt}"

    def get_merchant_phone(self):
        return f"merchant's phone: {self.phone}"

    def get_info(self):
        return f"Name: {self.name}, Lastname: {self.lastname}, Born year: {self.byear}"


class Customer(Person):
    def __init__(self, name, lastname, byear, bank_accaunt):
        super().__init__(name, lastname, byear)
        self.bank_accaunt = bank_accaunt
        self.cash = 9999

    def add_cash_to_customer(self):
        self.cash += int(input("Enter cash: "))

    def get_infocash(self):
        return f"Cash: {self.cash}"

    def get_info(self):
        return f"Name: {self.name}, Lastname: {self.lastname}, Born year: {self.byear}"

class Patient(Person):
    def __init__(self, name, lastname, phone, byear, passport_data):
        super().__init__(name, lastname, byear)
        self.passport_data = passport_data
        self.phone = phone
        self.disease = "unknown"
        self.cure = "swimming"

    def get_info(self):
        return f"Name: {self.name} Lastname: {self.lastname}, Born in {self.byear}. Passport data: {self.passport_data}, Disease: currently {self.disease}"

    def get_cure(self):
        return f"Treatment: {self.cure}"



class Admin(User):
    def __init__(self, name, lastname, byear, passport_data, password):
        super().__init__(name, lastname, byear, passport_data)
        self.password = password

    def get_info(self):
        return f"Name: {self.name} Lastname: {self.lastname}, Born in {self.byear}. Passport data: {self.passport_data}"

    def ban_user(self, user):
        return f"{user} - user blocked"



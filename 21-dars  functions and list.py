# 1 - masala
"""
def do_alpha(names):
    '''Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir
     matnning birinchi harfini katta harfga o'zgatiruvchi funksiya'''
    alpha_students = []
    while names:
        student = names.pop(0)
        alpha_students.append(student.title())
    return alpha_students

students = ['ali', 'vali', 'salim', 'karim', 'najim', 'hoshim', 'odil', 'qobil']
print(do_alpha(students))
"""

# -------------------------------------------

# 2 - masala
"""
def do_aplha(names):
    '''Yuoqirdagi funksiyaning asl ro'yxatni o'zgartirmaydigan
         va yangi ro'yxat qaytaradigan qilib o'zgartirilgan shakli'''

    names = students[:]
    alpha_students = []
    while names:
        name_s = names.pop().title()
        alpha_students.append(name_s)
    return alpha_students


students = ['ali', 'vali', 'salim', 'karim', 'najim', 'hoshim', 'odil', 'qobil']
print(students, end="\n\n")
print(do_aplha(students.reverse()))
"""

# -------------------------------------------

# 3 - masala
# Way - A:
"""
def bahola(ismlar):
    '''pop() metodidan foydalangan holda  va talabalar 
       royxatiga o'zgartirish kiritgan holda ishlanishi:'''
       
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
"""
# Way - B:
"""
def bahola(ismlar):
    ''' pop() metodidan foydalanmasdan va asl ro'yxatga ozgartirish 
        kiritmasdan faqat lugat qaytaradigan qilib ishlanishi'''

    baholar = {}
    for ism in ismlar[:]:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
"""

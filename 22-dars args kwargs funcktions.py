# 1 - masala
"""
# dinamic type: user-input

def multiply_all(*nums):
    '''Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing'''
    return sum(*nums)
numbers = []
while True:
    exitask = input("Are you done? (Y/n): ")
    if exitask.lower() == 'y':
        break
    else:
        number = int(input("\nEnter number: "))
        numbers.append(number)

print(multiply_all(numbers))
"""

# ------------------------

# 2 - masala

"""
# static type: dev-has-written

def student_datas(name, surname, **other_datas):
    '''
    Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya
    Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa 
    ixtiyoriy ko'rinishda istalgancha berilishi mumkin.
    '''
    other_datas["name"] = name
    other_datas["surname"] = surname

    return other_datas

student = student_datas("Ali", "Valiyev", age = 23, born_year = 1999, institute = "YTIT", faculty = "ISE")
print(student)
"""


    
# 1 - masala


def collect_data(curr_year, u_name, u_surname, u_born_year, u_born_city, u_email, u_age, u_phone):
    
    '''Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
    email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
    qaytaruvchi funksiya. Lug'atda foydalanuvchu yoshi ham bo'ladi.
    Ba'zi argumentlarni kiritish ixtiyoriy qilingan (masalan, tel.raqam, el.manzil)'''

    user_list = [] # user_list == clients []
    user_dict = {
        "curr_year": curr_year,
        "u_name": u_name,
        "u_surname": u_surname,
        "u_born_year": u_born_year,
        "u_born_city": u_born_city,
        "u_email": u_email,
        "u_age": u_age,
        "u_phone": u_phone
    }
    user_list.append(user_dict)
    return user_list

u_name = input("Enter name: ")
u_surname = input("Enter surname: ")
u_born_city = input("Enter  born city: ")
u_born_year = int(input("Enter born year: "))
curr_year = int(input("Enter current year: "))
ask_to_user = input("Do you want to enter your email too? (Y/n) (Not important) : ")
if ask_to_user.lower() ==  'y':
    u_email = input("Enter email: ")
elif ask_to_user.lower() ==  'n':
    u_email = "None"
    
ask_to_user2 = input("Do you want to enter phone number too? (Y/n) (Not important) : ")
if ask_to_user2.lower() ==  'y':
    u_phone = input("Enter phone number: +998 ")
elif ask_to_user2.lower() ==  'n':
    u_phone = "None"
u_age = curr_year - u_born_year

user_data = collect_data(curr_year, u_name, u_surname, u_born_year, u_born_city, u_email, u_age, u_phone)
for user in user_data:
    print(f"Name & surname: {user['u_name']} {user['u_surname']}\nBorn year: {user['u_born_year']}\nBorn city: {user['u_born_city']}\nAge: {user['u_age']}")






# ALMOST ALL THE STATEMENTS IN BOTTOM DOES'NT MATTER !!!

# while True:
#     u_choise = int(input("\n* * * * * * * * * * * * * *\nEnter what you want to:\n1) User registration;\n2) See users list\n3) Exit \n\nEnter: "))
#     if u_choise == 3:
#         print("****************** Program finished ******************")
#         break

#     elif u_choise == 2:
#         user_data = collect_data(curr_year, u_name, u_surname, u_born_year, u_born_city, u_email, u_age, u_phone)
#         for user in user_data:
#             print(f"Name & surname: {user['u_name']} {user['u_surname']}\nBorn year: {user['u_born_year']}\nBorn city: {user['u_born_city']}\nAge: {user['u_age']}")
#         print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
#         print(collect_data(curr_year, u_name, u_surname, u_born_year, u_born_city, u_email, u_age, u_phone))
#         break
#     elif u_choise == 1:
#         u_name = input("Enter name: ")
#         u_surname = input("Enter surname: ")
#         u_born_city = input("Enter  born city: ")
#         u_born_year = int(input("Enter born year: "))
#         curr_year = int(input("Enter current year: "))

#         ask_to_user = input("Do you want to enter your email too? (Y/n) (Not important) : ")
#         if ask_to_user.lower() ==  'y':
#             u_email = input("Enter email: ")
#         elif ask_to_user.lower() ==  'n':
#             u_email = "None"
        
#         ask_to_user2 = input("Do you want to enter phone number too? (Y/n) (Not important) : ")
#         if ask_to_user2.lower() ==  'y':
#             u_phone = input("Enter phone number: +998 ")
#         elif ask_to_user2.lower() ==  'n':
#             u_phone = "None"

#         u_age = curr_year - u_born_year



# -----------------------------

# 2 - masala

"""
user_list = [] # user_list == clients []
def collect_data():
    u_name = input("\nEnter name: ")
    u_surname = input("Enter surname: ")
    u_born_city = input("Enter  born city: ")
    u_born_year = int(input("Enter born year: "))
    curr_year = int(input("Enter current year: "))
    ask_to_user = input("\nDo you want to enter your email too? (Y/n) (Not important) : ")
    if ask_to_user.lower() ==  'y':
        u_email = input("Enter email: ")
    elif ask_to_user.lower() ==  'n':
        u_email = "None"
    ask_to_user2 = input("\nDo you want to enter phone number too? (Y/n) (Not important) : ")
    if ask_to_user2.lower() ==  'y':
        u_phone = input("Enter phone number: +998 ")
    elif ask_to_user2.lower() ==  'n':
        u_phone = "None"
    u_age = curr_year - u_born_year

    user_dict = {
                "curr_year": curr_year,
                "u_name": u_name,
                "u_surname": u_surname,
                "u_born_year": u_born_year,
                "u_born_city": u_born_city,
                "u_email": u_email,
                "u_age": u_age,
                "u_phone": u_phone
            }
    user_list.append(user_dict)

while True:
    u_choise = int(input("\n* * * * * * * * * * * * * *\nEnter what you want to:\n1) User registration;\n2) See users list\n3) Exit \n\nEnter: "))
    
    if u_choise == 1:

        collect_data()

    elif u_choise == 2:

        for user in user_list:
            print("\n * * * * * * * * * * * * * * * *\n")
            print(f"\nName & surname: {user['u_name']} {user['u_surname']}\nBorn year: {user['u_born_year']}\nBorn city: {user['u_born_city']}\nAge: {user['u_age']}")
            # print(user, end="\n")

    elif u_choise == 3:

        print("****************** Program finished ******************")
        break
"""

# -----------------------------

# 3 - masala
"""
def most_great(a, b, c):
    '''Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya'''

    return max(a, b, c)

num1 = int(input("Enter A: "))
num2 = int(input("Enter B: "))
num3 = int(input("Enter C: "))

print(most_great(num1, num2, num3))
"""

# -----------------------------

# 4 - masala
"""

import math

def circle_parametres(r):
    '''Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
    diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya '''
    diametr = 2 * r
    peremetr = 2 * math.pi * r
    surface = math.pi * r**2

    all_parametres = {
        "radius": r,
        "diametr": diametr,
        "peremetr": peremetr,
        "surface": surface
    
    }

    return all_parametres

radius = int(input("Enter circle's radius: "))

parametres = circle_parametres(radius)
for key, value in parametres.items():
    print(f"{key.title()} : {round(value, 3)}")

"""

# -----------------------------

# 5 - masala
"""
def find_primes(num1, num2):
    '''Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya'''
    prime_nums = list()
    for i in range (num1, num2 + 1):
        count_prime = 0
        for j in range (2, i+1):
            if i % j == 0:
                count_prime += 1
        if count_prime <= 2:
            prime_nums.append(i)
    return prime_nums          
            

a = int(input("Enter A: ")) # a == 15
b = int(input("Enter B: ")) # b == 20
print(find_primes(a, b))

"""

# -----------------------------

# 6 - masala
"""

def find_fibonacci(num):
    '''Foydalanuvchidan son qabul qilib,  shu son miqdoricha Fibonachchi 
        ketma-ketligi sonlar ro'yxatni qaytaruvchi funksiya'''

    #   Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng 
    # bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ich 
    # had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

    fobolist = []
    for i in range(num):
        if i == 0 or i == 1:
            fobolist.append(1)
        else:
            fobolist.append(fobolist[i-1] + fobolist[i-2])
    return fobolist



num = int(input("Enter number: "))
print(find_fibonacci(num))
"""
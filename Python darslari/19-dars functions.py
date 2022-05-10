# 1 - masala

"""
def count_age(user_name, user_age, curr_year):
    '''Foydalanuvchining yoshi va ismini so'rab, unga tugulgan yilinii chiqarib beruvchi funksiya'''

    result = f"\nHello {user_name}, You were born in {curr_year - user_age}."
    
    return result

user_name = input("\nEnter Your name: ")
user_age = int(input("\nEnter Your age: "))
curr_year = int(input("\nEnter current year: "))
print(count_age(user_name.title(), user_age, curr_year))
"""


# -----------------------------------

# 2- masala
"""
def find_cube(a):
    '''kiritilgan sonning kubi va kvadratini hisoblab beruvchi dastur'''
    result = f"The square of {a} is {pow(a, 2)};\nThe cube of {a} is {pow(a, 3)}"
    return result

num = int(input("\nEnter number: "))
print(find_cube(num), end="\n")
"""

# -----------------------------------

# 3- masala
"""
def is_even(a):
    '''kiritilgan sonning juft yo toqligini bilib beradigan funksiya'''
    if a % 2 == 0:
        return True
    else:
        return False
    
num = int(input("\nEnter number: "))
print(f"{num} is even" if is_even(num) == True else f"{num} is odd")
"""

# -----------------------------------

# 4 - masala
"""
def is_great(a, b):
    '''2 ta son kiritganda  ularni taqqoslab beradigan funksiya'''

    result = "Both numbers are equal to each other"
    if a > b:
        result = "Number - 1 is greater than number - 2"
    elif a < b:
        result = "Number - 1 is smaller than number - 2"
    return result
    

num1 = int(input("Enter number - 1 : "))
num2 = int(input("Enter number - 2 : "))
print(is_great(num1, num2))
"""

# -----------------------------------

# 5 - masala
"""
def count_power(a, b):
    '''A sonning B darajasini hisoblab beruvchi funktsiya'''
    result = pow(a, b)
    return result

num1 = int(input("\nEnter x : "))
num2 = int(input("\nEnter y : "))
print(f"\nThe {num2}th power of {num1} is {count_power(b = num2, a = num1)}\n")
"""

# -----------------------------------

# 6 - masala
"""
def count_power(a, b):
    '''A sonning B darajasini hisoblab beruvchi funktsiya. && B uchun qo'shimchalar kiritilgan.'''
    result = f"\nThe {num2}th power of {num1} is {pow(a, b)}"
    if b == 1:
        result = f"\nThe {b}st power of {a} is {pow(a, b)}"
    elif b == 2:
        result = f"\nThe {b}nd power of {a} is {pow(a, b)}"
    elif b == 3:
        result = f"\nThe {b}rd power of {a} is {pow(a, b)}"
    return result

num1 = int(input("\nEnter x : "))
num2 = int(input("\nEnter y : "))

print(count_power(b = num2, a = num1))
"""

# -----------------------------------

# 7 - masala
"""
def find_divisors(a):
    '''foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya'''
    for i in range(1,a):
        if a % i == 0:
            print(f"{i} can devide {a} without remnant")
        else:
            continue

num = int(input("Enter number: "))
print(f"Dividing signs for {num}: \n")
find_divisors(num)
"""
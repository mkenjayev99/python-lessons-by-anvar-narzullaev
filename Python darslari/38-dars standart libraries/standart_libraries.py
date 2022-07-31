import datetime as dt


# 1 - masala
'''
now = dt.datetime.now()
twoweekslater = dt.datetime(2022, 8, 18)

visual_time_now = now.strftime(f'%d.%m.%Y')
visual_time_twoweekslater = twoweekslater.strftime(f'%d.%m.%Y')


# print(visual_time_now)
# print(visual_time_twoweekslater)
day1 = 12
for day in range(day1, 22):
    visual_time_twoweekslater = twoweekslater.strftime(f'{day}.%m.%Y')
    print(visual_time_twoweekslater)
    # print(day, end="; ")
'''

# 2 - masala
'''
# 23.03.2023 - Ramadan
# 28.06.2023 - Qurban
#total secoonds - 8629; it stpits as: 2 hours, 23 minutes, 49 secoonds

thetoday = dt.datetime.now()
ramadan = dt.datetime(2023, 3, 23)
qurban = dt.datetime(2023, 6, 28)

differencein = ramadan - thetoday
secoonds = differencein.seconds
hours = int(secoonds/60/60)
minutes = int(secoonds/60 - hours*60)


differencein_2 = qurban - thetoday
secoonds_2 = differencein_2.seconds
hours_2 = int(secoonds_2/60/60)
minutes_2 = int(secoonds_2/60 - hours*60)

print(f"Total: {secoonds}\n* * * * * * * * * * * * * *  * ")
print(f'Ramazongacha {differencein.days} kun, {hours} soat, {minutes} minut qoldi')
print(f"* * * * * * * * * * * * * * * * * * * * * * * *\n\
Qurbon hayitigacha {differencein_2.days} kun, {hours_2} soat, {minutes_2} minut qoldi")
'''

# 3 - masala
# my birthday: 1999-02-18
"""
# Python program to check if year is a leap year or not

# year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# # century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# # not divided by 100 means not a century year
# # year divided by 4 is a leap year
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# # if not divided by both 400 (century year) and 4 (not century year)
# # year is not leap year
# else:
#     print("{0} is not a leap year".format(year))
"""

'''
# Function has not used
thetoday = dt.datetime.now()
birthday = dt.datetime(1999, 2, 18, 4, 5)
deltadays = thetoday - birthday # total days: 8561; it splits as 23 years, 5 months, 7 days
months = int((int(deltadays.days) - 366*6 - 365*17)/30)
year = int(int(deltadays.days)/365)
daays = int(int(deltadays.days) - 366*6 - 365*17 - months*30 - 3) # spesial calculation for myself

secoonds = int(deltadays.seconds)
hours = int(secoonds/3600)
minutes = int(secoonds - hours*3600)//60
last_s = int(secoonds - hours*3600 - minutes*60)

print(f"{deltadays.days} - Total days")
print(f"* * * * * * * * * *\n{year} - years;\n* * * * * * * * * *\n{months} - months; \n* * * * * * * * * *\n{daays} - days")
print(f"* * * * * * * * * *\n{hours} - hours\n* * * * * * * * * *\n{minutes} - minutes\n* * * * * * * * * *\n{last_s} - seconds")
'''
'''
# Function has used
def howMuchDays(year, month, day, hour, min):
    """
    Thie function tells you how much time you lived
    at this moment after you have input clear your 
    birth - year, month, day, hour.
    """
    thetoday = dt.datetime.now()
    birthday = dt.datetime(year, month, day, hour, min)
    deltadays = thetoday - birthday # total days: 8561; it splits as 23 years, 5 months, 7 days
    months = int((int(deltadays.days) - 366*6 - 365*17)/30)
    yeaar = int(int(deltadays.days)/365)
    daays = int(int(deltadays.days) - 366*6 - 365*17 - months*30 - 3) # spesial calculation for myself

    secoonds = int(deltadays.seconds)
    hours = int(secoonds/3600)
    minutes = int(secoonds - hours*3600)//60
    last_s = int(secoonds - hours*3600 - minutes*60)
    restring = f"* * * * * * * * * *\n{yeaar} - years;\n* * * * * * * * * *\n{months} - months; \n* * * * * * * * * *\n{daays} - days\n" 
    restring += f"* * * * * * * * * *\n{hours} - hours\n* * * * * * * * * *\n{minutes} - minutes\n* * * * * * * * * *\n{last_s} - seconds"
    return restring

whenuborn_year = int(input("Born year: "))
whenuborn_month = int(input("Born month: "))
whenuborn_day = int(input("Born day: "))
try:
    whenuborn_hour = int(input("Born hour: "))
except:
    whenuborn_hour = 0

try:
    whenuborn_minute = int(input("Born minute: "))
except:
    whenuborn_minute = 0
    

print(howMuchDays(whenuborn_year, whenuborn_month, whenuborn_day, whenuborn_hour, whenuborn_minute))
'''

# 4 - masala
'''
p_template = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
while True:
    phone_num = input("Enter your phone number: ")
    
    if re.match(p_template, phone_num):
        print("Phone number accepted :)")
        break
    else:
        print("Phone number doesn't match. Try again :|")
'''

# 5 - masala

import re

pattern1 = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)" #ishlamadi
pattern2 = "https://[a-z0-9_.\-]+\.[a-zA-Z0-9_\-/]+" #ishladi
pattern3 = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' #ishladi

full_text = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI \
    Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni \
        o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

the_result = re.findall(pattern3, full_text)
print(the_result)

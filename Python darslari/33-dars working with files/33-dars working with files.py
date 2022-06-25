# 1st step:

# file = open('learnedthings.txt')
# msg = file.read()
# print(msg)
# file.close()

# 2nd step:
# with open('data/pi32.txt', 'r') as file:
#     a = file.read()
#     print(a)


# 3rd step:

# with open('data/pi32.txt') as file: #faylni ochib uni ichidagi matnlarni string-object ko'rinishida qaytarish
#     pi = file.read() # faylni o'qish
#     pi = pi.rstrip() #string oralaridagi bo'sh joylarni olib tashlash
#     pi = pi.replace('\n', '') # keyingi qatorga ko'chiruvchini **hech narsa** bilan almashtirish
#     pi = float(pi) #sting tipidagi sonni float tipiga o'tkazish
#     print(pi) # va nihoyat float tipidagi son k-ekranga chiqadi


# 4th step:

# fname = 'learned_things.txt'
# with open(fname) as f:
#     for line in f:
#         if 'fayl' in line:
#             print(line)
#         else:
#             continue


# 5th step:

# n = 1
# found = 1
# with open('data/pi_million_digits.txt') as f:
#     for line in f:
#         if '19990814' in line: # 1999.08.14 sanani borligini pi_million_digits.txt faylidan qidiradi
#             print(f"{found}\n* * * * * * \n{line}\n* * * * * * *, ")
#             found += 1
#         else: 
#             n += 1
#             continue
#     print(n)

# 6th step:
import pickle


new_file = 'data/float_pickle'
with open('data/pi_million_digits.txt') as f:
    pi = f.read()
    # pi = pi.rstrip()
    pi = pi.replace('  ', '')
    pi = pi.replace('\n', '')
    pi = float(pi)
    # bu yerda print yozsa ham yozmasa ham console ga pi ni chiqarib yuborayapti

with open(new_file, 'wb') as f:
    pickle.dump(pi, f)

with open(new_file, 'rb') as f:
    binary1 = pickle.load(f)
    

print(binary1) # float qiymatni qaytaradi
print(type(binary1)) # tepadadgi binary1 ning tipi <class float ekan>
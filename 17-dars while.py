
# ---------------------------------------------------
# 1-masala
'''
books = []
print(f"type 'stop' for exit program\n**********************\n")
while True:
    q = input("Enter your lovely books: ").lower()
    if q == 'stop':
        break
    else:
        books.append(q.title())

    n = 0
for book in books:
    print(f"{n+1}. {book}")
    n +=1
print("**********************")
'''

# ---------------------------------------------------
# 2-masala
'''
while True:
    q = input("Enter your age: ")
    if q.lower() == 'quit' or q.lower() == 'exit':
        print("***************** The program finished *****************")
        break
    elif int(q) <= 7 and int(q) >= 0:
        print("The ticket price is 2000 sum for you")
    elif int(q) > 7 and int(q) <= 18:
        print("The ticket price is 3000 sum for you")
    elif int(q) > 18 and int(q) <= 65:
        print("The ticket price is 10000 sum for you")
    elif int(q) > 65:
        print("The ticket price is free for you")
    else:
        print("Enter real age! it is not real.")
'''

# ---------------------------------------------------
# 3-masala

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if float(qiymat) < 0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

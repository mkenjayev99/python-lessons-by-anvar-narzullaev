# -------------------------------
# 1-masala
'''
bookings = list()
while True:
    q = input("Enter product name: ")
    
    if q.lower() == "stop":
        break
    else:
        bookings.append(q.title())
n = 0
for item in bookings:
    print(f"{n+1}. {item}")
    n += 1
'''

# -------------------------------
# 2-masala
'''
market = dict()

while True:
    pro = input("Enter product name:")
    if pro.lower() == 'exit' or pro.lower() == 'quit' or pro.lower() == 'stop' or pro.lower() == 'leave':
        # print("*************** Program finished ***************\n")
        break
    else:
        pri = input("Enter it's price: ")
        market[pro] = int(pri)
n = 1
while True:
    wannasee = input("Are wanna see your products with prices? (Y/n): ")
    if wannasee.lower() == 'y':
        for pro, pri in market.items():
            print(f"{n}. {pro} price is {pri}")
            n += 1
        break
    elif wannasee.lower() == 'n':
        print("Okay. We will meet later ;) ")
        break
    else:
        print("You enterd wrong input! Try one more.")
'''

# -------------------------------
# 3-masala


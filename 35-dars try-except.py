summ = 0
x = 0
while True:
    try:
        n = int(input("Enter only integers: "))
        summ += n
        x += 1
        if x == 3:
            break
    except:
        x -= 1
        # pass
        print("Your input must be integer! ")
print(summ)
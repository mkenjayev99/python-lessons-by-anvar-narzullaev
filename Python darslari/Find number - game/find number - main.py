'''
Game - "Find the number"

Main file
'''

from random import randint


print("Let's play the 'Find my number' game!")
while True:
    print("I meant a number from 1 to 10. Can you find it?:")
    x = int(randint(1, 10))
    q = 1
    while True: #The computer meant a number. So the user need to find it. (Computer meanning side)
        y = int(input(">>> "))
        if y == x:
            print(f"THAT'S RIGHT! You found it in {q} attempts")
            break
        elif y < x:
            print(f"That's wrong. The number I thought was bigger than that.")
            q += 1
        elif y > x:
            print(f"That's wrong. The number I thought was Smaller than that.")
            q += 1
        elif y == str(y):
            print("You entered wrong input")
            q += 1

    print("Think a number from 1 to 10. I will try to find it.")
    ask_to_user2 = input(f"If you thought a number, press any key to continue.")
    q2 = 0
    supposed_nums = list()
    while True:
        x2 = int(randint(1, 10))
        if x2 not in supposed_nums:
            supposed_nums.append(x2)
            user_apply = input(f"Your number is {x2}: Right (r), Wrong (w): ")
            # It's bigger than that (+), It's smaller than that (-): 
            
            q2 += 1
            if user_apply.lower() == 'r':
                print(f"I found your number in {q2} attempts")
                break
            else:
                continue
        
            # if user_apply == '+':
            #     x2 = int(randint(x2+1, 10))
            #     if x2 not in supposed_nums:
            #         supposed_nums.append(x2)
            #         user_apply = input(f"Your number is {x2}: Right (r), It's bigger than that (+), It's smaller than that (-): ")
            #         q2 += 1
            #         if user_apply.lower() == 'r':
            #             print(f"I found your number in {q2} attempts")
            #             break
            # elif user_apply == '-':
            #     x2 = int(randint(1, x2-1))
            #     if x2 not in supposed_nums:
            #         supposed_nums.append(x2)
            #         user_apply = input(f"Your number is {x2}: Right (r), It's bigger than that (+), It's smaller than that (-): ")
            #         q2 += 1
            #         if user_apply.lower() == 'r':
            #             print(f"I found your number in {q2} attempts")
            #             break

    if q == q2:
        print(f"Score is {q} - {q2}. We are equal.")
    elif q < q2:
        print(f"Score is {q} - {q2}. You are Win.")
    elif q > q2:
        print(f"Score is {q} - {q2}. I am Win.")

    ask_to_user = int(input("Play again:?: Yes(1) / no(0): "))
    if ask_to_user == 1:
        continue
    elif ask_to_user == 0:
        break


    



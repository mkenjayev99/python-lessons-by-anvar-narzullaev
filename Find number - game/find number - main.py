'''
Game - "Find the number"

Main file
'''

import random

def computer_meaning_side(x=10): #computer think a number, then user will try to find it
    print("I meant a number form 1 to 10. Can you find it?")
    comp_num = random.randint(1, x)
    q = 0
    while True:
        q += 1
        user_supposed_num = int(input(">>> "))
        if comp_num < user_supposed_num:
            print("Incorrect. It's smaller than that. Try again.")
        
        elif comp_num > user_supposed_num:
            print("Incorrect. It's bigger than that. Try again.")
        
        else:
            print(f"CONGRATULATIONS! You found it in {q} attempts!") 
            break
    return q


def user_menaing_side(x=10): #user think a number, then computer will try to find it
    print("Now, you think a number from 1 to 10. I will try to find it.")
    q = 1
    lower_num = 1
    higher_num = x

    input("If you thought a number, press any key to continue: ")
    while True: 
        # for example: user thought 1.
        q += 1
        if lower_num == higher_num:
            comp_num2 = higher_num
        else:
            comp_num2 = int(random.randint(lower_num, higher_num))
        user_choise = input(f"You thought {comp_num2} : Right (R), It's smaller than that (-), It's bigger than that (+): ".lower())
                
        if user_choise == '+': # for example: comp printed 9
            lower_num = comp_num2 + 1
            
        elif user_choise == '-': # for example: comp printed 3
            higher_num = comp_num2 - 1

        else:
            print(f"YES! I found it in {q} attempts.")
            break
    return q

def main_func(x=10):
    ask_to_user = True
    while ask_to_user:
        supposes_comp = computer_meaning_side(x)
        supposes_user = user_menaing_side(x)

        if supposes_comp > supposes_user:
            print("I am win!")
        elif supposes_comp < supposes_user:
            print("You are win!")
        else:
            print("Both of us are winner!")

        ask_to_user = int(input("Let's play again? Yes(1) / no(0): "))
        
# main_func()

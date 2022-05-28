"""
Find the word - game

main function
( mine )
"""

from display import display
from get_word import get_word

def play():
    while True:
        word = get_word()
        word_letters = set(word)
        user_letters = ''

        print(f"I thought of {len(word)}-letter word. Can you find it?")
        while len(word_letters) > 0:
            print(display(user_letters, word))
            if len(user_letters) > 0:
                print(f"The letters you entered: {user_letters}")
            letter = input("Enter your letter: ").upper()

            if letter in user_letters:
                print("You entered this letter before, try again.")
                continue
            elif letter in word:
                word_letters.remove(letter)
                print(f"'{letter}' letter is right!")
            else:
                print(f"This '{letter}' letter is wrong. Try again.")
            user_letters += letter

        print(f"CONGRATULATIONS! You found '{word}' in {len(user_letters)} attempts.")

        x = int(input("\nPlay again? Yes(1) / no(0) : "))
        if x == 1:
            continue
        elif x == 0:
            print("\n***********Program finished***********")
            break
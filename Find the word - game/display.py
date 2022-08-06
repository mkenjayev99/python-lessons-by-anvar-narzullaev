def display(user_letters, word): # returns a <list> which contains some letters as <object>
    display_letter = ''
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += '-'
    return display_letter
    
def display(user_letter, word): # returns a <list> which contains some letters as <object>
    display_letter = ''
    for letter in word:
        if letter in user_letter.upper():
            display_letter += letter
        else:
            display_letter += '-'
    return display_letter
    
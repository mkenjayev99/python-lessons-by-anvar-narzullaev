def fibonaci(num):
    '''
    Berilgan son Fibonachchi ketma ketligida uchraydimi
    (True) yoki yo'q (False) qaytaruvchi f-ya
    '''
    fobolist = []
    n1, n2 = 0, 1
    count = 0
    if num <= 0:
        return True
    elif num == 1:
        return True
    else:
        while count < num+1:
            fobolist.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    if num in fobolist:
        return True
    else:
        return False

print(fibonaci(5)) # only for testing
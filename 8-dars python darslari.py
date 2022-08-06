#1-mashq
#izoh: men bilgan ba'zi davlatlarning ismlarini ro'yxatga kiritdim va konsolga chiqardim. va shu ro'yxatning uzunligini ham.

#davlatlar = ["O\'zbekiston", "Qozog\'iston", "Qirg\'iziston", "Turkmaniston", "Afg\'oniston", "Mo\'g\'iliston", "Amerika", "Rossiya", "Polsha", "Gruziya", "Arabiston", "Hindiston", "Turkiya", "Kambodja", "Braziliya"]
#print(davlatlar)
#print(len(davlatlar))

#2-mashq
#izoh: sorted() metodi yordamida 1-mashqdagi ro'yxatni tartiblangan holda ekranga chiqardim. Va xuddi shunday qilib teskari holatda ham.

#print('tartiblangan ro\'yxat:\n', sorted(davlatlar), '\n')
#print("teskari tartiblangan ro'yxat:\n", sorted(davlatlar, reverse=True), '\n')
#print("tartiblanmagan ro'yxat:\n", davlatlar)

#3-mashq
#izoh: sort() metodi yordamida ro'yxatni tartiblab konsolga chiqardim

#davlatlar = ["O\'zbekiston", "Qozog\'iston", "Qirg\'iziston", "Turkmaniston", "Afg\'oniston", "Mo\'g\'iliston", "Amerika", "Rossiya", "Polsha", "Gruziya", "Arabiston", "Hindiston", "Turkiya", "Kambodja", "Braziliya"]
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse = True)
#print(davlatlar)

#4-mashq
#izoh: reverse() metodi yordamida ro'yxatni teskari tuzulishda konsolga chiqardim

#davlatlar = ["O\'zbekiston", "Qozog\'iston", "Qirg\'iziston", "Turkmaniston", "Afg\'oniston", "Mo\'g\'iliston", "Amerika", "Rossiya", "Polsha", "Gruziya", "Arabiston", "Hindiston", "Turkiya", "Kambodja", "Braziliya"]
#davlatlar.reverse()
#print(davlatlar)

#5-mashq
#izoh: 'juft sonlar' degan ro'yxat yaratdim va range() metodi yordamida 120 dan 1200 gacha bo'lgan juft xonali sonlarni 2 qadam tartibi bilan ro'yxatga kiritdim va konsolga chiqardim. Ularning maksimum va minimum qiymatlarining ayirmasini komsolga chiqardim. ro'yxat uzunligini ham konsonlga chiqardim

#j_sonlar = list(range(120, 1201, 2))
#jami = int(sum(j_sonlar))
#print(j_sonlar)
#print('\nbarcha sonlar yig\'indisi:\n', jami)
#katta = max(j_sonlar)
#kichik = min(j_sonlar)
#print('\nmaksimum va minimum qiymatlarning ayirmasi:\n', katta - kichik)
#print('\nro\'yxat uzunligi:\n', len(j_sonlar))

#6-mashq
#izoh: ro'yxatning boshidagi oxiridagi va o'rtasidagi 20ta sonni konsolga chiqardim

#j_sonlar = list(range(120, 1201, 2))
#print("Boshidagi 20ta son\n", j_sonlar[:20], "\nO'rtadagi 20ta son\n", j_sonlar[260:280], "\nOxiridagi 20ta son:\n", j_sonlar[521:])

#7-mashq
#izoh: 'taomlar' degan ro'yxat yaratdim va 'nonushta' degan ro'yxatga uning elementlarini nusxaladim. Unga ba'zi elementlar qo'shdim, ba'zilarini o'chirdim. 'nonushta' ro'yxatini o'zgarmas ro'yxat ( tuple() ) qilib qo'ydim.

taomlar = ['Osh', 'Somsa', 'lag\'mon', 'tandir', 'Shashlik', 'Jiz']
nonushta = taomlar[:]
nonushta.append('sho\'rva')
del nonushta[5]
nonushta.insert(0, 'Mastava')
print('Ertalabki nonushtaga yeyish mumkin:\n', nonushta)
print("\nDastlabki taomlar:\n", taomlar)
nonushta = tuple(nonushta)
print("\nYangi nonushtaga ", nonushta, "larni yeyish mumkin")

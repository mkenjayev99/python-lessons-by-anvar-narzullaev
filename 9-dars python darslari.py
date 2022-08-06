#1-mashq
#izoh: 'ismlar' degan ro'yxat tuzdim va 'for' operatori va 'f - string' yordamida har bir ism uchun matnli xabarni konsolga chiqardim. Va kodning necha marta takrorlanganligini aytib o'tdim

#ismlar = ["Ali", "Vali", "Olim", "Damir", "Karim", "Oqil", "Odil"]
#for ism in ismlar:
#	print(f"Assalomu alaykum, yaxshimisan {ism}")
#print("kod", len(ismlar), "marta takrorlandi")

#2-mashq
#izoh: 10 dan 100 gacha bo'lgan hamma toq sonlar ro'yxatini tuzdim va har bir elementning kubini konsolga chiqardim

#sonlar = list(range(11, 100, 2))
#for t_son in sonlar:
#	print(f"{t_son} ning kubi {t_son**3} ga teng")

#3-mashq
#izoh: Foydalanuvchidan 6 ta eng sevimli kinolari ro'yxatini so'radim va uni 'kinolar' degan bo'sh ro'yxatga saqladim. Ro'yxatni konsolga chiqardim

#kinolar = []
#for n in range(7):
#	kinolar.append(input(f"eng sevimli {n + 1}-kinoyingiz nomini kiriting: "))
#print(kinolar)

#4-mashq
#izoh: bugun foydalanuvchidan nechta odam bilan suhbat qilganini so'radim va ular kimligini so'rab, ro'yxatga yig'ib konsolga chiqardim.

#1-usul:
#odam = input(f"Bugun nechta odam bilan suhbat qurdingiz?\n(sonning o'zini kiriting)>>> ")
#odamlar =[]
#for n in range(int(odam)):
#	odamlar.append(input(f"{n + 1}-odam kim edi?\n>>> "))
#print(odamlar)

#2-usul
#odam = int(input(f"Bugun nechta odam bilan suhbat qildingiz?\n(sonning o'zini kiriting)>>> "))
#odamlar = []
#for n in range(odam):
#	odamlar.append(input(f"{n+1}-odam kim edi?\n>>> "))
#print(odamlar)
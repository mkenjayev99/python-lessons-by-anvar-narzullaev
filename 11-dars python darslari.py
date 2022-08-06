#1-mashq
#izoh: 1-100 oraliqda juft sonlar ro'yxatini yaratdim va foydalanuvchidan 1-100 gacha bo'lgan sonlardan 1ta kiritishni so'radim, agar u ro'yxatda bor bo'lsa "Rahmat!", agar yo'q bõlsa "Juft son kiriting" degan natijani konsolga chiqardim

#j_sonlar = list(range(2, 101, 2))
#son = int(input(f"1 dan 100 gacha bo'lgan juft son kiriting: "))
#if son in j_sonlar:
#	print("Rahmat!")
#elif son not in j_sonlar:
#	print(f"Juft son kiriting!")

#2-mashq
#izoh: foydalanuvchidan juft son kiritishni sõradim va u agar juft son bõlsa, "Rahmat!", agar toq son bõlsa "Juft son kiriting!" degan natijani konsolga chiqardim

#son = float(input(f"Juft son kiriting: "))
#if son%2:
#	print("Bu juft son emas. Juft son kiriting!")
#else:
#	print("Rahmat!")

#3-mashq
#izoh: foydalanuvchilarni yoshiga ko'ra biletni narxini aytadigan dastur tuzdim

#1-usul
#x = int(input("Yoshingiz nechada?\n>>>"))
#if x<=4 or x>=60: print("Sizga kirish bepul")
#elif x<=18: print("Sizga kirish 10 000 so'm")
#elif x>18: print("Sizga kirish 20 000 so'm")

#2-usul
#yosh = int(input("Yoshingiz nechada? "))
#if yosh<4 or yosh>60:
#	narh = 0
#elif yosh<=18:
#	narh = 10000
#else:
#	narh = 20000
#print(f"chipta narxi {narh} so'm")

#4-mashq
#izoh: foydalanuvchidan 2ta son kiritishni so'rab, ilarning katta, kichik, yoki tengligini tekshirdim

#a = int(input("a sonni kititing: "))
#b = int(input("b sonni kiriting: "))
#if a>b: print("a son b sondan katta")
#elif a<b: print("a son b sondan kichik")
#else: print(" a va b sonlar teng")

#5-mashq
#izoh: 4-mashqdagidan boshqacharoq kod bilan topshirilgan natijani chiqardim

#x = float(input("1-son: "))
#y = float(input("2-son: "))
#if x>y: print(f"{x}>{y}")
#elif x<y: print(f"{x}<{y}")
#else: print("x=y")

#6-mashq
#izoh: 'mahsulotlar' degan ro'yxat yaratdim va 'savat' degan bo'sh rõyxat yaratdim. savatga foydalanuvchidan 5ta mahsulot nomini kiritishni so'radim. keyin, 'savat'dagi mahsulotlar bilan "mahsulotlar" dagi mahsulotlarni taqqoslab(bor yo'qligini tekshirib) konsolga chiqardim

#mahsulotlar = ["piyoz", "kartoshka", "sabzi", "go'sht", "karam", "bodring", "pomidor", "kadi", "qovoq", "guruch", "mosh", "loviya"]
#savat = []
#for n in range(5):
#	savat.append(input(f"{n+1}-mahsulotingizni kiriting: "))
#if savat:
#	for mahsulot in savat:
#		if mahsulot in mahsulotlar:
#			print(f"Do'konda {mahsulot} bor")
#		else:
#			print(f"Do'konda {mahsulot} yo'q")


#7-mashq
#izoh: Yuqoridagi mashqni quyidagicha o'zgartirdim. Foydalanuvchidan 6ta mahsulotmi so'radim. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shdim. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqardim

#mahsulotlar = ["piyoz", "kartoshka", "sabzi", "go'sht", "karam", "bodring", "pomidor", "kadi", "qovoq", "guruch", "mosh", "loviya"]
#savat = []
#for n in range(6):
#	savat.append(input(f"{n+1}-mahsulotingizni kiriting: "))
#bor_mahsulotlar = []
#mavjud_emas = []
#if savat:
#	for mahsulot in savat:
#		if mahsulot in mahsulotlar:
#			bor_mahsulotlar.append(mahsulot)
#		else:
#			mavjud_emas.append(mahsulot)
#if mavjud_emas:
#	print("Dõkonda quyidagi mahsulotlar yo'q: ")
#	for mahsulot in mavjud_emas:
#		print(mahsulot)
#else:
#	print("Siz so'ragan hamma mahsulotlar do'konimizda bor")

#8-mashq
#izoh: foydalanuvchilar degan ro'yxat tuzdim va foydalanuvchidan login tanlashni so'radim. keyin kiritilhan loginni ro'yxat ichidagi elementlar bilan solishtirib, agar ro'yxatda bo'lmasa "Xush kelibsiz" degan, agar ro'yxatda (mavjud) bõlsa "Login band, yangi login tanlang!" degan natijani konsolga chiqardim

#foydalanuvchilar = ["ali", "vali", "karim", "salim", "damir", "olim", "hasan", "husan"]
#login = input("Yangi login tanlang: ")
#if login.lower() in foydalanuvchilar:
#	print("Login band, yangi login tanlang!")
#else:
#	print("Xush kelibsiz", login)
	
#9-mashq
#izoh: Foydalanuvchidan butun son kiritishni so'radim va shu sonni 2dan 10 gacha bo'lgan sonlarga qoldiqsiz yoki qoldiqli bo'linishini aytib beradigan dastur tuzdim

#x = int(input("Butun son kiriting: "))
#for n in range(2,11):
#	if not (x%n):
#		print(f"{x} soni {n} ga qoldiqsiz bo'linadi")
#	else:
#		print(f"{x} soni {n} ga qoldiq bilan bo'linadi")

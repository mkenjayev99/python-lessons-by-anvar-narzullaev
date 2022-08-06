#1-mashq
#izoh: 'cars' degan ro'yxat yaratdim va if-else operatoridan foydalanib faqatgina 'gm' ni õzini katta harflarda, qolganini birinchi harfini bosh harflarda chiqadigan qildim

#cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
#for car in cars:
#	if car == "gm":
#		print(car.upper())
#	else:
#		print(car.title())
		
#2-mashq
#izoh: dastlabki mashqni 1-mashqdagi '==' amalining õrniga '!=' amali bilan bajardim

#cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
#for car in cars:
#	if car != "gm":
#		print(car.title())
#	else:
#		print(car.upper())
		
#3-mashq
#izoh: Foydalanuvchi login ismini so'radim va agar u 'admin' bo'lsa, "..., Foydalanuvchilar ro'yxatini ko'rasizmi?", agar oddiy foydalanuvchi bo'lsa, "..." degan javobni konsolga chiqardim

#f_ismi = input(f"Loginni kiriting: ")
#if f_ismi.lower() == "admin":
#	print(f"Xush kelibsiz {f_ismi.title()}. Foydalanuvchilar ro'yxatini ko\'rasizmi?")
#else:
#	print("Xush kelibsiz", f_ismi.title(), "!")

#4mashq
#izoh: foydalanuvchidan 2ta son kiritishni so'radim va agar sonlar teng bo'lsa, 'sonlar teng' degan natijani, agar biri boshqasidan katta bo'lsa, 1-si 2-sida yoki 2-si 1-sidan katta degan natijani konsolga chiqardim.

#a = int(input(f"1-sonni kiriting: "))
#b = int(input(f"2-sonni kiriting: "))
#if a == b: print("\nSonlar teng.")
#if a > b: print("\n1-son 2-sondan katta")
#if a < b: print("\n2-son 1-sondan katta")

#5-mashq
#izoh: Foydalanuvchidan istalgan son kiritishni so'radim va agar son<0 dan bòlsa, 'manfiy son'; agar son>0 dan bo'lsa 'musbat son' degan natijani konsolga chiqardim

#a = int(input(f"Istalgan son kiriting: "))
#if a == 0: print("Bu qiymat 0 ga teng.")
#if a > 0: print("Bu musbat son")
#if a<0: print(f"Bu manfiy son")

#6-mashq
#izoh: Foydalanuvchidan son kiritishni so'radim va agar u musbat bo'lsa sonning ildizini hisoblab konsolga chiqardim. agar son manfiy bo'lsa, "musbat son kiriting" degan natijani konsolga chiqardim

#a = int(input(f"sonni kiriting: "))
#if a >= 0: print(f"Sonning ildizi {a**(1/2)} ga teng")
#if a < 0: print("Musbat son kiriting!")
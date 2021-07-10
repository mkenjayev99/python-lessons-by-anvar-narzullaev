#1-mashq
#izoh: berilgan koddagi hatolarni topdim

#son = float(input("Juft son kiriting: "))
#if son%2:
#	print("Bu juft son emas!")
#else: print("Rahmat!")

#2-mashq
#izoh: berilgan koddagi hatolarni topdim

#yosh = int(input("Yoshingiz nechada? "))
#if yosh <= 0 or yosh >= 60:
#	narh = 0
#elif yosh < 18:
#	narh = 10000
#else:
#	narh = 20000
#print(f"Siz uchun chipta narhi {narh} so'm")

#3-mashq
#izoh: berilgan koddagi hatolarni topdim

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#	print(f"{x}={y}")
#elif x<y:
#	print(f"{x}<{y}")
#else:
#	print(f"{x}>{y}")

#4-mashq
#izoh: berilgan koddagi hatolarni topdim

#mahsulotlar = ["un", "tuxum", "yog'", "go'sht", "piyoz", "kartoshka", "banan", "uzum", "qovun"]
#savat = []
#for n in range(5):
#	savat.append(input(f"{n + 1}-mahsulotni kiriting: "))
#if savat:
#	for mahsulot in savat:
#		if mahsulot in mahsulotlar:
#			print(f"do'konimizda {mahsulot} bor")
#		else: print(f"dõkonimizda {mahsulot} yo'q")
#else: print("Savatingiz bo'sh")

#5-mashq
#izoh: berilgan koddagi hatolarni topdim

#mahsulotlar = ["tuxum", "un", "sariyog'", "olma", "banan", "uzum", "qovun", "kartoshka", "piyoz", "sovun"]
#savat = []
#for n in range(5):
#	savat.append(input(f"{n + 1}-mahsulotni qo'shing: "))
#	bor_mahsulotlar = []
#	mavjud_emas = []#yo'q_mahsulotlar
#for mahsulot in savat:
#	if mahsulot in mahsulotlar:
#		bor_mahsulotlar.append(mahsulot)
#	else:
#		mavjud_emas.append(mahsulot)
#if mavjud_emas:
#	print("Do'konimizda quyidagi mahsulotlar yo'q:\n")
#	for mahsulot in mavjud_emas:
#		print(mahsulot)
#else:
#	print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#6-mashq
#izoh: berilgan koddagi hatolarni topdim

#users = ["vali", "ali", "hasan", "husan", "salim", "karim"]
#login = input("Yangi login tanlang: ")
#if login.lower() in users:
#	print("Bu login band. Boshqa yangi login tanlang!")
#else: print("Xush kelibsiz")
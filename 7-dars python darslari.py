#3ta do'stimdan 2tasiga turli savollar bilan murojaat qildim

#ismlar = ["Abror", "Mahmud", "Qosim", 'Damir']
#print("Salom", ismlar[1], 'bugun bo\'shmisan?')
#print("Qandaysan", ismlar[0], "bugun choyxona nechchida edi?")

#1-mashq:
#izoh: Bunda sonlar ustida amallar bajardim.
#sonlar ro'yxati bilan ishlashni o'rgandim

#sonlar = [100, -202, 10.42, 12.0]
#sonlar[0] = sonlar[0] + 3
#sonlar[1] = -103
#sonlar[3] = sonlar[0] * sonlar[2]
#print("sonlardagi 0-qiymat 100 edi va u", #sonlar[0], "ga o'zgardi")
#sonlar.insert(2, 16)
#print("ro'yxatdagi qolgan sonlarning qiymati quyidagicha o'zgardi:\n", sonlar)

#2-mashq
#izoh: Bunda sonlar ustida amallar bajardim.

#sonlar = [100, -202, 10.42, 12.0]
#sonlar.pop(1)
#sonlar.append(34)
#sonlar.remove(10.42)
#print(sonlar)

#3-mashq
#izoh: 5-mashqning soddaroq ko'rimishini yaratdim. bunda f"** {*} ** " komanda/operatoridan foydalanmadim.

#olimlar = ["Imom Buxoriy", "Ilon Musk", "Abu Nasr Farobiy", "Jek Ma"]
#olim1 = olimlar.pop(0)
#olim2 = olimlar.pop(1)
#print("Men tarixiy olimlardan", olim1, "bilan, zamonaviy kishilardan esa", olim2, "bilan ko'rishishni istar edim")
#print("Men gaplashmoqchi bo'lgan ilmli odamlardan yana 2tasi", olimlar, "dir")

#4-mashq
#izoh: friends degan bo'sh ro'yxat tuzdim va unga mehmonga chaqirilgan do'stlarim ro'yxatini tuzib chiqdim. kela olmaydiganlarini esa .remove() va del operatorlari yordamida o'chirib tashladim.

friends = []
friends.append('Umid')
friends.append('Ulug\'bek')
friends.append("Nuriddin")
friends.append("Laziz")
friends.append("Mirkomil")
friends.append("Sarvar")
friends.append("Islom")
#print(friends)
friends.remove("Sarvar")
del friends[3]
#print(friends)
friends.insert(1, "Muhammadsarvar")
friends.append("Tohir")
friends.insert(0, "Elyor")
#print(friends)

#5-mashq
#izoh: tarixiy shaxslar va zamonaviy shaxslar degan 2ta ro'yxat tuzdim, ro'yxatdan men eng yaxshi ko'rgan 2ta imsonlarimni .pop() buyrug'i yordamida sug'urib olib konsolga chiqardim

#t_shaxslar = ["Imom Buxoriy", "Termiziy", "Xorazmiy", "Bahovuddin Naqshband", "Abdurrohman ibn Avf r.a."]
#z_shaxslar = ["Ilon Musk", "Jek Ma", "Stive Jobs", "Bill Gates", "Saud Abdulvahed"]
#print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, \nzamonaviy shaxslardan esa {z_shaxslar.pop(3)} bilan \ngaplashishni hohlar edim\n")

#6-mashq
#izoh: yangi 'mehmonlar' degan ro'yat ochdim va unga 'friends' ro'yxatidan bir nechta element ajratib olib qo'shdim. bu da pop() append() buyrug'i ichiga yozib, ikalasida  ham baravar foydalandim.

#mehmonlar = []
#mehmonlar.append(friends.pop(0))
#mehmonlar.append(friends.pop(1))
#mehmonlar.append(friends.pop(2))
#mehmonlar.append(friends.pop(3))
#mehmonlar.append(friends.pop(-1))
#print("Bugun bayramga", mehmonlar, "lar mehmon bo'lib kelishdi")
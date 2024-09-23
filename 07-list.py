# List type 
# print(len(my_list))

# len list ichidagi elementlar sonini chiqaradi

my_list = ["samandar", 19, 0.4]
# print(my_list[0])

# names = ["samandar", 'sardor', 'otabek']
# names.append("dilshod")
# print(names)
# append royxatning ohiriga element qoshadi

# names = ["samandar", 'sardor', 'otabek']
# names.insert(1, "dilshod")
# print(names)
# insert ro'yxatga indeks boyicha element qoshadi

# names = ["samandar", 'sardor', 'otabek']
# names.pop()
# print(names)
# pop ro'yxatning ohiridan boshlab elementni o'chiradi

# names = ["samandar", 'sardor', 'otabek']
# names.remove("sardor")
# print(names)
# remove ro'yxatning orasidan tanlab olib elementni o'chiradi

# mevalar = ['olma', 'anor', 'orenge']
# mevalar.insert(0, "banana")
# print(mevalar)
# insert indeks bo'yicha ro'yxatga element qo'shadi

# sanoq = [2, 4, 1, 5, 3, 8, 2]
# sanoq.sort()
# print(sanoq)
# sort bizga elementlarni tartib bilan tahlaydi


# sanoq = [2, 4, 1, 2, 5, 3, 8]
# sanoq.sort()

# sanoq.reverse()
# reverse bizga elementlarni teskari tartib bilan tahlaydi

# newlist = sanoq.copy()
# copy yangi o'zgaruchiga copy qiladi 


# print(newlist.count(2))
# caunt royxatdagi elementlar nechtaligini chiqaradi

# sanoq = [2, 4, 1, 2, 5, 3, 8]
# mevalar = ['olma', 'anor', 'orenge']

# mevalar.extend(sanoq)
# print(mevalar.index(3))
# extend bizga 2 ta listni 1 taga jamlab beradi 
# index lestdagi elementni nechanchi indexdaligini aniqlaydi

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] #mevalar royxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yhat
# ismlar = [] # bosh royhat

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print("Birinchi meva:",mevalar[0].title())
# print("Ikkinchi meva:",mevalar[1].upper())

# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[0] + narhlar[1])

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1])

# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1 - qiymatni 13000 ga o'zgartirdik
# narhlar[2] = 11000 # 3 - qiymatni 11000 ga o'zgartirdik
# narhlar[3] = narhlar[3] + 2000 # 4 qiymatga 2000 qo'shdik
# print(narhlar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append('tarvuz')
# print(mevalar)

# cars = [] # bo'sh ro'yhat
# cars.append('lacetti') # royhatga lacetti qoshildi
# cars.append('Nexia 3') # royhatga nexia 3 qo'shildi
# cars.append('Cobalt') # ro'yhatga cobalt qo'shildi
# print(cars)

# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1- o'ringa Malibu qoshildi
# print(cars)
# cars.insert(2, 'Damas') # 3 - o'ringa Damas qo'shildi
# print(cars)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1]
# print(mevalar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli')
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', "qo'y", 'quyon', 'mushuk']
# hayvonlar.remove('mushuk')
# print(hayvonlar)

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3)
# print(f"Men {mahsulot.title()} sotib oldim")
# print(f"Olinmagan mahsulotlar: {bozorlik}")

# AMALIYOT

# ismlar = []
# ismlar.append('Bolat')
# ismlar.append('Diyorbek')
# ismlar.append('Abdulatif')
# ismlar.append('Nurken')

# xabar = (f"Salom {ismlar[0]}, bugun kontir bormi?\n{ismlar[1]}, tug'ilgan kunga boramizmi?")

# print(xabar)
# ismlar = ['Bolat', 'Diyorbek', 'Abdulatif', 'Nuken']
# print(f"Salom {ismlar[0]} ishlaring yaxshimi? ")
# print(f"{ismlar[1]} va {ismlar[-1]} sirdoshlar")
# print(f"{ismlar[2]} bugun tug'ilgan kunga borasanmi?")

# sonlar = [12, 88, -45, 34.6, 99, 14]
# print(sonlar)
# sonlar[0] = sonlar[0] + sonlar[1]
# sonlar[1] = 888
# sonlar[2] = 45
# sonlar[-1] = 140
# print(sonlar)

# t_shaxslar = ['Islom Karimov', 'Alisher Navoiy', 'Amur Temur']
# z_shaxslar = ["Ilon Musk", 'Mark Sucerburg', 'Bill Geyts']

# t_shaxs = t_shaxslar.pop(0)
# z_shaxs = z_shaxslar.pop(1)

# print(f"""Men tarixiy shaxslardan {t_shaxs} bilan,
# zamonaviy shaxslardan esa {z_shaxs} bilan 
# suhbat qilishni istar edim.""")

friends = []
friends.append('Bolat')
friends.append('Diyorbek')
friends.append('Abdulatif')
friends.append('Nurken')
friends.append('Aybek')
print(friends)

friends.remove('Nurken')
friends.remove('Abdulatif')
print(friends)

friends.insert(0, 'Javlon')
friends.insert(-1, 'Bekmurod')
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
print("\nKelgan mehmonlar: ", mehmonlar)


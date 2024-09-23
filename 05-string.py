# str yani string
# f stringni ham o'rganamiz


x = 'salom'
name = "Samandar"
# print(f"salom {name} xush kelibsiz botimizga")

# f stiring f dan keyin qoshtirnoq ochamiz va 
# # jingalak qavs ichida o'zgaruvchi yozsak bo'ladi

# nametwo = "Samandar"
# age = '20'

# datatext = """ahgaighagha;oghagh
# ajoghoahgoahgoa
# gagahoghoaerhgaerohg"""


# print(datatext)

# vatan = 'uzbekistan'
# print(vatan.upper()) # upper() hamma harflarni katta qilib beradi

# vatan1 = 'AvgoNisTON'
# print(vatan1.lower()) # lower() hamma harflarni kichiq qilib beradi

# vatan2 = 'Turk,me,nis,ton'
# vatan3 = vatan2.split(',')
# print(vatan3) # split bizga strdan list yasab beradi 

x = 10
x = str(x)
# print(type(x))
# str() boshqa turdagi qiymatni intga aylantiradi

ismi = 'samandar yoshi {yoshi:} ga teng'
# print(ismi.format(yoshi = '20'))
# format str ichiga ozgaruvchi yozishimizda kerak boladi

# len funksiyasi

# lens = "fakbgiaiarbgierhgraegore"

# print(f"So'zlarning soni {len(lens)} ta")

# len bizga elementlarning sonini aniqlab beradi

# replace metodi
# df = 'asi.,l'
# df = df.replace(",", "").replace(".", "")
# print(df)

x = "ajdsbgigbuieargm,galhgoa.....gohgoeammm,,,,jaogh."
x = x.replace(",", "").replace(".", "")
# print(f"kampyuterdan egallagan joyi {len(x)} bayt")

# vazifa strni qolgan methonlarini takrorlash

# String (matn)

shahar = "кукон"
viloyat = 'фаргона'

# print(shahar, viloyat)

matn = "Men yangi 🌑 sotib oldim"
# print(matn)

ism = 'Ahmad'
# print("Mening ismim " + ism)

ism = 'Ahad'
familiya = 'Qayum'
# print(ism + familiya)
# print(ism + ' ' + familiya)
ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

ism = "James"
familiya = "Bond"
# print(f"Salom, mening ismim {ism}. {ism} {familiya}")

# print('Hello World!')
# print('Hello \tWorld!')
# print('Hello \nWorld!')

# upper() va lower() metodlari

# ism = 'Ahad'
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())
# print(ism_sharif.lower())

# title() va capitalize() metodlari

# ism_sharif = 'james bond'
# print(ism_sharif.title())

# ism_sharif = 'james bond'
# print(ism_sharif.capitalize())

# strip(), rstrip() va lstrip() metodlari

# meva = "    olma    "
# print(meva)
# print(f"Men {meva.lstrip()} yaxshi ko'raman")
# print(f"Men {meva.rstrip()} yaxshi ko'raman")
# print(f"Men {meva.strip()} yaxshi ko'raman")
# print(f"Men {meva} yaxshi ko'raman")

# input funksiyasi

# ism = input("Ismingiz nima?")
# print("Assalomu aleykum, ", ism)

# ism = input("Ismingiz nima?\n>>>")
# print('Assalomu aleykum,', ism.title())

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# kocha = input("Kochangiz: ")
# mahalla = input("Mahallangiz: ")
# tuman = input("Tumaninggiz: ")
# viloyat = input("Viloyatingiz: ")
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# kocha = input("Kochangiz: ")
# mahalla = input("Mahallangiz: ")
# tuman = input("Tumaninggiz: ")
# viloyat = input("Viloyatingiz: ")
# print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")

# kocha = input("Kochangiz: ")
# mahalla = input("Mahallangiz: ")
# tuman = input("Tumaninggiz: ")
# viloyat = input("Viloyatingiz: ")
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil)

# kocha = "bog'bon"
# mahalla = "sog'bon"
# tuman = "bodomzor"
# viloyat = "samarqand"
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.title())
# print(manzil.capitalize())


# a = 20 
# b = -30
# c = a + b
# print(c)

# Kvadratning yuzini hisoblaymiz 
# kvdrt_tmni = 20 # Kvadratning tomoni 20 ga teng
# kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
# print(kvdrt_yuzi)

# pi = 3.14159 # o'nlik son (float)
# radius = 10 # butun son (integer)
# diametr = 2*radius
# print(f"Aylana uzunligi {pi*diametr} ga teng")

a = -20
b = 40
c = b/a
# print(c) # natija o'nlik son bo'ladi

a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil bo'ladi
# print(a + b)
# print(a * b)
# print(a ** b)
# print(2*(a+b))

aholi_soni = 7_594_819_426 # o'zimiz tushunishimiz uchun shunday yozilgan
# print(f"Yer kurrasida {aholi_soni} ga yaqin odam yashaydi")

# KONSTANTA -> konstanta qiymat katta harflar bilan belgilanadi va uni o'zgartirish mumkin emas
PI = 3.14159
radius = 21.2

x, y, z = 10, -7.35, -30
# print(x,y,z)

# ism = 'Jobir'
# yosh = 36
# print(type(ism))
# print(type(yosh))
# xabar = f"{ism} {yosh} yoshda"
# # print(xabar)
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)

# str() -> int yoki float qiymatlarni strga o'zgartiradi
# int() -> float yoki str sonli qiymatlarni intga o'zgartiradi
# float() -> int yoki str sonli qiymatlarni floatga o'zgartiradi

# INPUT() va Sonlar
# input() funksiyasi foydalanuvchidan qabul qilgan qiymatni str qilib saqlaydi

# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2024 - t_yil
# print(f"Siz {yosh} yoshda ekansiz")

# t_yil = input("Tug'ilgan yilingizni kiriting: ")
# t_yil = int(t_yil)
# yosh = 2024 - t_yil
# print(f"Siz {yosh} yoshda ekansiz")

# Amaliyot
# 1. Kiritilgan sonning kvrati va kubini 

# son = int(input("Istalgan butun son kiriting: "))
# print(f"{son} ning kvadrati {son**2} ga teng")
# print(f"{son} ning kubi {son**3} ga teng")

# 2. Yoshni so'rab t_yilini hisoblab beramiz

# yosh = int(input("Yoshingiz nechida?\n>>>"))
# t_yil = 2024 - yosh
# print(f"Siz {t_yil} - yilda tug'ilgansiz")

# 3. Sonlarning yig'inidsi, ayirmasi, ko'paytmasi va bo'linmasini hisoblaymiz

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
print(f"{son1} + {son2} = ", son1+son2)
print(f"{son1} - {son2} = ", son1-son2)
print(f"{son1} * {son2} = ", son1*son2)
print(f"{son1} / {son2} = ",son1/son2)

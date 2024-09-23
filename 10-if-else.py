# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism = 'Ali'
# ism == 'Ali' # True
# ism == 'Vali' # False
# ism == 'ali' # False

# ism = input("Ismingiz nima?\n>>")
# if ism.lower() != 'ali':
#     print(f"Uzr, {ism.title()} biz Alini kutayabmiz.")
# else:
#     print("Salom, Ali")

# javob = float(input("12x6 nechiga teng?>>>"))
# if javob != 72:
#     print("Javob xato!")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh >= 18:
#     print("Xush kelibsiz!")
# else:
#     print("Sizga kirish mumkin emas!")

# login = input("Yangi login tanling: ")
# if len(login)<=5:
#     print("Login 5 harfdan ko'proq bo'lishi shart!")

# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2024 - yil < 18:
#     print(f"Yoshingiz {2024-yil} da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz.")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# x, y = 255, 50
# print("x>y") if x>y else print('x<y')

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# login = input("Login kiriting: ")
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin.\nFoydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print("Xush kelibsiz, ",login.title())

# print("2 ta son kiriting")
# son1 = float(input('1 - son: '))
# son2 = float(input('2 - son: '))
# if son1 == son2:
#     print("Sonlar teng")

# son = float(input("Istalgan son kiriting: "))
# if son < 0:
#     print("Son manfiy")
# else:
#     print('Son musbat')

# son = int(input("Istalgan son kiriting: "))
# if son > 0:
#     print(son**(1/2))
# else:
#     print("Musbat son kiriting")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4:
#     print('Sizga kirish bepul')
# elif yosh <= 12:
#     print("Sizga kirish 5000 so'm")
# else:
#     print("Sizga kirish 10000 so'm")

# yosh = int(input('Yoshingizni kiriting: '))
# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# else:
#     narh = 10000

# print(f"Sizga kirish {narh} so'm")

# kun = input("Bugun nima kun?>>>")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print('Bugun ish kuni.')

# kun = input('Bugun nima kun?>>>')
# harorat = int(input("Havo harorati qanday?>>>"))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("Cho'milgani kettik!")
# elif kun.lower() == 'yakshanba' and harorat < 30:
#     print('Uyda dam olamiz.')

# kun = input("Bugun nima kun?>>>")
# harorat = float(input("Havo harorati qanday?>>>"))
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")

# narh = 15000
# choy = True
# salat = False

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000

# print(f"Jami {narh} so'm")

# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kampot = 0
# assorti = 1

# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 3000
# if kampot:
#     print("Mijoz kampot oldi.")
#     narh = narh + 5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 20000

# print(f"Jami {narh} so'm")

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# print(menu)
# print('manti' in menu) # manti menuda yoq
# print('osh' in menu) # osh menuda bor
# # in royxatni ichida borligini tekshirib beradi

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print(f"{ovqat.title()} afsuski menuda qo'q.")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# print(menu)
# print('manti' not in menu) # manti menyuda yoqmi aslida yoq shunga True
# print('osh' not in menu) # osh menyuda yoqmi aslida bor shunga False
# # not in royxatni ichida yoqligini tekshirib beradi

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print("Afsuski bizda bunday ovqat yo'q")
# else:
#     print("Buyurtma qabul qilindi")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh")

# son = int(input('Juft son kiriting: '))
# if son%2 == 0:
#     print(f"Juft son kiritdingiz: {son}")
#     print("Rahmat!")
# else:
#     print(f"Juft son kiriting: {son}")
#     print("Bu juft son emas")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4 or yosh > 60:
#     narh = 0
# elif yosh <= 18:
#     narh = 10000
# elif yosh > 18:
#     narh = 20000
# print(f"Sizga kirish {narh} so'm")

# x = int(input('Birinchi sonni kiriting: '))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print(f"{x} = {y}")
# elif x > y:
#     print(f"{x} > {y}")
# else:
#     print(f"{x} < {y}")

# mahsulotlar = ['un', 'kartoshka', 'piyoz', 'shakar', 'moy', 'guruch', 'qalampir', "yog'", 'makaron', 'tuxum']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
    
# for mahsulot in savat:   
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot.title()} do'konimizda bor.")
#     else:
#         print(f"{mahsulot.title()} do'konimizda yo'q.")

# mahsulotlar = ['un', 'kartoshka', 'piyoz', 'shakar', 'moy', 'guruch', 'qalampir', "yog'", 'makaron', 'tuxum']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# foydalanuvchilar = ['anvar', 'komil', 'husniddin', 'alibek', 'bubur']
# login = input("Yangi login tanlang: ")
# if login.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang")
# else:
#     print(f"Xush kelibsiz, {login.title()}")

# son = int(input("Birorta butun son kiriting: "))

# for n in range(2,10):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
        
# ism = 'Samandar'
# if ism == 'samandar':
#     print("Salom mijoz botimizga hush kelibsiz!")
# else:
#     print("Mijoz ismini to'g'ri kiriting!")

# x = input()

# if x == 'salom':
#     print('salom xush kelibsiz')
# elif x == 'samandar':
#     print('Samandar xush kelibsiz')
# elif x == "end":
#     print('dastur yakunlandi degan yozuv chiqsin ')
    
# a = 22
# b = 22

# if b > a:
#     print(f"{b} > {a}")
# elif b < a:
#     print(f"{b} < {a}")
# else:
#     print(f"{a} == {b}")

# x = int(input("1-sonni kiriting: "))
# amal = input("amalni tanlang (+, -, *, /): ")
# y = int(input('2-sonni kiriting: '))

# if amal == '+':
#     print(f"{x} + {y} = ", x + y)
# elif amal == '-':
#     print(f"{x} - {y} = ", x - y)
# elif amal == '*':
#     print(f"{x} * {y} = ", x * y) 
# elif amal == '/':
#     print(f"{x} / {y} = ", x / y)
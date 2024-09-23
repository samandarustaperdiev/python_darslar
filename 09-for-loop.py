# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# print(mehmonlar)

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)

# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = []
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

# ismlar = ['obit', 'javohir', 'akmal', 'ziyot', 'momin']
# for ism in ismlar:
#     print(f"Salom {ism.title()}")
# print(f"Kod {len(ismlar)} marta takrorlandi")

# for son in range(11,100,2):
#     print(f"{son} ning kubi {son**3} ga teng")

# kinolar = []
# print("5 ta eng sevimli kinongizni kiriting.")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1} - kinoni kiriting: "))
# print(kinolar)

# insonlar = []
# sonlar = int(input("Bugun necha kishi bilan suhbat qildingiz?>>>"))
# for son in range(sonlar):
#     insonlar.append(input(f"{son+1} - suhbat qilgan odamingiz kim edi: "))
# print(insonlar)

# my_list = [1, 2, 3, 4]
# for i in my_list:
#     print(i)

# fruits = ['orange', 'apelsin', 'lemon','tarvuz']
# for x in fruits:
#     print(x)

# for i in 'samandar':
#     print(i)

# name = ['samandar', 'akmal', 'sardor', 'asil']
# for i in name:
#     if i == 'asil':
#         break
#     print(i)

# name = ['samandar', 'akmal', 'sardor', 'asil']
# for i in name:
#     if i == 'akmal':
#         continue
#     print(i)

# son = float(input("Juft son kiriting: "))
# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu juft son emas.")

# yosh = int(input("Yoshingiz nechida?>>>"))

# if yosh <= 4 or yosh >= 60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))

# if x == y:
#     print(f"{x} == {y}")
# elif x > y:
#     print(f"{x} > {y}")
# else:
#     print(f"{x} < {y}")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

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
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
      
# users = ['alisher1983', 'aziza', 'yasina', 'umar']

# login = input('Yangi login tanlang: ')

# if login in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print("Xush kelibsiz!")
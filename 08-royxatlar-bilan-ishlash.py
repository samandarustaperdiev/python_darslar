
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:",sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:",mehmonlar)
# print(sorted(mehmonlar, reverse=True))

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# fruits.reverse()
# print(fruits)

# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# print("Elementlar soni:", len(fruits))

# sonlar = list(range(0,10))
# print(sonlar)

# juft_sonlar = list(range(0,20,2))
# toq_sonlar = list(range(1,20,2))
# print('Juft sonlar:', juft_sonlar)
# print('Toq sonlar:', toq_sonlar)

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print(f"Eng arzon narh: {arzon}, eng qimmat narh: {qimmat}, jami narh: {jami}")

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3]
# print(my_cars)
# print(cars)
# print(cars[2:5])
# print(cars[:4])
# print(cars[2:])

# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar 
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yxati:",sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar[:]
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lezard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys = ('bus','car','bear','dino','snake','lizard')
# toys = list(toys)
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys)
# print(toys)

# AMALIYOT

davlatlar = ['Rassia', 'Amerika', 'Turkiya', 'Germaniya', 'London', 'Belarusiya']
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar,reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
juft_sonlar = list(range(120,1200,2))
print(juft_sonlar)
yigindi = sum(juft_sonlar)
print(yigindi)
katta = max(juft_sonlar)
kichik = min(juft_sonlar)
print(katta - kichik)
print(len(juft_sonlar))
print(juft_sonlar[:21])
print(juft_sonlar[-20:])
print(juft_sonlar[260:281])

taomlar = ['osh', 'norin', 'beshbarmoq', 'dolma', 'shorva']
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove('norin')
nonushta.remove('shorva')
nonushta.append('manti')
nonushta.insert(2, 'bishteks')
print("Taomlar ro'yxati:", taomlar)
print("Nonushta ro'yxati:",nonushta)
nonushta = tuple(nonushta)
print(nonushta)

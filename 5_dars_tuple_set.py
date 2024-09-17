"""
Thame: O'zgarmas ro'yhat(Tuple), Set
""" 

"""
Pythonda 4 turdagi ma'lumotlar to'plami mavjud:
List  - Ro'yhat	[]
Tuple - O'zgarmas ro'yhat ()
Set   - Aralash ro'yhat {}
Dictionary - Lug'atlar {}
"""

""" 
Tuple - o'zgarmas ro'yhatlar
Tuple - o'zgarmas ro'yhatlarga element qo'shib bo'lmaydi,
ularni o'zgartirib yoki o'chirib bo'lmaydi.
Tuple elementlari har qanday turdagi ma'lumotlarga ega bo'lishi mumkin:
"""
# ismlar = ["Olim","Anvar", "Rustam"]
# familyalar = ("Xasanov", "Husanov","Abdulayev")
# print(type(ismlar))
# print(type(familyalar))

# ismlar.append("Aziz")
# print(ismlar)

# familyalar.append("Ismatov") # ishlamaydi
# print(familyalar)

"""" list(), tuple() funksiyalari """
# print(type(familyalar))# tuple turidagi ro'yhatni oddiy ro'yhat shakliga o'tkazamiz
# familyalar = list(familyalar)
# print(type(familyalar))

# familyalar.append("Ismatov")# ro'yhatimizga yangi element qo'shamiz
# print(familyalar)

# familyalar = tuple(familyalar)# list turidagi ro'yhatimizni o'zgarmas ro'yhat shakliga o'tkazamiz
# print(type(familyalar))

""" tuple yaratish """
# meva = ("apple","dfdf")
# print(type(meva))

# meva = ("apple") # tuple emas
# print(type(meva))

""" tuple ni o'chirish """
# del meva
# print(meva)
# print(meva) # bu xatolik keltirib chiqaradi, chunki endi "meva" degan ro'yhat yo'q

""" tuple larni qo'shish """
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)


""" 
<--- Set --->
Set tartibsiz , o'zgarmas va indekslanmagan to'plamdir.
Set elementlarini o'zgartirish mumkin emas, lekin  elementlarni olib tashlash va yangi elementlar qo'shish mumkin.
Set tartibsiz, shuning uchun elementlar qaysi tartibda bo'lishi aniq emas.

"""
# myset = {"apple", "banana", "cherry", "lime", "melon", "apple", "orange"} # ikkita bir xil emelent printda chiqmaydi
# print(myset)
# print(type(myset))

""" set() funksiyasi """
# name = ("ali", "vali", "olim")
# print(name)
# print(type(name))

# name = set(name)
# print(name)
# print(type(name))

""" add() funksiyasi """
# name = {"ali", "vali", "olim"}
# name.add("hasan")
# print(name)

""" elementni o'chirish .remove() va .discard()"""
# name.remove("ali") # Agar o'chiriladigan element mavjud bo'lmasa remove() xato beradi
# print(name)

# name.discard("aziz") # descard() esa xato bermaydi
# print(name)

""" del va .clear()"""
# name.clear()
# print(name)

# del name
# print(name) # xatolik yuzaga keladi !!!

""" Ikki set ni qo'shish / union(), update() funksiyalari"""
# name1 = {"Abbos", "Ahmad", "Anvar"}
# name2 = {"Bobur", "Bahrom"}

# name3 = name1.union(name2) # ikkita set ni qo'shib 3-yangi set ni yaratadi
# print(name3)

# name1.update(name2)
# print(name1)

# name2.update(name1)
# print(name2)

"""
<--- Vazifa --->
1) oila deb nomlangan bo'sh o'zgarmas ro'yhatlarga(tuple) o'z oila azolaringizni ismini qo'shing va konsulga chiqaring.com
	-so'ng oila azolarimizning 2 tasini ismini ro'yhatdan o'chirib tashalng va qolgan ismlarni konsulga chiqaring;
	-keyin esa qolgan ismlarni tahrirlab ularni familyasini ham qo'shing --> "Ali" > "Olimov Ali" . va konsulga chiqaring;
	-so'ngra avval o'chirib yuborgan ismlaringizni qaytadan ro'yhatgfa qo'shing va ularni ham konsulga chiqaring;

2) musbat_sonlar va manfiy_sonlar degan ikkita ro'yhat(list) yarating. so'ngra ularni birlashtirib yangi 'sonlar' deb nomlangan
	ro'yhat yarating.
	-so'ngra ushbu ro'yhatni o'zgarmas ro'yhat shakliga keltiring va konsulga shu ro'yhatni va uning turini chiqaring;
	-keyin shu ro'yhatni o'chirib tashlang va uni qaytadan konsulga chiqarishga urinib ko'ring;

3) ismlar deb nomlangan ro'yhat(list) va sonlar deb nomlangan o'zgarmas(tuple) ro'yhat yarating va ularni avval har birini keyin esa 
	birlashtirib ularning tuirni set ga almashtiring.

4) mevalar deb nomlangan ro'yhat(list ) yarating. Avval uni o'zgarmas ro'yhat turiga , keyin esa set turiga o'zgartiring va konsulga ularning 
turini chiqaring.
	-remove() yordamida 3 ta discard() yordamida 3 ta elementni o'chirib tashlang va ro'yhatni konsulga chiqaring.
	-va yangi 5 ta element qo'shing va ro'yhatni konsulga chiqaring;
	-so'ngra ro'yhatni tozalang va uni konsulga chiqaring;
	-keyin esa ro'yhatni o'chirib tashlang;

5) yuqorida yaratgan musbat_sonlar va manfiy_sonlar ro'yhatlarimizni set ko'rinishiga olib o'ting.
	-ularni sonlar degan yangi set ga birlashtiring va konsulga chiqaring;
	-har ikkolovida mavjud elementlarni avval musbat_sonlar setiga keyin esa manfiy_sonlar setiga birlashtirib, 
		har ikkolovini konsulga chiqaring;
"""


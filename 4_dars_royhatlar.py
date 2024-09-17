"""
Thame: Ro'yhatlar(Lists)
"""  

""" Element, Index"""

"""
mevalar = ["olma", 'gilos', "o'rik", "olcha"]
              0       1        2        3
             -4      -3       -2       -1

-3 -2 -1 0 1 2 3 4
"""

# mevalar = ["olma", 'gilos', "o'rik", "olcha"]
# print(mevalar)
# print(mevalar[0])
# print(mevalar[1])
# print(mevalar[3])
""" Ro'yhat turlari """
# ismlar = ["Ali", 'Olim', "Anvar", "Abbos"]
# sonlar = [3,57,-6,0,54,8]
# darslar = ["Pyhton", "Django", 3, 10]
#bosh_royhat = []
# list = list(("apple", "banana", "cherry"))

# print(ismlar)
# print(sonlar)
# print(ismlar[0], ismlar[2], ismlar[3])
# print(ismlar[-4], ismlar[-2], ismlar[-1])
# print(ismlar[0:3])
# print(list)
# print(f"Biz  o'quv markazda {darslar[0].lower()} va {darslar[1].upper()} ni o'rganamiz")

"""Ro'yhat elementlarini o'zgartirish"""
# print(darslar)
# darslar[0] = "Telegram bot"
# print(darslar)

# son = [2,6,-5]
# print(son[0] * son[2])
# x = son[0]+son[1]
# print(x)

""" .append() - ro'yhatga element qo'shadi """
# students = ["Ali","Maruf","Bahrom"]
# print(students)
# students.append("Umarbek")
# students.append("Nodir")
# print(students)

# student = []
""" .insert(3,"name") - ro'yhatga elementni index bo'yicha qo'shadi"""
# students.insert(2,"Jasur")
# print(students)

""" bir ro'yhatni ikkinchisiga qo'shish  extend() """
# fruts = ["apple", "banana", "cherry"]
# tropic_frut = ["mango", "pineapple", "papaya"]
# fruts.extend(tropic_frut)
# print(fruts)

""" del - ro'yhatdan elementni indexi bo'yicha o'chiradi """
""" del -> kalit so'zi  ro'yxatni butunlay o'chirib tashlashi mumkin . """
# del students[1]
# print(students)

""" .remove() - ro'yhatdan elementni qiymati bo'yicha o'chiradi """
# students.remove("Ali")
# print(students)

"""  .pop() - ro'yhatdan elementni sug'urib oluvchi metod"""
""" Agar pop() ga index bermasak u ro'yhat oxiridagi elementni aftomatik oladi """
# print(students)
# new_students = []

# new_students.append(students.pop(2))
# print(students)
# print(new_students)

""" len() - ro'yhatning uzunligini o'lchaydi"""
# family = ["father",'mother','me',]
# print(f"Bizning olilada {len(family)} ta inson yashaydi.")
# print(f"They are {family[0]}, {family[1]}, {family[2]}")

""" list() - ro'yhat shakillantirish uchun funksiya """
# country = list() # ro'yhat yaratish
# davlatlar = [] # bo'sh ro'yhat

""" Ro'yhatni tozalash(elementlardan) clear()"""
# fruts = ["apple", "banana", "cherry"]
# fruts.clear()
# print(fruts)

""" range() - sonli oraliq shakillantirish uchun funksiya """
# sonlar = list(range(-10,11))
# sonlar2 = list(range(2,21,2))
# print(sonlar)
# print(sonlar2)

"""Ro'yhatdan nusxa olish"""
# son = list(range(1,30))
# print(son)

# son2 = son[10:20]
# print(son2)

# family = []
# family.append(input("Otangizni ismini kiriting: "))
# family.append(input("Onangizni ismini kiriting: "))
# print(f"Sizning olilangizda {len(family)} ta inson yashaydi.\
# Ular: {family[0]} va {family[1]}")

"""  .sort() - ro'yhatni alifbo tartibida tartiblaydi """
# name = ["Olim", "Anvar", "Sarvar", "Ali", "Murod"]
# print(name)
# name.sort() # to'g'ri tartiblash
# name.sort(reverse=True) # teskari tartibda tartiblash
# print(name)

""" sorted() - ro'yhatni bir marta alifbo bo'yicha tartiblab beradi """
# print(name)
# print(sorted(name)) # to'g'ri tartibda 
# print(sorted(name, reverse=True)) # teskari tartibda

""" reverse() - ro'yhatni boshi va oxirini aylantirib konsulga chiqaruvchi funksiya"""
# country = ["Uzbekistan", "Afrikaans", "Albanian", "Russian", "Serbian", "Serbian"]
# print(country)
# country.reverse() #ro'yhatni boshi va oxirini aylantirib konsulga chiqaramiz
# print(country)

""" range() """
# number = list(range(1,21))
# print(number)
"""  mix() , min(), sum() funksiyalari """
# print(max(number)) # eng katta soni topib beradi
# print(min(number)) # eng kichik soni topib beradi

# number2  = [55,42,245,-985,0,2,28,93,111,5,3,8439,-34]
# number2.sort()
# print(number2)
# print(f"Bizning ro'yhatdagi eng katta son {max(number2)} va eng kichik {min(number2)}")

# print(sum(number2))# sum() - sonli yig'indini hisoblab beruvchi funksiya
# num3 = max(number2) - min(number2)
# print(num3)



""" Vazifa:
1) ismlar degan ro'yxat yarating va kamida 5 ta yaqin do'stingizning ismini kiriting. 
   Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 


2) sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang(musbat, manfiy, butun, o'nlik). 
    Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
    Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa o'chirib tashlaymiz. 

3) aktyorlar va honandalar degan ro'yhatlaer yarating va ularga o'zingiz eng ko'p kuzatadigan
    aktyorlar va honandalar ni kiriting, ulardan ikkitadan aktyorni o'chirib tashalng, va yangi 3tadan qo'shing.
    song'ra har ikkala ro'yhatdagi elementlarni insonlar degan yangi ro'yhatga jamlang.

4) friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan 
    do'stlaringizni kiriting. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi 
    yordamida o'chrib tashlang. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

5) Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
    metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends 
    ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

6) O'zingizga ma'lum davlatlarning ro'yxatini tuzing(eng kamida 10 ta) va ro'yxatni konsolga chiqaring.
    -ro'yxatning uzunligini konsolga chiqaring;
    -sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring;
    -sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring;
    -asl ro'yxatni qaytadan konsolga chiqaring;
    -reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring;
    -sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring;

7) 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
    -ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring;
    -ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring;
    -ro'yxatdagi elementlar sonini hisoblang;
    -ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring;

8) Taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting.
    -nonushta degan yangi ro'yxatga taomlardan nusxa oling;
    -yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing;
    -ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring;

""" 




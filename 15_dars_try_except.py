"""
Thame: Try - except
"""
# son  = int(input("Son kiriting: "))
# print(f"{son} ning kvadrati {son**2} ga teng")

# try:
#     son  = int(input("Son kiriting: "))
#     print(f"{son} ning kvadrati {son**2} ga teng")
# except:
#     print("Siz son kiritmadingiz")
    
# print("Dasturning davomi")

"""
try - sizga xatolarni tekshirishga imkon beradi
except - sizga xatoni xal qilishga, va uning o'rniga boshqa ma'lumot chiqishiga imkon beradi
else - xato bo'lmaganda kodni bajarishga imkon beradi.
"""
# x = "SAlom"

# print(x)
# print("Hello, world!")

""" try """
# try:
#     print(x)
# except:
#     print("try-except yordamida, xatolik yuzaga kelmaydi va dastur to'xtab qolmaydi.")

# print("Hello, world")

"""
'try' bloki xatoga yo'l qo'yganligi sababli, 'except' bloki bajariladi.
'try' bloki bo'lmasa, dastur ishdan chiqadi va xatoga yo'l qo'yadi av dastur to'xtab qoladi:
"""

""" bir nechta except va xato turlari """
# x = 5
# y = 0
# print(x/y)

# x = 5
# y = 0
# try:
#     z = x/y
# except ZeroDivisionError:
#     print("Sonni nolga bo'lib bo'lmaydi")
# except NameError:
#     print("'x' degan o'zgaruvchi topilmadi")
# except:
#     print("Bu yerda xato matni bo'ladi")

"""
https://www.tutorialsteacher.com/python/error-types-in-python

AssertionError -     Assert bayonoti bajarilmaganda ko'tariladi.
AttributeError -     Atribut tayinlashda ko'tarildi yoki mos yozuvlar bajarilmadi.
EOFError -   Input() funksiyasi faylning oxiri holatiga tushganda ko'tariladi.
FloatingPointError -     Suzuvchi nuqta operatsiyasi bajarilmaganda ko'tariladi.
GeneratorExit -  Jeneratorning close() usuli chaqirilganda ko'tariladi.
Import -     xatosi Import qilingan modul topilmaganda ko'tariladi.
IndexError -     Ketma-ketlik indeksi diapazondan tashqarida bo'lganda ko'tariladi.
KeyError -   Kalit lug'atda topilmasa ko'tariladi.
KeyboardInterrupt -  Foydalanuvchi uzilish tugmachasini bosganda ko'tariladi (Ctrl+c yoki o'chirish).
MemoryError -    Operatsiya xotirasi tugashi bilan ko'tariladi.
NameError -  O'zgaruvchi mahalliy yoki global miqyosda topilmasa ko'tariladi.
NotImplementedError -    Mavhum usullar bilan ko'tarilgan.
OSError -    Tizim ishi tizim bilan bog'liq xatolikka sabab bo'lganda ko'tariladi.
OverflowError -  Arifmetik amal natijasi koʻrsatish uchun juda katta boʻlganda koʻtariladi.
ReferenceError -     Axlat yig'ilgan referentga kirish uchun zaif havola proksi-serverdan foydalanilganda ko'tariladi.
RuntimeError -   Xato boshqa toifaga kirmasa ko'tariladi.
StopIteration -  iterator tomonidan qaytariladigan boshqa element yo'qligini bildirish uchun keyingi() funktsiyasi tomonidan ko'tariladi.
SyntaxError -    Sintaksis xatosiga duch kelganda tahlilchi tomonidan ko'tariladi.
IndentationError -   Noto'g'ri chiziq mavjud bo'lganda ko'tariladi.
TabError -   Qachonki chekinish mos kelmaydigan yorliqlar va bo'shliqlardan iborat bo'lsa ko'tariladi.
Tizim -  xatosi Tarjimon ichki xatoni aniqlaganida ko'tariladi.
SystemExit -     sys.exit() funksiyasi tomonidan ko'tarilgan.
TypeError -  Funktsiya yoki operatsiya noto'g'ri turdagi ob'ektga qo'llanilganda ko'tariladi.
UnboundLocalError -  Funksiya yoki usulda mahalliy o‘zgaruvchiga havola qilinganda ko‘tariladi, lekin bu o‘zgaruvchiga hech qanday qiymat bog‘lanmagan.
UnicodeError -   Unicode bilan bog'liq kodlash yoki dekodlash xatosi yuzaga kelganda ko'tariladi.
UnicodeEncodeError -     Kodlash paytida Unicode bilan bog'liq xatolik yuzaga kelganda ko'tariladi.
UnicodeDecodeError -     Unicode bilan bog'liq xato dekodlash vaqtida yuzaga kelganda ko'tariladi.
UnicodeTranslateError -  Unicode bilan bog'liq xato tarjima paytida yuzaga kelganda ko'tariladi.
ValueError -     Funktsiya to'g'ri turdagi, lekin noto'g'ri qiymatdagi argumentni olganida ko'tariladi.
ZeroDivisionError -  Bo'linish yoki modul operatsiyasining ikkinchi operandi nolga teng bo'lganda ko'tariladi.

""" 


""" else """
""" 
else - xech qanday xatolik yuzaga kelmagan xollarda ishlatiladi
"""
# a = 5
# try:
#     print(a**2)
# except:
#     print("Bu yerda xato matni bo'ladi")
# else:
#     print("Xech qanday xatolik yuzaga kelmadi") # va hech qanday xatolik bo'lmasa 'else' ham ishlaydi


""" finally """
"""
'try' - blokida xatolik bo'ladimi yoki yo'qmi, qat'iy nazar 'finally' bajariladi.
"""

# a = 4
# b = 10
# try:
#     print(a+b)
# except:
#     print("Error Error Error")
# finally:
#     print("'finally' doim ishlaydi")

""" raise """
""" 'raise' xato matnini dasturchiga o'zimiz hohlagan ko'rinishda ko'rsatishga imkon beradi
"""

# a = 4
# b = 10
# try:
#     print(a+b)
# except NameError:
#     print("Name Error")
# raise NameError("Name Error - berilgan nomdagi o'zgaruvchi topilmaganda yuzaga keladi") 

""" 
try:
    Xatolik yuzaga kelishi mumkin bo'lgan blok 
except:
    Xatolikni oldini aniqlab kodning to'xtab qolishini oldini oladi
else:
    Agar xatolik bo'lmasa shu blokdagi kod ishlaydi
finally:
    Xatolik bo'lsa ham bo'lmasa ham, bu blokda gi kod ishlaydi
"""

""" Masalalar """
""" 1 """
# def bigger():
#     try:
#         a = float(input("1-sonni kirirting:"))
#         b = float(input("2-sonni kirirting:"))
#     except ValueError:
#         print("Siz son kiritmadingiz")
#     except:
#         print("Error Error Error ")
#     else:
#         if a>b: 
#             print(f"{a}>{b}")
#         elif a<b:
#             print(f"{a}<{b}")
#         else :
#             print(f"{a}={b}")
# bigger()

""" 2 """
# def bithday():
#     try:
#         yil = int(input("Tug'ilgan yilingizni kiriting: "))
#     except ValueError:
#         print("Siz butun son kiritmadingiz !!!")
#     except:
#         print("Ma'lumot kiritishda xatolik yuzaga keldi.")
#     else:
#         if 2023 > yil > 0:
#             print(f"Siz {2023-yil} yoshda ekansiz")
#         elif -2023 < yil < 0:
#             print(f"Siz {2023-(-yil)} yoshda ekansiz")
#         else:
#             print("Siz hali mavjud bo'lmagan yil kiritdingiz")

# bithday()

"""  
Vazifa:

1) Sonlar deb nomlangan ro'yhat tuzing ro'yhatda bir nechta sonlar va 0 ham bo'lsin.
    Keyin foydalanuvchidan biror son kiritishini so'rab, qabul qilingan sonni sonlar ro'yhatidagi 
    sonlarga bo'ling va natijani konsulga chiqaring.
    Dastur tuzishda 'try-except' dan foydalaning va yuzaga kelishi mumkin bo'lgan barcha xatoliklarni oldini oling !
    
2) Foydalanuvchidan uning yoshini qabul qilib olib uni 0 dan 1,000 gacha bo'lgan sonlardan qaysilariga 
    qoldiqsiz bo'linnishini aniqlab, qoldiqsiz bo'linadigan sonlarni ro'yhatga saqlab konsulga chiqaring.
    Va bu dasturni funksiyaga joylang. Hamda uni yozishda 'try-except' dan foydalaning va yuzaga kelishi
    mumiin bo'lgan xatoliklarni oldini oling
    
3) To'g'ri burchakli uchburchakning gipotenuzasini hisoblash. Ushbu kodda yuzaga kelishi mumkin bo'lgan hatoliklarni
    'try-except' yordamida oldini oling
    
a = int(input("Birinchi katetni kiriting: "))
b = int(input("Ikkinchi katetni kiriting: "))
# c**2=a**2+b**2

import math
c = round(math.sqrt(a**2+b**2),2)
print(f"Katetlari {a} va {b} ga teng bo'lgan uchburchakning giputenuzasi {c} ga teng")

4) mevalar deb nomlangan ro'yhat(list ) yarating. Avval uni o'zgarmas ro'yhat turiga , keyin esa set turiga o'zgartiring va konsulga ularning 
turini chiqaring.
	-remove() yordamida 3 ta discard() yordamida 3 ta elementni o'chirib tashlang va ro'yhatni konsulga chiqaring.
	-va yangi 5 ta element qo'shing va ro'yhatni konsulga chiqaring;
	-so'ngra ro'yhatni tozalang va uni konsulga chiqaring;
	-keyin esa ro'yhatni o'chirib tashlang;
 
    Ushbu kodda yuzaga kelishi mumkin bo'lgan hatoliklarni 'try-except' yordamida oldini oling

"""




"""
Thame: Kirish, print() funksiyasi, o'zgaruvchilar(veribles), o'zgaruvchilar turlari
"""

""" 
print() funksiyasi 
print() - python da o'zgaruvchi(matn, son, ro'yhat, lug'at...)larni
konsulga chiqarib beruvchi funksiya hisoblanadi
"""

""" Birinchi dastur """
print("Hello world!")
print("Olim Hasanov")

""" Kommnet turlari """
print("Bu bir qator kommnetga olingan matn") # birinchi comment
print("Kommentlar asosan izoh qoldirish uchun oshlatiladi") # bu mening birinchi izohim

"""
Ushbu turdagi kommnetlar asosan 
ko'p qatorli so'zlar ishlatilganda
foydalaniladi.
Uning afzaligi istalgancha 
yangi qatordan kod yoza olasiz
"""

""" O'zgaruvchilar """
"""
O'zgaruvchi —kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan joy. 
Soddaroq qilib tushuntirsak, o'zgaruvchini quti, quti ichidagi narsani esa qiymat deb tasavvur qilish mumkin. 
Pythonda qiymatlar son, matn, ro'yxat va hokazo ko'rinishida bo'lishi mumkin.


O'zgaruvchi (variable) bunday deyilishiga sabab, uning qiymati istalgan vaqt o'zgartirilishi mumkin

O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:
O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
O'zgaruvchi nomida faqatgina lotin alifbosi harflari (a-z), raqamlar (0-9) va pastki chiziq (_) qatnashishi mumkin
O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)
Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va maxsus kalit so'zlarning (keywords) nomini bermang.
False, True, and, if, while, in, on, break, await, continue, not, try, from, def, pass ...
"""

matn = "Bu matn ko'rinishidagi o'zgaruvchi"
print(matn)

son = 5
print(son)

matn1 = "Bu"
matn2 = "matn"
matn3 = matn1 + matn2
print(matn3)

""" bir vaqtni o'zida ko'p o'zgaruvchi yaratish """
x, y, z = "Olma", "Banan", "Olcha"
print(x)
print(y)
print(z)

""" Birxil qiymatli o'zgaruvchilar """
x = y = z = "Olma"
print(x)
print(y)
print(z)

""" Bir nechta o'zgaruvchilarni  konsulga chiqarish """
x = "Python"
y = "is"
z = "best programming language"
print(x, y, z)

a = "Python"
b = "is"
c = "best programming language"
print(a + ' ' + b + " "+ c)

x = 5
y = 10
print(x + y)

x = 5
y = 10
print(x , y)


""" Malumot turlari  """
son =  5 # butun son - number
son2 = 12.8 # o'nlik son - float
matn = "Bu matn" # matn - string
ismlar = ["Ali", "Olim", "Vali", "Hasan"] # ro'yhat  - list
sonlar = (2, 5, -7, 5.7, 12.5, 33) # o'zgarmas ro'yhat - tuple
oila = { # lug'at - dictionary
    "ota":"Olim",
    "ona":"Nigora",
    "ogil":"Anvar",
}
ali = True # mantiqiy qiymat - Boolean
set1 = {'Ali', 2, 3,'Python'}  # to'plam - set

""" type() funksiyasi """
print(matn)
print(type(matn))

print(son)
print(type(son))

print(ismlar)
print(type(ismlar))




"""
Vazifa:
    5 ta turli matnlarni print() da chiqarish.
    oila azolarimizning har birini ismlarni alohida print() da konsulga chiqaramiz.
    3 ta sonni print() da chiqaramiz.
    5 ta o'zgaruvchi yaratamiz va ularni har birini print() da o'zini va ularning turini konsulga chiqaramiz.
    ism, familya, yosh, kasb va manzil degan o'zgaruvchilar yaratamiz va ularni bitta print() da chiqaramiz.
    Yuqoridagilarning har biriga komment yozib chiqaramiz
"""



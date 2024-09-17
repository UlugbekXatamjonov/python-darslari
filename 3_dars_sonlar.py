"""
Thame:Sonlar(Lists) bilan ishalsh
"""

""" Sonlarning turlari """
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

""" Butun son turlari """
a = 15
b = -8
c = 0
print(a)
print(type(a))

""" O'nlik son turlari """
x = 35e3 # 35000.0
y = 12E4 # 120000.0
z = 14.76
print(x)
print(type(x))

"""Arifmetik amallar"""
a = 5
b = 7
print(a+b) # qo'shish
print(a-b) # ayrish
print(a/b) # bo'lish
print(a*b) # ko'paytirish

c = a+(b-a)*b
print(c)

"""Sonni kvadradga ko'tarish"""
f = 3**4 #  ** kvadrat belgisi
print(f)

"""" Sonni ildizdan chiqarish  """
d = 16
import math
print(math.sqrt(d))

""" Sonni yaxlidlash """
x = 4.3
print(x,2)
print(round(x))

""" random moduli - tasodifiy son """
import random
print(random.randrange(1, 10))

 
""" int()/ str()/ float() """
a = 5           # butun son  --> int
b = 12.3        # o'nlik son --> float
c = "Salom"     # matn       --> str

print(type(a))  # a ni turini tekshiramiz
print(a)        # a ni konsulga chiqaramiz
a1 = float(a)   # a ni turini o'nlik son(float) ga "a1" o'zgartiramiz
print(type(a1)) # a1 ni turini tekshiramiz
print(a1)       # a1 ni konsulga chiqaramiz

"""Bir vaqting o'zida bir nechta o'zgaruvchi yaratish"""
x,y,z  = 4,9,-7
print(x,y,z)

""" Ko'p honali sonlar """
uzb = 36_032_123
yer = 800_321_215_245
print(uzb)
print(yer)

"""Yoshni topuvchi dastur"""
year = int(input("Qaysi yilda tug'ilgansiz: "))
age = 2022-year
print(f"Siz {year} yili tug'ilgansiz va yoshingiz {age} yoshda")

""" Sonni kvga va kubga ko'tarish """
number = int(input("Biror son kiriting: "))
kv = number**2
kub = number**3
print(f"Siz kiritgan {number} sonining kvadrati {kv} ga kubi esa {kub} ga teng")

""" Kvadratning perimetri va yuzi  """
kvadrat = int(input("Kvadratning tomonini kiriting: "))
yuza = kvadrat**2
per = kvadrat*4
print(f"Tomoni {kvadrat} ga teng bo'lgan kvadratning yuzi {yuza} ga,\
perimetri esa {per} ga teng bo'ladi. ")

""" To'g'ri burchakli uchburchakning gipotenuzasini hisoblash """
a = int(input("Birinchi katetni kiriting: "))
b = int(input("Ikkinchi katetni kiriting: "))
c**2=a**2+b**2

import math
c = round(math.sqrt(a**2+b**2),2)
print(f"Katetlari {a} va {b} ga teng bo'lgan uchburchakning giputenuzasi {c} ga teng")


"""
Vazifa:
1) Alanani uzunligini topuvchi dastur tuzing. Aylananing radiusini foydalanuvchidan so'rang.  
   Formulasi: S=2*pi*r  / pi=3.14 / r= radius
2) Doirani yuzini topuvchi dastur. Aylananing radiusini foydalanuvchidan so'rang.
   Formulasi: S=pi*r**2 / pi=3.14 / r = radius
3) Tog'ri burchakli uchburchakni katetlari ni foydalanuvchidan so'rab, shu uchburchakning 
   gipotenuzasini hisoblaydigan dastur tuzing. 
   Formulasi: c**2 = a**2 + b**2   / a va b - katetlar, c - gipotenuza
4) Foydalanuvchidan ikkita son kiritishini so'rab shu kiritilgan sonlarning o'rta 
   arifmetigini hisoblang.
   Formulasi: (a+b)/2
5) Foydalanuvchidan ikkita son kiritishini so'rab shu kiritilgan sonlarning yig'indisi, 
   ayirmasi, ko'paytmasi
   bo'linmasi, o'rta arifmetigi va har ikkala sonning kvadrati va kuni aniqlang.
   Formulasi: a+b, a-b, a*b, a/b, (a+b)/2, a**2, a**3, b**2, b**3
6) Foydalanuvchidan ikkita A va B sonlarini kiritishini so'rang va sonlar qiymatini 
   almashtirib konsulga chiqaring.
7) Foydalanuvchidan ikkita A, B va C sonlarini kiritishini so'rang va A ni qiymatini 
   B ga , Bni qiymatinni C ga
   C ni qiymatini A ga almashtirib konsulga chiqaring
8) Foydalanuvchidan 'x' ni kiritishini so'rab quidagi 'y' ning qiymatini toping.
   y = 4*(x-3)**5-7*(x-3)**3+2
9) Quidagi ammalarning natijasini yaxlidlang:
   231/4.7    24/1.4   541/7.6
10) math va random modullaring har biridan 5 tadan funksiyani o'rganib, undan 
   foydalanish(misol yozib kelish).
    Darsda ko'rganlarimizdan tashqari ! 

"""



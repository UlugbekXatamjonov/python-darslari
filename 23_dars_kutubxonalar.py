"""
Thame: Pythonda Kutubxonalar, dates, math, RegEx...
"""

""" Datetime - Vaqt moduli """
import datetime

# hozir = datetime.datetime.now()
# print(hozir)

# print(hozir.date()) # sanani ajratib olish
# print(hozir.time()) # vaqtni ajratib olish
# print(hozir.hour) # soatni ajratib olish
# print(hozir.minute) # minutni ajratib olish
# print(hozir.second) # sekundni ajratib olish

# print(hozir.date()) # sana 
# print(hozir.strftime("%A")) # hafta kuni
# print(hozir.strftime("%B")) # oy

"""
link -> https://docs.python.org/3/library/datetime.html
link -> https://www.w3schools.com/python/python_datetime.asp

%a	Weekday, short version	                    Wed	
%A	Weekday, full version	                    Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	    3	
%d	Day of month                                01-31	31	
%b	Month name, short version	                Dec	
%B	Month name, full version	                December	
%m	Month as a number                           01-12	12	
%y	Year, short version, without century	    18	
%Y	Year, full version	                        2018	
%H	Hour                                        00-23	17	
%I	Hour                                        00-12	05	
%p	AM/PM	                                    PM	
%M	Minute                                      00-59	41	
%S	Second                                      00-59	08	
%f	Microsecond 000000-999999	                548513	
%z	UTC offset	                                +0100	
%Z	Timezone	                                CST	
%j	Day number of year 001-366          	    365	
%U	Week number of year, 
    Sunday as the first day of week, 00-53	    52	
%W	Week number of year, 
    Monday as the first day of week, 00-53	    52	
%c	Local version of date and time	            Mon Dec 31 17:41:00 2018	
%C	Century	                                    20	
%x	Local version of date	                    12/31/18	
%X	Local version of time	                    17:41:00	
%%	A % character	                            %	
%G	ISO 8601 year	                            2018	
%u	ISO 8601 weekday (1-7)	                    1	
%V	ISO 8601 weeknumber (01-53)	                01
"""

# bugun = datetime.date.today()
# print(f"Bugungi sana: {bugun}")

# hozir = datetime.datetime.now().time()
# print(f"Hozir soat: {hozir}")

""" Ramazongacha bo'lgan vaqt """
# bugun = datetime.date.today()
# ramazon = datetime.date(2023, 3, 23)
# farq = ramazon-bugun
# print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")


""" math - Matematik moduli """
import math

# PI = math.pi
# print(f"PI ning qiymati: {PI}")

# x = abs(-7.25) # elgilangan raqamning mutlaq (musbat) qiymatini qaytaradi
# print(x)

# x = pow(4, 3) # 'x' ni 'y' darajaga ko'taradi
# print(x)

# x = math.ceil(1.4) # raqamni yuqoriga qarab eng yaqin butun songa yaxlitlayd
# y = math.floor(1.4) # raqamni pastga qarab eng yaqin butun songa yaxlitlaydi

# print(x) # javobi - 2
# print(y) # javobi - 1

"""
link -> https://www.w3schools.com/python/module_math.asp
link -> https://docs.python.org/3/library/math.html

math.acos()              Raqamning yoy kosinusini qaytaradi
math.acosh()             Sonning teskari giperbolik kosinusini qaytaradi
math.asin()              Sonning yoy sinusini qaytaradi
math.asinh()             Sonning teskari giperbolik sinusini qaytaradi
math.atan()              Radyandagi sonning yoy tangensini qaytaradi
math.atan2()             y/x ning yoy tangensini radianlarda qaytaradi
math.atanh()             Sonning teskari giperbolik tangensini qaytaradi
math.ceil()              Raqamni eng yaqin butun songacha yaxlitlaydi
math.comb()              n ta elementdan takror va tartibsiz tanlash usullari sonini qaytaradi
math.copysign()          Birinchi parametrning qiymati va ikkinchi parametrning belgisidan iborat floatni qaytaradi
math.cos()               Raqamning kosinusini qaytaradi
math.cosh()              Sonning giperbolik kosinusini qaytaradi
math.degrees()           Burchakni radiandan gradusga aylantiradi
math.dist()              Ikki nuqta (p va q) orasidagi Evklid masofasini qaytaradi, bu erda p va q bu nuqtaning koordinatalaridir.
math.erf()               Raqamning xato funksiyasini qaytaradi
math.erfc()              Raqamning to'ldiruvchi xato funksiyasini qaytaradi
math.exp()               X darajasiga ko'tarilgan E ni qaytaradi
math.expm1()             Ex - 1ni qaytaradi
math.fabs()              Raqamning mutlaq qiymatini qaytaradi
math.factorial()         Raqamning faktorialini qaytaradi
math.floor()             Raqamni eng yaqin butun songacha yaxlitlaydi
math.fmod()              x/y ning qolgan qismini qaytaradi
math.frexp()             Belgilangan sonning mantis va ko'rsatkichini qaytaradi
math.fsum()              Har qanday takrorlanadigan barcha elementlarning yig'indisini qaytaradi (kordellar, massivlar, ro'yxatlar va boshqalar).
math.gamma()             X da gamma funksiyasini qaytaradi
math.gcd()               Ikki butun sonning eng katta umumiy boʻluvchisini qaytaradi
math.hypot()             Evklid normasini qaytaradi
math.isclose()           Ikki qiymat bir-biriga yaqin yoki yo'qligini tekshiradi
math.isfinite()          Raqamning chekli yoki chekli emasligini tekshiradi
math.isinf()             Raqam cheksiz yoki cheksiz ekanligini tekshiradi
math.isnan()             Qiymat NaN (raqam emas) yoki yo'qligini tekshiradi
math.isqrt()             Kvadrat ildiz sonini pastga qarab eng yaqin butun songa yaxlitlaydi
math.ldexp()             math.frexp() ning teskarisini qaytaradi, bu berilgan x va i raqamlarining x * (2**i) ga teng
math.lgamma()            X ning log gamma qiymatini qaytaradi
math.log()               Sonning natural logarifmini yoki sonning logarifmini asosga qaytaradi
math.log10()             x ning 10 ta asosiy logarifmini qaytaradi
math.log1p()             1+x ning natural logarifmini qaytaradi
math.log2()              x ning 2 ta asosiy logarifmini qaytaradi
math.perm()              n ta elementdan tartibli va takrorlanmasdan k ta elementni tanlash usullari sonini qaytaradi
math.pow()               x qiymatini y darajasiga qaytaradi
math.prod()              Takrorlanadigan barcha elementlarning mahsulotini qaytaradi
math.radians()           Daraja qiymatini radianga aylantiradi
math.remainder()         Numeratorni maxrajga toʻliq boʻlinishi mumkin boʻlgan eng yaqin qiymatni qaytaradi
math.sin()               Sonning sinusini qaytaradi
math.sinh()              Sonning giperbolik sinusini qaytaradi
math.sqrt()              Raqamning kvadrat ildizini qaytaradi
math.tan()               Raqamning tangensini qaytaradi
math.tanh()              Sonning giperbolik tangensini qaytaradi
math.trunc()             Raqamning kesilgan butun son qismlarini qaytaradi
"""


""" 
RegEx

RegEx yoki Regular Expression - qidiruv sxemasini tashkil etuvchi belgilar ketma-ketligi.
Bu modul yordamida biror matn berilgan andozaga tushish, tushmalsigini tekshrib ko'rishimiz mumkin. 
Yoki berilgan andoza asosida matnlar orasidan kerakli matnlarni ajratib olish mumkin.
"""
import re

"""
So'zlarni andozaga solishtirish uchun re.match() funksiyasidan foydalanamiz. 
    Agar tekshirgan so'zimiz andozaga mosh tushsa, re.match() metodi so'zni o'zini qaytaradi, 
    aks holda None qiymatini qaytaradi.
"""
# word1 = "python"
# word2 = "Hello"
# word3 = "noutbook"

# print(re.match("^p....n", word1))
# print(re.match("^H...o", word2))
# print(re.match("^n...k", word3))


"""
Tayyor andozalarni yaratish va ularninsinash --> https://ihateregex.io/
"""

matn = """
    Assalomu aleykum
    Vaaleykum assalom
    Menga telefon raqamingizni bera olasizmi ?
    Albatta. +998991234567. Email manzilim esa testemail@gamil.com
"""

matn2 = """
    -Assalomu aleykum
    -Vaaleykum assalom
    -Menga telefon raqamingizni bera olasizmi ?
    -Albatta. +998991234567 . 01/01/2000  Email manzilim esa testemail@gamil.com
"""
# email_andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(email_andoza,matn2)
# print(email)


# text = "Python the best programming language in the world"
# x = re.split("a", text)
# print(x)

# text = "Python the best programming language in the world"
# x = re.split("a", text, 2) # bo'linishlar soni belgilash mumkin
# print(x)

# text = "Python the best programming language in the world"
# x = re.sub("a", 'o', text ) # belgilangan belgini boshqasi bn almashtiradi
# print(x)

# text = "Python the best programming language in the world"
# x = re.sub("a", 'O', text, 3 ) # birinchi 3 tasini  
# print(x)

"""
link -> https://docs.python.org/3/howto/regex.html
link -> https://docs.python.org/3/library/re.html
link -> https://www.w3schools.com/python/python_regex.asp

RegEx funksiyalari
findall()   -   Barcha mosliklarni o'z ichiga olgan ro'yxatni qaytaradi
search()    -   Agar satrning istalgan joyida moslik mavjud bo'lsa, Match ob'ektini qaytaradi
split()     -   Har bir o'yinda satr bo'lingan ro'yxatni qaytaradi
sub()       -   Bir yoki bir nechta moslikni satr bilan almashtiradi

"""


""" 
Vazifa 

1) Foydalanuvchidan tug'ilgan kuni, sanasini so'rab, unga tug'ilgan vaqtidan ayni vaqtgacha o'tgan,
    vaqtni soat va minutigacha aniqlikda hisob qaytaring.
2) Insonlarning yoshi uchun regex yarating.
3) Aynan O'zbekiston aloqa operatorlari raqamlariga mos regex yarating.
"""



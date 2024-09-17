"""
Thame: Funkcions(Funksiyalar)
"""

""" Funksiyaga ro'yhat uzatish """
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)

# print(baholar)


""" Moslashuvchan funksiya """
"""
Agar funksiyangiz bir nechta argument qabul qilishi kerak bo'lsa-yu, lekin siz argumentlar 
sonini aniq bilmasangiz, Pythonda istalgancha qiymat qabul qiluvchi funksiya yaratish 
imkoniyati bor. 
"""

""" *args usuli """ #   *args ---> arguments
# def summa(son1, son2, *sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = son1 + son2
#     for son in sonlar:
#         yigindi += son
        
#     return yigindi

# print(summa(1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 16, 17))
# print(summa(-7,0,8))
# print(summa(23,4))

"""
*args usulida, bacha uzatilgan parametrlar (bir dona bo'lsa ham) funksiya ichida.
o'zgarmas ro'yxatga (tuple) joylanadi.

Agar funksiya bir nechta argument qabul qilsa, *args argument doim oxirida yoziladi.
"""

# def summa(x,y,*sonlar): # funksiyamiz kamida 2 ta parametr qabul qiladi(x va y)
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     a = x+y+sum(sonlar)
#     return a

# print(summa(4, 5, 7, 9))


""" **kwargs usuli """ #  **kwargs ---> keyword arguments(kalit so'zli argumentlar)
"""
Agar funksiyaga kalit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa,
va bunday parametrlar soni noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).
"""
# def info(ism, familya, **malumotlar):
#     """ Inson haqidagi malumotlarni lug'at ko'rinishida qaytaradigan funksiya """
#     malumotlar['ism'] = ism
#     malumotlar['familya'] = familya
#     return malumotlar

# inson1 = info("Abubakir", "Olimov")
# inson2 = info("Hasan", "Abdullayev", yosh=34, kasb="haydovchi", tel=998997897878, email="qwerty@gmail.com")
# print(inson1)
# print(inson2)


""" Modullar """
"""
Funksiyaning qulayliklaridan biri, ko'p takrorlanadigan kodlarni funksiya ichida yashirishimiz va 
kerak bo'lgan murojat qilishimiz mumkinligida. Maqsadimiz dasturimizni ixcham va tushunarli qilib, 
kelajakda o'zimiz yoki boshqalar uchun ham "toza" kod qoldrisih. Bu yo'nalishda yana bir qadam qo'yib, 
dasturimizni modullarga ajratimshimiz mumkin. 

Modul bu loyihamiz ichidagi alohida fayl bo'lib, dasturimiz davomida ishlatiladigan funskyalarni 
(va o'zgaruvchilarni) mana shu faylga joylab, ko'zdan yashirib qo'yishimiz mumkin. Bu bizga asosiy 
dasturimizdan chalg'imasdan kod yozish imkoniyatini beradi. 

Modul va uning ichidagi funksiyalarni istalgan payt asosiy dasturimizga yuklab olishimiz, modullarni 
boshqa dasturchilar bilan ulashishimiz yoki kelajakda o'zimizning boshqa loyihalarimizda foydalanishimiz mumkin.
Umuman olganda katta dasturlar bir nech o'nlab modullardan iborat bo'lishi tabiiy hol.

Modul yaratish uchun asosiy dasturimizdagi funksiyalarni yangi faylga ko'chiramiz xolos. 
Modulga oson murojat qilishimiz uchun, bugungi darsimiz uchun bitta "papka"(modullar_darsi) yaratib olamiz va
uning ichida main.py va funksiyalar.py deb nomlangan 2ta fayl hosil qilamiz.

"""

""" funksiyalar faylidan kerakli funksiyalarni chaqirib(yuklab) olamiz"""
# from funksiyalar import bahola
# import funksiyalar
# from yordamchi_funksiyalar.y_funksiyalar import summa
# from yordamchi_funksiyalar.y_funksiyalar import summa as yig

""" bahola() """
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)


""" summa() """
# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(-7,0,8))
# print(summa(23))


""" as - modul nomini o'zgartirish """
# print(yig(1,2,3,4,5,6,7,8,9))
# print(yig(-7,0,8))
# print(yig(23))



""" Lambda funksiyasi """

"""
Pythonda nomsiz vaqtinchalik funksiyalar yaratish imkoniyati mavjud. Bunday funksiyalarni yaratishda 
    def operatori o'rniga 'lambda' operatori ishlatilgani uchun ham lambda funskiyalar deb ataladi. 

Lambda funksiyalari istalgan miqdordagi argumentlarga ega bo'lishi mumkin, ammo funksiya badanida faqat 
    bitta ifoda mavjud bo'ladi. Ifoda bajariladi va qaytariladi (return operatori shart emas). 
"""

# from math import pi

# uzunlik = lambda pi, r : 2*pi*r
# #             Argument : Ifoda """
# print(uzunlik(pi,10))


""" 2       Istalgan songa 10 ni qo'shuvchi funksiya """ 
# x = lambda a : a + 10
# print(x(3))

""" 3       a va b ni ko'paytmasini qaytaradigan funksiya """
# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b * c
# print(x(5, 6, 2))

""" 4  Sonni istalgan songa ko'paytuvchi funksiya """
# def myfunc(n):
#     return lambda a : a * n

# ikkiga = myfunc(2) # n
# uchga = myfunc(3)
# beshga = myfunc(5)

# print(ikkiga(10)) # a
# print(uchga(15))
# print(beshga(4))

""" Qisqa vaqt ichida anonim funksiya talab qilinganda lambda funksiyalaridan foydalaning """


"""
Vazifa:

1) Avvalgi darslarimizda bajargan parol tizimi haqidagi dasturimizni 'password.py' fayliga qayta yozing.
    Va uni yangi 'main.py' fayliga chaqirib olib ishlating.

2) Inson haqidagi malumotlarni qabul qilib olib, ularni lug'at ko'rinishida qaytaradigan funksiyani 
    'person.py' fayliga yozing. va uni ham 'main.py' fayliga chaqirib olib ishlating.
    Funksiya yozishda *args va **kvargs usullaridan foydalaning.

"""





"""
Thame: Funkcions(Funksiyalar)
"""
"""
Funksiya - Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.
Biz shu vaqtgacha ko'rib o'tgan funksiyalar: print(), len(), sum(), max(), min()...
"""
""" Funksiya yaratish """
# def salom():
#     """ Ushbu funksiyaning vazifasi Salomlashish """
#     print("Assalom aleykum")
    
# salom()

""" DOCSTRING """
""" 
    DOCSTRING ---> Defenition
    Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin: 
"""
# print(len.__doc__)

# def salom_ber(ism):
#     """ Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya. ism -> Matn kiritish kerak """
#     print(f"Assalomu alaykum, hurmatli {ism}!")
    
# salom_ber("Ali")
# salom_ber("Vali")
# salom_ber('Umar')

"""
    Funksiyaga nom berishda fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning. 
    Bu bilan siz o'zgaruvchi va funksiya o'rtasini farqlashingiz oson bo'ladi. 
    Misol uchun, yuqorida biz funksiyamizni salom emas salom_ber deb nomladik.
"""

""" Funksiyaga qiymat uzatish """
# def hisobla(tyil, yil):
#     """
#     Foydalanuvchi yoshini hisoblovchi funksiya. 
#     tyil - Tug'ilgan yilingizni kiriting
#     yil- hozirgi yil
#     """
#     yosh = yil - tyil
#     print(f"Siz {yosh} da ekansiz")
    
# hisobla(2023, 2000)
# hisobla(2001, 2023)


""" Argumentni kalit so'z bilan uzatish """
# def plus(son1, son2):
#     """ Foydalanuvchi kiritgan sonlarni bir biriga qo'shib beradi. """
#     son3 = son1 + son2
#     print(f"Siz kiritgan {son1} va {son2} larning yig'indisi {son3} ga teng.")
# plus(son2=5, son1=5)


# def full_name(name, surname, father):
#     """
#     full_name - To'liq ism sharifni qaytarish uchun funksiya
    
#     Arguments:
#         name - str
#         suename - str
#         father - str 
#     """
#     print(f"{surname} {name} {father}")

# full_name(name="Olimjon", surname="Aliyev", father="Baxodirovich")



""" Standar qiymat uzatish """
"""
    Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi kerak. 
    Aks holda xatolik yuzaga keladi.
"""     
# def full_name(familya, ism="Ali"):
#     print(ism, familya)
    
# full_name(familya = "Olimmov")
# full_name("Asadbek","Mirzanvarov")


# def kv(son=5):
#     """ Kiritilgan sonning kvadratini hisoblovchi funksiya, son - int"""
#     son_kv = son**2
#     print(f"Siz kiritgan {son} ning kvadrati {son_kv} ga teng")
# kv(4)
# kv(5)


"""
Vazifa:

1) Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
2) Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
3) Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
4) Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
    Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
5) Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini 
    tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
6) Foydalanuvchidan uning oila azolari haqidagi malumotlarmni olibn ularni konsulga chiqaruvchi funksiya 
    yozing. M: ismi, yoshi, kasbi...
7) Tog'ri to'rtburchakli uchburchakning katetlarini qabul qilib olib uning gipotenuzsini hisoblovchi funksiya 
    yozing, 2- katetni o'zgarmas parameter sifatida bering.
    f: c**2 = a**2 + b**2 / c ni topish kk / b - o'zgarmas qiymat

Yuqoridagi har bir funksiyaga to'liq tarif(defenition yozing)

"""


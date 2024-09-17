"""
Thame: Pythonda OOP va Class lar bilan tanishuv
"""

"""
Python - bu ob'ektga yo'naltirilgan dasturlash tili.
OPP - Object Oriented Programming ya'ni obyektga yo'naltiriglan dasturlash.
OOP haqida ---> https://python.sariq.dev/oop/kirish
Klass-  bu obyekt yaratish uchun shablon yoki qolipdir. 
Bitta klassdan biz istalgancha nusxa olishimiz va yangi obyektlar yaratishimiz mumkin.
"""

# x = 17
# print(type(x))

# matn = "python"
# print(type(matn))

# def func():
#     print("Hello world!")
# print(type(func))

"""
METODLAR
Har bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. 
Bu funksiyalar obyekt ichida yashirin bo'ladi, va biz ularga nuqta va funksiya nomi 
orqali murojat qilishimiz mumkin. Bunday funksiyalar shu klass (yoki obyektga) tegishli metodlar deyiladi.
Bir klassga tegishli metodlar, boshqa klassdagi obyketlar uchun mavjud bo'lmasligi tabiiy. 
Misol uchun matnlar uchun mavjud metodlarni, butun yoki o'nli sonlarga qo'llab bo'lmaydi.
"""
# matn = "python"
# print(matn.title())

# son = 20
# print(son.title()) # error message


""" Class yaratish """
"""
Yangi klass yaratish uchun class operatoridan foydalanamiz.
klass bu hali obyekt emas, bu obyekt uchun shablon. Shuning uchun klass yaratishda 
shu klassdagi obyektlar uchun umumiy bo'lgan xususiyatlar va funksiyalarni o'ylashimiz kerak.
"""

# class Car:
#     """ Mashina klassi """
#     def __init__(self, brend, model, year, prise): # klasni hususiyatlarini o'zida saqlovchi funksiya
#         """ Mashinaning xusiyatlari 
#         self.xususiyat = argument
#         """
#         self.brend = brend
#         self.model = model
#         self.year = year
#         self.prise = prise
        
#     def get_info(self):
#         return f"{self.brend} kompaniyasining  {self.model} rusumli aftomobili {self.year}-yilda ishlab chiqarilgan. Narxi: {self.prise} $"


#     def full_info(self):
#         """ Mashina haqida ma'lumot beruvchi funksiya  """
#         print(f"{self.brend} brendining {self.model} modeli. \nIshla chiqarilgan yili {self.year}. \nNarxi: {self.prise}")

#     def get_year(self):
#             """ Mashinaning ishlab chiqarilgan yilini aniqlovchi metod(funksiya)"""
#             info = f"Ushbu mashina {self.year} da ishlab chiqarilgan"
#             return info
            
#     def get_prise(self):
#             """ Mashinaning narxini aniqlovchi metod(funksiya)"""
#             return f"Ushbu mashina {self.prise} $ turadi"
        
#     def get_date(self, now=2023):
#         """ Mashina ishlab chiqarilgan vaqtgacha bo'lgan yil """
#         info = ''
#         year = now - self.year
#         if year:
#             info = f"Mashina ishlab chiqarilganiga {year} yil bo'lgan"
#         else:
#             info = "Mashina shu yili ishlab chiqarilgan" 
        
#         return info
"""
class Car — Car nomli klass yaratdik. Klasslarga nom berishda uning birinchi harfini katta harfdan 
    boshlash tavsiya qilinadi. Agar klass nomi 2 va undan ko'p so'zdan iborat bo'lsa har bir so'zni 
    katta harf bilan boshlang.
def __init__(self) — kaslsga tegishli xususiyatlarni saqlovchi maxsus metod (funksiya). 
    'self' kalit so'zi ingliz tilidan "o'zi" deb tarjima qilinadi, va bu klassdan yaratilgan obyektning 
    o'ziga ishora qiladi. Ya'ni keyinchalik biz obyekt ichidagi metodga murojat qilganimizda 
    shu obyektning o'zi birinchi bo'lib funksiyaga argument sifatida uzatiladi, obyket ustida 
    turli amallar bajarish imkonin beradi. Har bir classda albatta bir marta yozilishi shart
def __init__(self, brend, model, name, year, prise) — yaratayotgan klassimizga xos xususiyatlarni 
    def __init__(self) funksiyasiga argument sifatida uzatamiz. Bizning Car klassimiz brend, model, 
    name, year, prisega ega bo'ladi. 
Keyingi qatorlarda esa 'self.xususiyat = argument' komandasi yordamida uzatilgan argumentlarni 
    klassning xususiyatlari bilan bo'glayapmiz. Bu yerda xususiyat nomi uzatilgan argument nomi 
    bilan mos tushishi shart emas, unga istalgan nom berishimiz mumkin (masalan self.name = ism)
"""

""" Obyekt yaratish """        
# car1 = Car("BMW", "A21", 202, 23000)
# car2 = Car("Tesla", "Model S", 2020, 75000)
# car3 = Car("Toyota", "X2", 2018, 3400)

"""
car1 obyektimiz tayyor. Obyektni yaratish uchun Car klassiga murojat qildik va mashinaning modeli,
nomi, narxini parameter sifatida uzatdik. 
"""
   
""" Obyektning xususiyatlarini ko'rish """   
# print(car1.brend)   
# print(car1.model)   
# print(car1.prise)   
# print(car2.brend)    
   
""" Classga metod qo'shamiz 👆👆👆 """

#     def get_info(self):
#         return f"{self.brend} kompaniyasining  {self.model} rusumli aftomobili {self.year}-yilda ishlab chiqarilgan. Narxi: {self.prise} $"

# print(car1.get_info())
# print(car2.get_info())
# print(car3.get_info())


# def full_info(self):
#         """ Mashina haqida ma'lumot beruvchi funksiya  """
#         print(f"{self.brend} brendining {self.model} modeli. \nIshla chiqarilgan yili {self.year}. \nNarxi: {self.prise}")

# def get_year(self):
#         """ Mashinaning ishlab chiqarilgan yilini aniqlovchi metod(funksiya)"""
#         info = f"Ushbu mashina {self.year} da ishlab chiqarilgan"
#         return info
        
# def get_prise(self):
#         """ Mashinaning narxini aniqlovchi metod(funksiya)"""
#         return f"Ushbu mashina {self.prise} $ turadi"


# print(car1.full_info())   
# print(car1.get_year())   
# print(car1.get_prise())   
   

""" Argument qabul qiluvchi metodlar """
   
# def get_date(self, now=2023):
#         """ Mashina ishlab chiqarilgan vaqtgacha bo'lgan yil """
#         info = ''
#         year = now - self.year
#         if year:
#             info = f"Mashina ishlab chiqarilganiga {year} yil bo'lgan"
#         else:
#             info = "Mashina shu yili ishlab chiqarilgan" 
        
#         return info
   
# print(car1.get_date(2023))
# print(car1.get_date(2025))
   
   
"""
Vazifa:

1) Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda 
    ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
    Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan 
    ma'lumotlarni chiroyli qilib chiqarsin. 
    (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
    Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
    
2) Oila classini yarating Va 1-mashqdagi kabi shartlarni bajaring

"""
   
   
   
    
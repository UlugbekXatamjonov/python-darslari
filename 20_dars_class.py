"""
Thame: Classlar bilan ishlash
"""

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
    
#     def get_full_name(self):
#         return f"{self.ism} {self.familiya}"
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

# inson = Shaxs("Hasan","Alimov","FB001122",1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")



# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism,familiya,passport,tyil)
        
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.MANZIL = manzil

#     def get_id(self):
#         return f"Talaba ID: {self.idraqam}"
    
#     def update_bosqich(self):
#         # self.bosqich += 1
#         self.bosqich = self.bosqich + 1
#         return self.bosqich
    
#     def get_bosqich(self):
#         return self.bosqich
    
#     def get_info(self):
#         text = f"{self.ism} {self.familiya}."
#         text += f"\nPassport raqami: {self.passport} va {self.tyil} -yilda tug'ilgan"
#         text += f"\nTalabaning ID raqami: {self.idraqam} va u {self.bosqich}- bosqich talabasi."
#         return text
        
# talaba = Talaba("Valijon","Aliyev", "AB2345324", 2000, 123456789)

# print(talaba.get_info())
# print(talaba.get_age(2023))
# print(talaba.get_full_name())
# print(talaba.get_id())
# print(talaba.update_bosqich())



"""  Dastur davomida super klass voris klasslardan avval yozilgan (chaqirilgan) bo'lishi kerak """



""" Voris klass boshqa klass uchun super klass bo'lishi mumkin
    Voris klassga super klassdan meros qolgan istalgan metodni qayta talqin qilish mumkin
"""


""" POLIMORFIZM — Super class metodlarini qaytadan yozish """

# def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info



# print(talaba.get_info())


""" Obyekt ichida obyekt """

# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def __init__(self,uy,kocha,tuman,viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
    
#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil


""" Talaba klassimizga ham qo'shimcha manzil xususiyatini qo'shamiz """

# talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)

# print(talaba.MANZIL.get_manzil())
# print(talaba.MANZIL.tuman)

"""
Vazifa:

1)  Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin
    va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
    Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
    Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga 
    tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
    Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. 
    Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
    
    
2) Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, 
    Sotuvchi, Mijoz va hokazo)
    Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
    Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
    Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan 
    Admin klassini yarating. 
    Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga 
    "Foydalanuvchi bloklandi" degan matn chiqarsin.


"""
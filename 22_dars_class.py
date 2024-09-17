"""
Thame: Dunder metodlar
"""

"""
Pythonda obyektlar bilan ishlashni yanada qulay qilish uchun bir nechta maxsus metodlar bor. 
    Bu metodlarning nomi ikki pastki chiziq bilan yozilgani uchun, double underscore yoki qisqa qilib 
    dunder metodlar deb ataladi. Dunder metolar yordamida obyektlarga qo'shimcha qulayliklar va 
    vazifalar qo'shishimiz mumkin. Klass yoki obyektga oid dunder metodlar ro'yxatini ko'rish 
    uchun dir() funksiyasidan foydalanamiz

    link1 > https://mathspp.com/blog/pydonts/dunder-methods
    link2 > https://www.geeksforgeeks.org/dunder-magic-methods-python/
    link3 > https://python.sariq.dev/oop/32-dunder-metodlar

"""

# class Avto:
#     """Avtomobil klassi"""
#     num_auto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         Avto.num_auto += 1
        
#     def get_km(self):
#         return self.__km
    
#     def __str__(self): # obyekt haqida qisqacha malumot qaytaradi
#         return f"{self.make} kompaniyasining {self.model} rusumli mashinasi"

#     def __repr__(self):
#         text = f"{self.make} kompaniyasining {self.model} rusumli mashinasi"
#         text += f"\nRangi {self.rang}, Ishlab chiqarilgan yili {self.yil}"
#         text += f"\nNarxi {self.narh} $"
#         return text

#     def __eq__(self,boshqa_avto): # ==
#         narxi =  self.narh == boshqa_avto.narh
#         yili =  self.yil == boshqa_avto.yil
#         return f"Narxi: {narxi} / Yili: {yili}"
        
#     def __lt__(self,boshqa_avto): # <
#         return self.narh < boshqa_avto.narh
    
#     def __le__(self,boshqa_avto): # <=
#         return self.narh <= boshqa_avto.narh

# avto1 = Avto("GM","Malibu","Qora",2022,40000)
# avto2 = Avto("BMW","M7","Qizil",2022,40000)

# print(avto1)
# print(dir(avto1))

# print(avto1<avto2) # avto1 avto2 dan kichik mi?
# print(avto1<=avto2)

"""
Dunder metodlar ro'yhati:
    '__class__',
    '__delattr__',
    '__dict__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__le__',
    '__lt__',
    '__module__',
    '__ne__',  
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    '__weakref__'
"""

""" Obyekt haqida ma'lumot berish """
"""
def __repr__(self):
    Obyekt haqida ma'lumo
    return f"Avto: {self.rang} {self.make} {self.model}"
"""


""" Obyektlarni taqqoslash """
"""
    def __eq__(self,boshqa_avto):
        return self.narh == boshqa_avto.narh
    
    def __lt__(self,boshqa_avto):
        return self.narh<boshqa_avto.narh
    
    def __le__(self,boshqa_avto):
        return self.narh<=boshqa_avto.narh
"""


# class AvtoSalon:
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = [avto1, avto2]

#     def __repr__(self): # ma'lumot berish uchun / print(salon1)
#         return f"{self.name} avtosaloni"
    
#     def __len__(self): # ro'yhat uzunligini qaytarish uchun / print(len(salon1))
#         return len(self.avtolar)
    
#     def __getitem__(self,index): # obyekt elementlariga murojat qilish uchun  / print(salon1[0])
#         return self.avtolar[index]
    
#     def __call__(self): # obyekt elementlarini chaqirish uchun / salon1()
#         return [avto for avto in self.avtolar]

# salon1 = AvtoSalon("MaxAvto")
# print(len(salon1))
# print(salon1.avtolar[0])
# print(avto1)
# print(salon1())

""" 
Vazifa 

Mustaqil ravishda 5 ta dunder metodni o'rganib kelish va unga misol yozib kelish

"""



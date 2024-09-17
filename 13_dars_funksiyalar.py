"""
Thame: Funkcions(Funksiyalar)
"""

""" Funksiyadan qiymat qaytarish """
# def full_name(name, surname):
#     """ To'liq ism qaytaradigan funksiya """
#     name = f"{name.title()} {surname.title()}"
#     return name # qiymat qaytarish uchun return operatorini ishlatamiz

# full_name("ALi", "Olimov")

""" Funksiyamiz return operatori yordamida full_name degan o'zgaruvchining qiymatini qaytaradi"""

# person1 = full_name("ALi", "Olimov")
# person2 = full_name("Husan", "Hasanov")
# person3 = full_name("Aziza", "Olimova")

# print(person1)
# print(person2)


"""
    Qiymat qaytaradigan funksiyaning afzalligi shundaki, biz bu qiymatlardan keyin ham 
    bemalol foydalanishimiz mumkin.Funksiya ichidagi o'zgaruvchilar mahalliy yoki ichki 
    o'zgaruvchilar deyiladi (local variables). Ichki o'zgaruvchilar faqatgina funksiya 
    ichida mavjud bo'ladi, ularga tashqaridan murojat qilib bo'lmaydi. 
    Shuning uchun ham funksiya o'zgaruvchi emas qiymat qaytaradi.
"""

""" Ixtiyoriy qiymat berish """
# def full_name(name, surname, father_name=''):
#     """ To'liq ism qaytaradigan funksiya """
#     full_name = f"{name.title()} {surname.title()} {father_name.title()}"
#     return full_name # qiymat qaytarish uchun return operatorini ishlatamiz

# person1 = full_name("ALi", "Olimov", "Tolipovich")
# person2 = full_name("Husan", "Hasanov")
# print(person1)
# print(person2)


# def taqqoslash(son1, son2, son3):
#     x= max(son1, son2, son3)
#     return x
# a = taqqoslash(4,5,6)
# b = taqqoslash(22,43,-6)

# print(a)
# print(b)

""" Funksiyadan sodda qiymat emas, ro'yxat, lu'gat va boshqa ma'lumot turlarini ham  
    qaytarishimiz mumkin """
    
""" Funksiyadan lug'at qaytarish """
# def person_info(name, surname, birth, gender, age, job=None):
#     """ Inson haqidagi malumotlarni qaytaruvchi funksiya """
#     person = {
#         'name': name,
#         'surname': surname,
#         "birth": birth,
#         "gender": gender,
#         "age": age,
#         "job": job
#     }
#     return person

""" 'job' nomli parametrga 'None' standart qiymatini berib ketdik. 
    None Pythonda mavjud emas ma'nosini beradi, va if yordamida tekshirganda 
    False mantiqiy qiymatini qaytardi. 
"""
# person1 = person_info("Olimjon", "Vohidov", 1998, "erkak", 25, "quruvchi")
# person2 = person_info("Ahmad", "Abbosov", 1987, "erkak", 34)
# insonlar = [person1, person2]

# print(person1)
# print(person2)


""" 1-usul """
# print("Insonlar haqida malumotlar: ")
# for inson in insonlar:
#     print(f"{inson['name']} {inson['surname']}. {inson['birth']}-yilda tug'ilgan,\
# hozirda {inson['age']} yoshda. Jinsi {inson['gender']}. \
# Kasbi {inson['job']} ")

""" 2-usul """
# print("Insonlar haqida malumotlar: ")
# for inson in insonlar:
#     if inson['job']:
#         job = inson['job']
#     else:
#         job = "nomalum"
#     print(f"{inson['name']} {inson['surname']}. {inson['birth']}-yilda tug'ilgan,\
# hozirda {inson['age']} yoshda. Jinsi {inson['gender']}. \
# Kasbi {job} ")


""" Funksiyadan ro'yhat qaytarish """
# def oila(n):
#     """ Oila azolaringizning ismini ro'yhat holatida qaytaruvchi funksiya """
#     oila = []
#     for i in range(n):
#         azo = input(f"{i+1}- oila azongizning ismi :")
#         oila.append(azo)
#     return oila

# oila1 = oila(4)
# oila2 = oila(7) 
# print(oila1)
# print(oila2)


""" Funksiyani tsiklda ishlatish """
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("\nIshlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    # avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break


# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['kompaniya']} {avto['rang']} {avto['model']}. Narhi: {narh}")

""" pass operatori """
"""
pass - operatori malum vaqt funksiyani ishlatmaslik kerak bo'lganda kerak bo'ladi
# """
# def name(ism):
#     pass
    
# name("Abbos")

# def name(ism):
#     pass

"""
Vazifa:

1) Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va 
    telefon raqamini qabul qilib, lug'at ko'rinishida malumot qaytaruvchi funksiya yozing. 
    Lug'atda foydalanuvchi yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy 
    qiling (masalan, tel.raqam, el.manzil)

2) Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan 
    ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

3) Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

4) Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
    perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

5) Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya 
    yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan 
    katta musbat sonlar)

6) Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi 
    sonlar ro'yxatni qaytaruvchi funksiya yozing.  
    Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan 
    ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 
    1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
    
"""
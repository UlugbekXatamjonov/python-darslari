"""
Thame: Dictionary(Lug'atlar)
"""

taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa",
    'nodir':"kabob",
}

""" 
taomlar = {'ali':'osh'}
nomi    = {'key':'value'}
"""

print(f"Alining sevimli taomi {taomlar['ali']}")
print(f"Husanning sevimli {taomlar['husan']}")
print(type(taomlar))

buyumlar = {
    "ism":"Ali",
    "yosh":12,
    "student":True,
    "oila":["ota","ona",'aka']
}
print(buyumlar)


""" Qiymat qo'shish """
taomlar["nodir"] = 'norin'
taomlar['azimjon'] = int(input("Azimjoning taomi ? "))
print(taomlar)

taomlar.update({"akramjon":"lag'mon"})
print(taomlar)



""" Qiymatni o'zgartirish / update() """
taomlar["hasan"] = 'qozon_kabob'
print(taomlar)

taomlar.update({"olin":"manti"})
print(taomlar)

""" Qiymatni o'chirish """
del taomlar["olim"]
print(taomlar)

taomlar.pop("hasan")
print(taomlar)

taomlar.popitem() # ro'yhatning oxiridagi elementni olib tashlaydi
print(taomlar)

""" Ro'yhatni tozalash """
taomlar.clear()
print(taomlar)

""" Ro'yhatdan nusha olish """
meals = taomlar.copy()
print(meals)

meals2 = dict(taomlar)
print(meals2)

""" get() metodi """
print(taomlar["abror"])
print(taomlar.get("nodir","Bunday key yo'q"))

""" items() metodi """
print(taomlar)
print(taomlar.items())
for key, value in taomlar.items():
    print(f"{key.title()}ning sevimli taomi {value.title()}")
    
davlatlar = {
    'uzbekistan':"Tashkent",
    'usa':"Vashington",
    'russian':"Russian",
}
savol = input("Davlat nomini kiriting: ").lower()
if savol in davlatlar:
    print(f"Siz so'ragan {savol.upper()}ning poytaxti {davlatlar[savol].title()}")
else:
    print(f"Siz so'ragan {savol.title()} haqida bizda malumot yo'q")

""" keys() va values() metodlar """
print(davlatlar.keys())
print(davlatlar.values())

for key in davlatlar.keys():
    print(f"{key}")

for value in davlatlar.values():
    print(f"{value}")

ismlar = {
    '1':'Ali',
    '2':'Hasan',
    '3':'Husan',    
}
for kalit, qiymat in ismlar.items(): # items --> buyhum 
    print(f"Salom do'stim {qiymat} sening tartib raqaming {kalit}")

for key in ismlar.keys(): # key
    print(f"Salom do'stim sening tartib raqaming {key}")

for qiymat in ismlar.values(): # value   
    print(f"Salom do'stoim {qiymat}")
    
    
"""" Mashqlar """
oila = {}
print(oila)

oila['ota'] = input("Otangizni ismi: ")
print(oila)

oila['ona'] = input("Onangizni ismi: ")
oila['aka'] = input("Akangizni ismi: ")
oila['opa'] = input("Opangizni ismi: ")
print(oila)


""" Do'kon """
mahsulotlar = {
    "olma":4500,
    "nok":2000,
    "non":3000,
    "asal":15000,
    "tuz":2500,    
}


zakaz = []
narx = 0
yoq = []
print("Assalomu aleykum do'konimizga hush kelibsiz !")
son = int(input("\nNechta mahsulot sotib olishni hohlaysiz: "))# foydalanuvchi olmoqchi bo'lgan mahsulotlari soni

print("Bizning do'konda quidagi mahsulotlar bor: ")
for m in mahsulotlar:
    print(f"{m.title()}", end=' ')# do'konimizdagi mahsulotlarni eslatib o'tamiz

for n in range(son): #mahsulotlarni birma bir so'raymiz
    xarid = input(f"\n{n+1}-mahsulot: ").lower()
    zakaz.append(xarid)

for k,v in mahsulotlar.items(): # sotib olingan mahsulotlar agar do'konimizda bo'lsa ularning narxini hisoblaymiz   
        if k in zakaz:
            narx += v 
            
print("Siz sotib olmoqchi bo'lgan mahsulotlar quidagilar: ") #sotib olingan mahsulotlarni va ularning ummumiy narxini chiqaramiz
for z in zakaz:
    if z in mahsulotlar:
        print(f"{z.title()}", end=" ")
    else: 
        yoq.append(z)


print(f"va ularning ummumiy narxi: {narx} so'm") # do'konimizda yo'q mahsulotlarni eslatamiz
print("Quidagi mahsulotlar esa bizning do'konda mavjud emas: ")
for y in yoq:
    print(f'{y.title()}', end=' ')



"""
Vazifa:

1) otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta 
    m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
    konsolga chiqaring M: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
    
2) Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
    
3) Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z(atamani) kiriting 
    (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
    
4) Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
    Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
 
6) Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va 
    qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
    
7) Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni 
    alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
    
8) Foydalanuvchidan istalgan davlatni kiritishni so'rang agar foydalanuvchi davlar kiritsa uning poytaxini, 
    poytaxt kiritsa uning davlatini konsulga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
    "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
    
9) Restoran menusi lug'atini tuzing(kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat
    buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda 
    bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
"""

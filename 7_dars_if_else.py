"""
Thame: if-else-elif operatorlari
"""

""" if-else """
a = 4 
b = 2
# if a > b: # 1-usul
#     print(a)
# else:
#     print(b)

# if a > b: print(a) # 2-usul
# else: print(b)

""" == """
ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh']
# for ism in ismlar: # == -> teng bo'lsa, tengmi ?
#     if ism == 'Olim': # if - Agar / Agar ism 'Ali' ga teng bo'lsa
#         print(f"Salom {ism} Admin, sizga yangi habar bor")
#     else:# else - yoki, boshqa barcha holatlarda
#         print(f"Salom {ism}")

""" != """
# for ism in ismlar: 
#     if ism != "Olim": # teng bo'lmasa
#         print(f"Salom {ism}, Olim kelmadimi ?")
#     else:
#         print(f"Salom {ism}")

""" elif """
# sonlar = [1,2,3,4,5,6,7,8,9,10]

# for son in sonlar:
#     if son < 5 : # agar son 5 dan kichik bo'lsa
#         print(f"{son} 5 dan kichik")
#     elif son == 5: # yoki 5 ga teng bo'lsa/ elifni istalgancha ishlatish mumkin
#         print(f"{son} 5 ga teng")
#     else: # qolgan barcha holatlarda
#         print(f"{son} 5 dan katta")

"""
    ==  -> teng bo'lsa
    !=  -> teng bo'lmasa
    >   -> katta bo'lsa
    <   -> kichik bo'lsa
    >=  -> katta yoki teng bo'lsa
    <=  -> kichik yoki teng bo'lsa
    or   -> yoki
    and  -> va 
"""
""" or va and """
sonlar = [1,2,3,4,5,6,7,8,9,10]
for son in sonlar:
    if son < 5 or son > 5: # agar son 5 ga teng yoki son 5 dan katta bo'lsa
        print(f"{son} 5 ga teng emas")

for son in sonlar:
    if son > 0 and son%2==0:
        print(son)

""" if ichida if """
son = 0
if son > 0:
    if son%2==0:
        print(f"{son} juft")
    else:
        print(f"{son} toq")
else:
    print("Son  musbat emas")
              
son = int(input('Juft son kiriting >>>'))
if son%2!= 0 :
    print('Bu juft son emas !')
else :
    print("Rahmat")
        
""" pass """
son = -7
if son > 0:
    pass
    print(son)

""" 1-misol """
son = int(input("Alining baxosini kiriting(10 ballik sistemada): "))
if son >= 1 and son < 4:
    print("qoniqarsiz baxo")
elif son >= 4 and son <= 7:
    print("yaxshi")
elif son >= 8 and son <=10:
    print("alo")
elif son <= 0 or son >10:
    print("Kiritilgan son xato. 1-10 oralig'idagi son tanlang")

""" 2-misol """
son = int(input("Istalgan son kiriting: "))
if son > 0:
    print(f"{son} musbat")
elif son == 0:
    print(f"{son} 0 ga teng")
else: 
    print(f"{son} manfiy")

""" 3-misol """
a = float(input("1-sonni kirirting:"))
b = float(input("2-sonni kirirting:"))
if a>b:
    print(f"{a}>{b}")
elif a<b:
    print(f"{a}<{b}")
else :
    print(f"{a}={b}")

""" 4 """
son = int(input("Son kiriting: "))
if son == 1:
    print("Dushanba")
elif son == 2:
    print("Seshanba")
elif son == 3:
    print("Chorshanba")
elif son == 4:
    print("Payshanba")
elif son == 5:
    print("Juma")
elif son == 6:
    print("Shanba")
elif son == 7:
    print("Yakshanba")

""" ZOO """
yosh = int(input("Yoshingiz nechida: "))
if yosh >= 1 and yosh < 101:
    if yosh <= 7 or yosh >= 70:
        narx = 'bepul'
    elif yosh > 7 and yosh < 18:
        narx = 5_000
    elif yosh >= 18 and yosh < 70:
        narx = 10_000
    if narx == 'bepul':
        print(f"Sizga kirish {narx}")
    else:
        print(f"Sizga kirish {narx} so'm")
elif yosh > 101:
    print(f"Siz xato son kiritingiz")
else:
    print(f"Musbat son kiriting")

    
    
""" 
Vazifa:
1)
dastur: Assalomu aleykum do'konimizga hush kelibsiz !
dastur: Bizda quyidagi mahsulotlar bor: olma, anor, non, shakar, tuz, qaymoq
        Nechta mahsulot sotib olmoqchisiz ?
foydalanuvchi: 4
dastur: 1-mahsulotni kiriting:
foydalanuvchi: olma
dastur: 2-mahsulotni kiriting:
foydalanuvchi: non
dastur: 3-mahsulotni kiriting:
foydalanuvchi: sut
dastur: 4-mahsulotni kiriting:
foydalanuvchi: tuz
dastur: 5-mahsulotni kiriting:
foydalanuvchi: anjir
dastur: Siz tanlagan quyidagi mahsulotlar do'konimizda bor: olma, non, tuz
        Quyidagi mahsulotlar esa do'konimizda yo'q: sut, anjir
        Haridingizdan mamnunmiz ! 

2)
dastur: Assalomu aleykum UITC Academiyasiga hush kelibsiz !")
        Bizning Academiyamizda quyidagi kurslar mavjud: Frontend, Backend, Grafik dizayn, 3D modeling
        Siz qaysi kursni tanlaysiz ?
foydalanuvchi: frontend
dastur: Bizda bunday kurs yo'q iltimos to'gri yozing(agar ro'yhatdagi yo'q kurs kiritilsa)
        Front end ursining narxi 500,000 so'm

3) Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
    -ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
    -GM uchun ikkala harfni katta qiling.
    -Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
    
4) Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini 
    hisoblab konsolga chiqaring. 
    -Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 

5) Parol tizimi. Foydalanuvchidan parol o'rnatishini so'rang. u ikki marta parol kiritsin.
    Kiritiladigan parol eng kamida 8ta belgiga teng bo'lishi kerak.
    Agar ikkala parol bir biriga teng bo'lsa; "Parol fuvaffaqiyatli o'rnatildi" degan
    habar chiqsin. Agar teng bo'lmasa "Xatolik ! Iltimos parolni boshqatdan kiriting"
    degn habar chiqsin.
    -va keyin parolni foydalanuvchidan boshqattan so'rasin, agar foydalanuvchi o'zi kiritgan
    parolni to'g'ri kiritsa, "Hush kelibsiz Admin" desin. Agar parol noto'g'ri kiritilsa
    "Parol xato" degan xabar chiqasin.

6) uchta haqiqiy son berilgan ulardan musbatlarining kubini chiqaradigan dastur tuzing.

"""



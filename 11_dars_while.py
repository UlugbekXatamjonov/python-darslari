"""
Thame: While tsikli
"""
sonlar = [1,2,3,4,5,6,7,8,9,10]
for son in sonlar:
    print(son)

""" 1 """
son = 1
while son < 100:
    print(son)
    son += 1 
    

""" 2 """
x = 1
s = 0
while x < 20:
    if x%2==0:
        s = s+x 
        print(x)   
    x = x+11
print(s)

""" 3 """
while True: # abadiy tsikl
    savol = input("son kiriting: ")
    if savol.isdigit():
        print(int(savol)**2)
    elif savol == 'exit':
        break # tsiklni to'xtatish uchun 
    else:
        print("son kiriting!!!")

""" Tug'ilgan yil """
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        if int(yosh) >= 10 and int(yosh) <= 110:
            print(f"Siz {2023-int(yosh)}-yilda tug'ilgansiz")
        else:
            print("Siz noto'g'ri yosh oralig'ini kiritingiz")
    elif yosh == "exit":
        print("Dastur tugadi")
        break
    else:
        print("Siz son kiritmadingiz !!!")
 

""" Abadiyt tsikl """
x = 1
while x < 10:
    print(x)


""" ishora """

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")

ishora = True
while ishora: # = while True -> abadiy tsikl
    savol = input("Istalgan son kiriting(dasturni to'xtatish uchun 'exit' deb yozing):")
    if savol == 'exit':
        ishora = False # dastur to'xtashi uchun
    elif savol.isdigit() or float(savol):
        print(float(savol)**2)
    else:
        print("Siz son kiritmadingiz!!!")


""" continue """
sonlar = [1,2,3,4,5,6,7,8,9,10]
for son in sonlar:
    if son == 6:
        continue # davom etish / bu holatda 6 ni tashlab o'tib ketadi
    else:
        print(son, end=' ')
   
ishora = 1 # 1 = True
while ishora:
    son = input("Son kiriting: ")
    if son.replace('.','').isdigit(): # !!!!
        if float(son) == 0:
            continue
        else:
            print(f"100 ni {son} ga bo'lsak {100/float(son)} chiqadi")
    elif son == 'no':
        print("dastur tugadi")
        ishora = 0 # 0 = False
    else:
        print("Siz son kiritmadingiz !!!")



""" while va else """
x = 0
while x < 3:
    print(f"{x+1}-print")
    x = x + 1
else:
    print('end print')

""" while do ga misol """
""" While - shartni tekshirib keyin kodni bajaradi
    While do - avval kodni bajarib keyin shartni tekshiradi
    Pythonda while do aslida yo'q. Lekin quyidagi misol orqali uning 
    qanday ishlashini tushuntirishimiz mumkin. 
"""
i = 1  
while True:  
    print(i)  
    i = i + 1  
    if(i > 5):  
        break  
    
""" parol tizimi """ 
parol = "www"
while True:
 	savol = input("Parolni kiriting: ")
 	if savol == parol:
        break
 	else:
		 print("parol xato !!!")

""" 
Vazifa

1) Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
    Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
    
2) Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
to'xtasin (ikkita shartni ham tekshiring). Yuqoridagi dasturni turli usullarda
yozib ko'ring (break, ishora)

3) Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

4) Foydalanuvchidan tizimga kirishi uchun parol so'rang, foydalanuvchi to'gri javob 
kiritsa unga 'hush keib siz' degan habar chiqsinva dastur to'xtasim. 
Agar foydalanuvchi 3 marta xato parol kiritsa uni abadiy tsiklga tushurib qo'ying.  

5) Online bozor loyihasini qiling. Avvaliga foydalanuvchiga do'koningizdagi mahsulotlarni nomi va narxini ko'rsating,
song foydalanuvchidan nima olishini so'rang, keyin xaridni davom etirasizmi yoki yo'q deb so'rang
agar ha desa yana mahsulot nomini so'rang, agar yoq dasa jarayoni tugatib, sotib olgan mahsulotlari va 
ularning narxini ko'rsating. 

6) 1 dan 100 gacha bo'lgan toq sonlar yig'indisini toping.

"""

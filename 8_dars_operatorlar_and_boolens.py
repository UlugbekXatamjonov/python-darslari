"""
Thame: Operators va Boolens / Operatorlar
"""

""" Boolen / Mantiqiy qiymatlar """
"""
Mantiqiy qiymatlarning 2 turi mavjud True va False
Ikki qiymatni solishtirganda, ifoda baholanadi va Python mantiqiy javobni qaytaradi.
True/False bilan teng kuch bilan 1/0 ham ishlatiladi.
"""
# print(5 > 10) # False
# print(5 == 10) # False
# print(5 < 10) # True

""" if-else """
# a = 17
# b = 14
# if a > b:
#     print(f"{a} {b} dan katta")
# else:
#     print(f"{b} {a} dan kichik")


""" bool() funksiyasi """
""" bool() funksiyasi har qanday qiymatni baholashga imkon beradi va bizga True yoki False javobini qaytaradi """
# matn =  ""
# son = -9
# print(bool(matn))
# print(bool(son))

# x = "Salom"
# y = 17
# print(bool(x)) # o'zgaruvchi sifatida
# print(bool(y))

# yosh = input("Yosh kiritng: ")
# if bool(yosh):
#     print("Rahmat")
# else:
#     print("Siz hechnima kiritmadingiz!!!")

"""
Deyarli har qanday qiymat, agar u bo'sh bo'lmasa --> True
Bo'sh matnlardan tashqari har qanday matn --> True
Har qanday raqam , agar u 0 bo'lmasa --> True
Har qanday Tuple, List, Set va Dictionary, agar u bo'sh bo'lmasa --> True
"""

# print(bool("Assalomu aleykum"))
# print(bool(123))
# print(bool(["Ali", "Olim", "Anvar"]))
# print(bool({"ism":"Ali", "yosh":23}))
# print(bool({23,"ism","daraxt"}))


# print(bool(""))
# print(bool(0))
# print(bool([]))
# print(bool({}))
# print(bool(()))

""" Masalalar """
# ism = input("ismingizni kiriting: ")
# if bool(ism):
#     print(ism)
# else:
#     print("Siz hech nima kiritmadingiz.")


""" Operators / Operatorlar """
"""
Operatorlar o'zgaruvchilar va qiymatlar ustida amallarni bajarish uchun ishlatiladi.

-Arifmetik operatorlar
-Belgilash operatorlari
-Taqqoslash operatorlari
-Mantiqiy operatorlar
-Identifikatsiya operatorlari
-A'zolik operatorlari
-Bitli operatorlar

"""

"""
Arifmmetik Operatorlar

+	Qo'shish	        x + y	
-	Ayrish	            x - y	
*	Ko'paytirish	    x * y	
/	Bo'lish	            x / y	
**	Darajaga ko'tarish	x ** y	
//	Yaxlidlab bo'lish	x // y
%   Qoldiqli bo'lish	x %  y
""" 
# a = 15
# b = 7
# print(a//b)


"""
Belgilash operatorlari

=	   x = 5	  x = 5	
+=	   x += 3	  x = x + 3	
-=	   x -= 3	  x = x - 3	
*=	   x *= 3	  x = x * 3	
/=	   x /= 3	  x = x / 3	
//=	   x //= 3	  x = x // 3	
**=	   x **= 3	  x = x ** 3
%=	   x %= 3	  x = x % 3
	
"""

# x = 5

# x **= 3 # x = x ** 3
# print(x)

# x //= 3 # x = x // 3
# print(x)


"""
Taqoslash operatorlari

==	Tengmi	            x == y	
!=	Teng emasmi	        x != y	
>	Katta	            x > y	
<	Kichik	            x < y	
>=	Katta yoki teng	    x >= y	
<=	Kichik yoki teng	x <= y

"""
# a = 3
# b = 4
# print(a > b)
# print(a < b)
# print(a == b)
# print(a <= b)


""" 
Mantiqiy operatorlar 
x=7

and 	Ikkala shart to'gri bo'lsa 	            x < 5 and  x < 10	
or	    Ikkala shartdan biri to'gri bo'lsa	    x < 10 or x < 5	
not	    Inkor. Ikkala shart to'gri bo'lsa	    not(x < 5 and x < 10)

"""
# x = 5
# print(x > 3 and x < 10)
# print(x < 7 or x < 4)
# print(not(x < 5 and x < 10))

"""
Identifikatsiya operatorlari

is          Agar ikkala o'zgaruvchi ham bir xil ob'ekt bo'lsa       True
is not      Agar ikkala o'zgaruvchi ham bir xil ob'ekt bo'lmasa !   True

"""
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z) # True > chunki x ning obyetklari z niki bilan birxil va joylashuvi ham birxil

# print(x is y) # False > chunki x ning obyetklari z niki bilan birxil ammo  joylashuvi birxil emas !

# print(x == y) # "is" va "==" o'rtasidagi farqni ko'rsatish uchun: bu taqqoslash True qaytaradi, chunki x y ga teng


"""  
A'zolik operatorlari

in          Agar 'x' 'y'ni ichida bo'lsa        True
not in      Agar 'x' 'y'ni ichida bo'lmasa      True

"""
# y = ['olma',  'gilos', 'anor']

# print('olma' in y)
# print('shaftoli' not in y)







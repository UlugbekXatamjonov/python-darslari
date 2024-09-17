"""
Thame: Matnlar(String) bilan ishlash
"""

""" Matnlar """
print("Bu matn edi")
matn = "O'zbekiston Respublikasi"
python = "Python the best programming language"
print(matn)
print(python)

""" "" va '' """
print("o'g'il")
print('o\'g\'il')

print("Bugun Anvar \"katta\" mashinada keldi.")
print('Bugun Anvar "katta" mashinada keldi.')

""" Atributlar / metodlar"""
shaxar = "NamangaN shaXar uychi Tumani"
print(shaxar)
print(shaxar.title()) # Birinchi harifni katta qilib chiqaradi
print(shaxar.upper()) # barcha so'zlardagi harflarni katta qilib beradi
print(shaxar.capitalize()) # matndagi 1-harfning 1-so'zini katta qilib beradi
print(shaxar.lower()) # barcha so'zlarni kichkina qilib beradi

"""  strip()  """
a = "   Hello, World!   "
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

""" f"" bilan ishalash""" # f"" --> f string"
a1 = 3
b1 = 2
c= a1+b1
print(a1, "+", b1, "=", c)
javob = f"{a1} + {b1} = {c}"
print(javob)

ism = "olim"
familya = "hasanov"
full_name = f"Salom mening ismim {ism} va familyam {familya}"
print(full_name)

""" imput() """
ism = input("Ismingiz nima: ")
familya = input("Familyangiz nima: ")

full_name = ism + ' ' + familya
print(full_name.title())


""" print() va comment """
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


   

""" matnni tekshirish """
txt = "Python the best programming language in the world"
print("best" in txt)

""" teskari tekshirish """
txt = "Python the best programming language in the world"
print("php" not in txt)

""" Matinni kesib chiqarish """
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

""" replace() """
a = "Hello, World!"
print(a.replace("H", "J"))


""" split() """
a = "Hello, World!"
print(a.split(","))

""" Matnlarni qo'shish """
a = "Hello"
b = "World"
c = a + b
print(a)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

""" Maxsus belgilar """
# \'    ' belgisi uchun
# \"    " belgisi uchun
# \n    Yangi qator
# \r    Yangi qator
# \t    Tab tashlab beradi
# \b    bo'shqilni yo'qotib beradi


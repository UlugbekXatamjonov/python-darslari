"""
Thame: Classlar bilan ishlash
"""
""" Obyektlar o'rtasidagi munosabat """

# class MyLibrary:
#     """ Kutubxona classi """
#     def __init__(self, NAME, ADRESS):
#         self.name = NAME
#         self.adress = ADRESS
#         self.books = [] # kitoblar
#         self.books_count = 0 # kitoblar miqdori
        
#     def get_info(self):
#         text = f"{self.name} kutubxonasining Manzili: {self.adress} "
#         text += f"Kitoblar soni {self.books_count} ta. "
#         return text
    
#     def add_book(self, new_book):
#         self.books.append(new_book)
#         self.books_count += 1

#     def get_books(self):
#         return [book.get_book_info() for book in self.books]
    
#     """
#     for book in self.books
#         book.get_book_info()
#     """
    
            
    
# mylibrary1 = MyLibrary("Common Library", "A. Navoiy ko'chasi 34-uy")
# print(mylibrary1.get_info())
    
    
# class Book:
#     """ Kitob haqidagi class """
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
        
#     def get_book_info(self):
#         return f"\"{self.name}\" kitobining muallifi {self.author}. Kitob {self.year}-yili chiqarilgan."


# book1 = Book("101 day", "Jek Darken", 2019)
# book2 = Book("Bad habbits", "Drayn Pool", 1988)

# print(book1.get_book_info())
# print(book2.get_book_info())+3

# print(mylibrary1.get_info())

# mylibrary1.add_book(book1)
# mylibrary1.add_book(book2)

# print(mylibrary1.get_books())


""" Obyektning hususiyat va metodlarini ko'rish  """
""" dir() funksiyasi """
# from pprint import pprint # prety print
# 
# pprint(dir(mylibrary1))
# pprint(dir(book1))


""" __dict__ metodi """
""" __dict__metodi obyketning xususiyatlarini lug'at ko'rinishida qaytaradi """
# print(mylibrary1.__dict__)
# print(book1.__dict__)
# print(book2.__dict__)


""" Amaliy mashg'ulot """
""" Avto salon va Avtomobil classlarini yarating. Har ikkala kalasda classning hususiyatlarini haqida 
    ma'lumot beruvchi va o'zgartirivchi metodlar yozing. AS(Avto Salon) classi da Avtomobil clasi obyekt
    larini o'zida jamlagan avtomobillar nomi ro'yhat bo'sin va shu ro'yhatda add_avto metodi yordamida 
    avtomobillar qo'shing
"""


""" Vazifa """
""" 
Oila va Inson klasini yarating va dars davomida classlar ustida ishlaganimiz dek shu klaslar bilan ishlang.
"""




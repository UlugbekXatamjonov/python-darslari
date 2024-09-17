"""
Thame: Classlar bilan ishlash
"""
""" Classlarga argument sifatida turli ma'lumot turlarini uzatish """
class Student:
    """ O'quvchi classi """
    def __init__(self, FULL_NAME, YEAR, MARKS,FRIENDS, FACULTY,LEVEL=1,):
        """ Student haqidagi malumotlarni o'zida saqlovchi funksiya """
        self.full_name = FULL_NAME
        self.year = YEAR
        self.marks = MARKS
        self.friends = FRIENDS
        self.faculty = FACULTY
        self.level = LEVEL

    def get_name(self):
        return self.full_name
    
    def get_info(self):
        return f"{self.full_name} {self.year} yoshda. Va u {self.level} - bosqich talabasi "
    
    def get_marks(self):
        text = f"\t{self.full_name}ning olgan baholari:\n"
        for fan, baho in self.marks.items():
            text += f"{fan} - {baho}\n"
        return text
    
    def get_friends(self):
        text = f"{self.full_name}ning ulfatlari:\n"
        for i in self.friends:
            text += f"{i}  "
        return text
    
    def set_level(self, new_level):
        self.level = new_level
        return self.level
    
    def update_level(self):
        if self.level < 4:
            self.level += 1
        else:
            return "5 - bosqich mavjud emas !!!"
        return self.level
    
    def get_faculty(self):
        return f"{self.full_name} {self.faculty}  fakulteti talabasi"
    
    def set_faculty(self, new_faculty):
        self.faculty = new_faculty
        return self.faculty

baxolar = {
    'matematika':3, 
    "ingliz_tili":5, 
    "ona_tili":5, 
    "geografiya":4
}
friends = ['Ali', "Olim", "Hasan", "Husan", "Vali"]

student1 = Student("Aziz Alimov",23,baxolar, friends, 'Matematika', 4)
# student2 = Student("Olimjon", 43,baxolar, friends)
# student3 = Student("Boburov", 1999, baxolar, friends)
# student4 = Student("Nodira Jamilova", 2002, {'matematika':5, 
#                                             "ingliz_tili":4, 
#                                             "ona_tili":3, 
#                                             "geografiya":5
#                                         }, ['Guli', "Aziza", "Husnora", "Madina", "Barno"])
# print(student1.get_marks())
# print(student1.get_friends())

# print(student1.set_level(3))
# print(student1.get_info())

print(student1.get_faculty())
print(student1.set_faculty('Iqtisot'))
print(student1.get_faculty())



""" 
Vazifa:

1) Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar
    (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart 
    qiymat bering (masalan, kilometer=0). Avto ga oid obyektning xususiyatlarini qaytaradigan 
    metodlar yozing. get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
    update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
"""





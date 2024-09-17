"""
Thame: Fayllar bilan ishlash
"""

""" 1-usul """
# with open('D:/projects/my_lessons/python_lessons/vazifa/text.txt') as fayl:
#     pi = fayl.read()
# print(pi)

"""
Birinchi qatorda open() funksiyasi yordamida faylni ochayapmiz. Bunda funksiyaga argument 
    sifatida fayl nomini berayapmiz. Bu yerda biz ochayotgan fayl va dasturimiz bir papkada bo'lishi muhim.
    open() funksiyasi faylni obyekt sifatida qaytaradi, as operatori yordamida esa biz obyektimizga 
    fayl deb nom berayapmiz.  Ikkinchi qatorda .read() metodi yordamida fayl obyektining tarkibidan 
    bizga kerakli matnni olib, yangi, PI o'zgaruvchisiga yuklayabmiz. with operatorining vazifasi biz fayl
    bilan ishlab bo'lganimizdan so'ng faylni yopish. Yuqoridagi misolda, 2-qatordan so'ng Python zudlik 
    bilan faylni yopadi.
"""

""" 2-usul """
# fayl = open('D:/projects/my_lessons/python_lessons/vazifa/text.txt')
# PI = fayl.read() # fayl.read(15) -> 15 birinchi 15 ta belgisini o'qish uchun  
# print(PI)
# fayl.close()

"""
Lekin, bu usul xavfli hisoblanadi va tavsiya qilinmaydi. Gap shundaki, open() funksiyasi yordamida 
    faylni ochganimizdan keyin, toki close() metodini chaqirgunga qadar faylimiz ochiq holatda turadi. 
    Agar, faylni vaqtida yopmasak, yoki fayl yopilmasidan avval dasturimiz to'xtab qolsa fayl 
    tarkibiga ziyon yetishi, ma'lumotlar yo'qotilishi mumkin.

    open() funksiyasiga with orqali murojat qilganimizda, faylimiz with blokining oxirigacha ochiq turadi, 
    va with tugashi bilan, fayl ham yopiladi.

    Matn faylda qanday saqlangan bo'lsa, huddi shu ko'rinishda konsolga chiqdi. 
    Saqlangan ma'lumot son bo'lsada, fayldan o'qiganimizda qaytgan qiymat matn ko'rinishida bo'ladi
    
"""

""" Faylni qatorma-qator o'qish """
""" 1-usul """
# with open('D:/projects/my_lessons/python_lessons/vazifa/text.txt') as file:
#     for line in file:
#         print(line)

""" 2-usul """
# with open('D:/projects/my_lessons/python_lessons/vazifa/text.txt') as file:
#     print(file.readline()) # bir qatorni o'qish
#     print(file.readlines()) # barcha qatorlarni o'qish
    

""" Faylga yozish """
""" 
Yuqorida biz faylni ochishda open() funksiyasidan foydalandik, va yagona argument sifatida fayl nomini berdik. 
    Bunda fayl faqatgina o'qish uchun ochiladi, unga yozib bo'lmaydi. Faylga ma'lumot yozish uchun open() 
    funksiyasiga murojat qilishda fayl nomidan tashqari yana bir argument beramiz. Ikkinchi argument faylni 
    aynan nima maqsadda ochishimizni bildiradi. 

-------------------------------------------------------------------------------------------------------------
'w'       open('file.txt','w')      Faylni yozish uchun ochish. Fayl mavjud bo'lmasa yangi fayl yaratiladi. 
                                    Fayl mavjud bo'lsa tarkibi o'chib ketadi

'r'     open('file.txt','r')        Faylni faqat o'qish uchun ochish (yozib bo'lmaydi)

'w+'    open('file.txt','w+')       Faylni o'qish va yozish uchun ochish. Fayl mavjud bo'lmasa yangi 
                                    fayl yaratiladi. Fayl mavjud bo'lsa tarkibi o'chib ketadi. 

'r+'    open('file.txt','r+')       Faylni o'qish va yozish uchun ochish.

'a'     open('file.txt','a')        Faylga ma'lumot qo'shish uchun ochish. 
                                    Fayl mavjud bo'lmasa yangi fayl yaratiladi.

'a+'    open('file.txt','a+')       Faylga ma'lumot qo'shish va o'qish uchun yozish. 
                                    Fayl mavjud bo'lmasa yangi fayl yaratiladi.

'x'     open('file.txt', 'x')       Fayl yaratadi, agar fayl mavjud bo'lsa, xatoni qaytaradi
-------------------------------------------------------------------------------------------------------------

❗❗❗ Diqqat!!! open() funksiyasini 'w' argumenti bilan chaqirganimizda ehtiyot bo'lishimiz kerak, 
    sababi agar bunday fayl mavjud bo'lsa, uning ichidagi barcha ma'lumotlar o'chib ketadi.

    Faylga yozayotgan ma'lumotlarimiz matn ko'rinishida bo'lishi kerak. Aks holda dasturimiz xato beradi.
❗❗❗ 

"""

faylnomi = 'D:/projects/my_lessons/python_lessons/text.txt'
with open(faylnomi,'r+') as fayl:
    x = fayl.read()
    print(x)

"""
Agar dastur davomida turli o'zgaruvchilarni faylda saqlash talab qilinsa pickle modulidan foydalanamiz. 
    Pickle ma'lumotlarni biz qanday ko'rinishda bersak, shunday ko'rinishda faylga yozadi. 
    Yuqoridagi usuldan farqli ravishda, pickle yordamida yozilgan fayllarning tarkibini 
    Pythondan tashqarida ko'rib bo'lmaydi. 

Faylni ochishda esa, open() funksiyasiga ikkinchi argument sifatida 'wb' (write binary) beramiz, 
    ya'ni ikkilik sanoq tizimida o'qishni ko'rsatamiz. Faylga yozish uchun esa pickle.dump() 
    metodidan foydalanamiz:
"""

# import pickle

# talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
# talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

# yozish
# with open('info.AAA','wb') as file: # 'wb'-> write binary -> ikkilik sanoq tizimida yozishni ifodalaydi
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)

# o'qish
# with open('info.AAA','rb') as file: 
#     print(type(pickle.load(file)))
    
"""
Pickle fayldan o'qish uchun open() funksiyasini 'rb' (read binary) argumenti bilan chaqiramiz. 
    O'zgaruvchilarni bitta faylga yozganimizda, har bir o'zgaruvchi alohida qatordan yoziladi. 
    Fayldan o'qishda ham har bir qatorni alohida o'qishimiz kerak bo'ladi.
"""
# with open('info','rb') as file: # 'rb' -> read binary -> ikkilik sanoq tizimida o'qishni ifodalaydi
#     talaba2 = pickle.load(file)

# print(talaba1)
# print(talaba2)

""" Faylni o'chirish """
"""
Faylni o'chirish uchun siz OS modulini import qilishingiz va uning os.remove()funksiyasini 
    ishga tushirishingiz kerak:
Xatolik kelib chiqmasligi uchun faylni o'chirishdan oldin uning mavjudligini tekshirishingiz kerak.
Butun 'papka'ni o'chirish uchun  'os.rmdir()' usuldan foydalanamiz.
"""
# import os

# if os.path.exists("D:/projects/my_lessons/python_lessons/text.txt"):
#   os.remove("D:/projects/my_lessons/python_lessons/text.txt")
# else:
#   print("Bunday fayl mavjud emas !!!")

""" papkani o'chirish """
# os.rmdir("D:/projects/my_lessons/python_lessons/test_papka")



""" 
Amaliy mashg'ulot  

1) O'zingiz haqidagi malumotlarni lug'at ko'rinishida yangi faylga saqlang, va uni qaytadan o'qing.
2) Yuqoridagi lug'at ko'rinishidagi malumotlarni o'zgaruvchi holatida faylga saqlang va uni qaytadan o'qing.

"""


""" 
Vazifa 

1) Bugungi dars davomida ko'rib o'tgan ma'lumotlarimizni barini yangi faylga yozing, uni qaytadan o'qing.
    -endi hudi shu ishni o'zgaruvchi bilan amalga oshiring. yangi faylga yozing va qaytadan o'qing.
    -faylni ochirib tashlang.

"""

"""
Thame: Jsonlar bilan ishlash
"""

"""
JSON - JavaScript Object Notation
Dastur va server orasidagi ma'lumotlar aynan JSON ko'rinishida uzatiladi.

Dasturlarimiz davomida ma'lumotlarni JSON ko'rinishida saqlashimiz, 
    internet orqali boshqa foydalanuvchilarga, dasturlarga yoki serverga yuborishimiz, 
    JSON fayllarni Pythonda ochib, unga ishlov berishimiz va turli amallar bajarishimiz mumkin.

JSON o'zgaruvchilar, tarkibidan qat'iy nazar matn ko'rinishida saqlanadi.

JSON ma'lumotlar va fayllar bilan ishlash uchun Pythonda maxsus json moduli bor. >>> import json
Ma'lumotlarni JSON matniga o'tkazish uchun ikki funksiyadan foydalanamiz: 
    json.dumps(x) — berilgan x o'zgaruvchini JSON matniga o'zgartiradi
    json.dump(x,fayl) — berilgan x o'zgaruvchini JSON ga o'zgartirib, ko'rsatilgan faylga saqlaydi.

"""

import json

""" Pythondan > JSON ga """

# x = 10
# x_json = json.dumps(x)
# print(type(x_json))
# print(x_json)

# ism = "anvar"
# ism_json = json.dumps(ism)
# print(type(ism_json))
# print(ism_json)

# sonlar = [12, 45, 23, 67]
# sonlar_json = json.dumps(sonlar)
# print(type(sonlar_json))
# print(sonlar_json)

"""
Python-dan JSON-ga aylantirilganda, Python ob'ektlari JSON (JavaScript) ekvivalentiga aylantiriladi:

Python	JSON

dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null

"""


# inson = {
#     'ism':"Anvarjon",
#     "familiya":"Olimov",
#     "yosh":23,
#     "kasb":"Dasturchi",
#     "oila_azolari":{
#                 'ota':"Abdulla Ahatov",
#                 "ona":"Nigora Ahatova",
#                 "uka":"Nodirjon Olimov"
#             },
#     "oilali" : False,
#     'dostlar':['Abdulaziz', "Toxir", "Ravshan", "Aziz"]    
# }

# inson_json = json.dumps(inson) # indent = 4 -> ma'umotlarni saqlashda chapdan qancha joy tashlashni ko'rsatadi.
# print(inson_json)
# print(type(inson_json))

""" Ma'lumotni faylga yozish """
# with open('D:/projects/my_lessons/python_lessons/test.json','w') as i:
#     json.dump(inson,i)


""" JSON dan Pythoga """

""""
JSON formatidagi ma'lumotlarni Pythondagi ma'lumot turiga keltirish uchun json.loads() yoki 
    json.load() funksiyalaridan foydalanamiz. Yuqoridagi ka'bi, json.loads() funksiyasi 
    to'g'ridan-to'g'ri JSON matn bilan ishlasa, json.load() funksiyasi JSON fayllarni o'qish uchun ishlatiladi.

json.loads() - Bu funksiya parametr sifatida JSON matn qabul qiladi va Python o'zgaruvchiga o'tkazadi.
json.load() - Bu funksiya JSON fayllarning tarkibini Pythonga yuklab olish uchun ishlatiladi. 


"""

""" loads() - matn uchun"""
# print(inson_json)
# inson_json_opened = json.loads(inson_json)
# print(inson_json_opened)

""" load() - fayl uchun """
# with open('D:/projects/my_lessons/python_lessons/test.json') as f:
#     inson_py = json.load(f)
# print(inson_py)

""" Amaliy mashg'ulot """
"""
    https://psihologictest7.pythonanywhere.com/api/subcategory/
    Apini ochib ishlatib ko'rish
"""


"""
Vazifa:
1)  Quidagi maqolalar ro'yhatini "maqolalar" nomli faylga json ko'rinishda saqlang va qaydadan chaqirib uni python kodi 
    ko'rinishida o'qing.

    maqolalar = [
        {
            "id": 1,
            "title": "Фикрлаш ва унинг бузилиши",
            "body": "Фикрлаш — индивиднинг билиш фаолиятидаги муҳим жа- раён бўлиб, атрофдаги борлиқнинг инсон онгида акс этишининг олий шакли ҳисобланади. Ҳис қилиш, тасаввур, идрок қилиш, билиш жараёнининг бошланғич босқичидир. Предметларнинг хоссалари ҳақидаги билимларни умумлаштириш тушунчаси фикрлашнинг асоси ҳисобланади.\r\n\r\nФикрлаш жараёни анализ (таҳлил) ва синтез, таққослаш, солиштириш, кўз ўнгига келтириш ва аниқлаштириш, умум- лаштириш, кейин эса тушунчанинг шаклланишига ўтиш босқичларидан ташкил топган. Фикрлашнинг моддий асоси — сўз ҳисобланади. Ҳар бир сўз маълум бир тушунчани бил- диради: масалан, аниқ (стол) ёки хаёлий (босқич). Фикрлаш субстратининг ёпиқ ёки хаёлий тушунчалар билан мос келиши қуйидагича фарқланади, яъни аниқ — тасвирий фикрлаш, хаё- лан — мантиқан фикрлаш. Охирги хусусият нутқи ривожлан- ган, мураккаб тушунчани умумлаштира оладиган катта ёшдаги одамларга хосдир.\r\n\r\nФикрлашнинг таркибий хусусиятларидан бири — бу ассо- циатив фаолиятдир.",
        },
        {
            "id": 2,
            "title": "Аутист – бахтсиз эмас",
            "body": "«Мен аутистман… Мен чарчадим… Мени тушунишмаганликларидан, ҳадеб тўғрилайверишларидан, жазолайверишларидан, танқид қилаверишларидан, ўзларига ўхшатиш учун дарс ўтаверишларидан… Ҳамма-ҳаммасидан чарчадим…\r\nҲа, мен аутистман! Ҳа, мен бошқачаман! Аммо тушунинглар, мен ёмон эмасман… мени тушунмасликларидан чарчадим… Мени боримча қабул қилмасликларидан чарчадим. Мендан «нормал» бўлишни кутишларидан чарчадим. Мен “нормал” эмасман! Тушунсанглар-чи! Мен аутистман. Мен бошқачаман. Ҳамманинг ўз тарозиси бор. Аммо аутистнинг дунёни қабул қилиш тарозиси бошқача. Ёмонмас! Яхшимас! Бошқача, тушуняпсизларми? Ҳамма нарсанинг ўлчов бирлиги бор: килограмм, метр, дақиқа. Аутистнинг ўлчов бирлиги ўзига хос, яна бир марта айтаман, ёмонмас, яхшимас, ўзига хос. Ўзингизга ўхшатишдан, аутистлар сизгни ўзига ўхшатишларини бас қилинг. Ёмон кўрманг, йиғламанг, бахтсиз деманг.\r\n\r\nАутист бахтсиз эмас!\r\nАутист болалар бирам ажойибки, олдингизда туриб сизни кўрмаслиги мумкин. ",
        },
        {
            "id": 6,
            "title": "Онг бузилиши синдромлари",
            "body": "Онгнинг бузилиши (хиралашуви) да беморда нафақат атроф реал дунё интиқосининг бузилиши, юз беради, балки ички боғлар (абстракт билиш) ҳамда ташқи (сезги ҳиссиёти) бевоси- та предмет ва ҳодисаларни акс эттириши ҳам бузилади. Онг- нинг бузилиш белгисига кўра беморнинг ўз шахсига нисбатан мўлжали ҳам бузилади, у ташқи дунёга аланглайди, вазиятни (вақт, жойини) баҳолай олмайди, борлиқ дунёдан юз ўгиради, атрофдагиларни қабул қила-олмайди, тафаккури ноаниқ ва тарқоқ онгнинг қисман ёки тўлиқсиз хиралашув даври ҳақида тўлиқ эслолмайди.\r\n\r\nОнг бузилишининг бошланишида қўйидаги синдромлар фарқланади. Онгнинг карахт бўлиш ҳолатининг уч даражаси фарқланади. Қисқа вақт давом этувчи онгнинг карахтлиги обнубуляция (юнонча пиЬ15 — булут) дейилади. Бунда ташқи таъсиротни қабул қилиш бир оз қийинлашади, онг худди булут ёки тутун билан ўралгандек бўлиб туради.\r\n\r\nКарахтлик — онгнинг сезиларли даражада бузилиши ташқи таъсиротларни қабул қилиш чегараси қисқаради. ",
        }
    ]

2)  Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: 
    talaba_json = \"""{"ism":"Hasan","familiya":"Husanov","tyil":2000}\"""  # ❗❗❗  \ - belgisini o'chirib tashlang ❗❗❗

3) 2-mashqadagi o'zgaruvchini yangi sjon fayliga saqlang va qaytadan uni o'qib yana konsulga chiqaring.

"""









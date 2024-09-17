"""
Thame: Lug'atlar(Dictionary) va Ro'yhatlar(List) bilan ishlash
"""

""" Lug'at ichida lug'at """

# insonlar = {
#     "inson_1" : {
#         "ism":"ALi",
#         "familya":'Valiyev',
#         "t_yil":2000,
#         "kasbi":{
# 			'kasb1':"talaba",
# 			"kasb2":"dasturchi"
# 		}   
#     },
    
#     "inson_2" : {
#         "ism":"Nodir",
#         "familya":"Jo'rayev",
#         "t_yil":"1989",
#         "kasbi":"Haydovchi"    
#     },
    
#     "inson_3" : {
#         "ism":"Hasan",
#         "familya":'Husanov',
#         "t_yil":1991,
#         "kasbi":"shifokor"    
#     }
# }

# print(insonlar['inson_1']['kasbi']['kasb1'])
# print(insonlar['inson_1']['kasbi'])

# print(f"Salom bu inson {insonlar['inson_2']['ism']} \
# {insonlar['inson_2']['familya']} \
# kasbi {insonlar['inson_2']['kasbi']}")


""" Lug'at ichida ro'yhat """

# qizlar = {
#     "anora":['atirgul','lola'],
#     "ezoza":['binafsha','moychechak'],
#     "dilshoda":['nastarin','chinnigul'],
#     "nigina":['kaktus','atirgul']    
# }

# print(qizlar['anora'][0])
# print(qizlar['dilshoda'][1])
# print(qizlar['ezoza'][0])

# for ism, gullar in qizlar.items():
#     print(f"\n{ism.title()} quyidagi gullarni yoqtiradi: ", end=' ')
#     for gul in gullar:
#         print(f"{gul.title()}", end=' ')
    

""" ro'yhat ichida lug'at """

# talaba_1 = {
#  	'ism':"Jasurbek",
#  	'familya':"Ibrohimov",
#  	'guruh':"4-KB_20",
#  	'fan':"Iqtisod",
# }

# talaba_2 = {
#  	'ism':"Azamhon",
#  	'familya':"Burxonxo'jayev",
#  	'guruh':"4-KB_20",
#  	'fan':" Makroiqtisodiyot",
# }
# talabalar = [talaba_1, talaba_2]

# print(talabalar[0]['fan'])

# for talaba in talabalar:
# 	for key, value in talaba.items():
# 		print(f"{key} - {value}")
    

""" ro'yhat ichida ro'yhat """

# guruh_1 = ['azimjon','ilxomjon','behruzbek']
# guruh_2 = ['anora','umarbek']

# guruhlar = [guruh_1, guruh_2]

# print(guruhlar[0][2])
# print(guruhlar[1][1])



""" -------- Vazifa --------

1)  Ro'yhat ichida  ro'yhat
Telefonlar yoki koputerlar kompanialari va ularnig modellari ni ro'yhat ichiuda ro'yhat 
ko'rinishida jamlab ularni honsolga chiqaring

Misol:
lg = ['X5','Q7','X Power 1']
sumsung = ['S7',"A50"]
telefonlar = [lg, sumsung]
print(.....)

2)
<> lug'at ichida lug'at
Oilalar degan lu'gat yarating uning kalitlarilari o'rnida olila bo'sin, 
va o'sha oila kaliti o'rnida oilanging azosi bo'lsin va uning ichidagi lug'atda  
oila azosining malulotlari chiqib tursin

Misol:

oilalar = {
	'oila1':{
		'ota':{
			'ism':"Alijon",
            'familya':"Mamajonov",
            'yosh':'32',
            'kasb':"Duradgor",
		},
		'ona':{
			'ism':'Munisa',
            'familya':"Mamajonova",
            'yosh':'30',
            'kasb':"Tikuvchi",
		},
	'oila2':{
		...
	}
	}
}

print("For va if larni ishlatib barcha oila va uning zaolari haqida malumotlarni
chiroyli qilib chiqaring ")


3) Lug'at ichida ro'yhat
3 ta ko'chadagi do'stingizdan, 3 ta sinfdoshingizdan va 3 ta kursdagi o'rtog'ingiz 
haqidagi malumotlarni lugatga quyidagi kabi joylang va ichida ro'yhat ochib unga sevimli taomlarini kiritsin

Misol:
dostalar = {
	'sinfdoshlar':{
		'ali':['hotdog','osh','norin'],
        'anvar':['gamburger','lavash','chizburger'],
        'olim':['kabob','somsa','norin']
	},
	"dostlar":{
		'abbos':['qazi','somsa','norin']
	},
	...	
}
For va if larni ishlatib barcha dostlaringiz va ularning taomlari haqidagi malumotlarni
chiroyli qilib chiqaring


4) ro'yhat ichida lug'at

car_1 = {
 	'model':"S3",
 	'brend':"BMW",
 	'year':"2021",
 	'price':"23000",
}

car_2 = {
 	'model':"Nexia-3",
 	'brend':"Chevrolet",
 	'year':"2016",
 	'price':"16000",
}
cars = [car_1, car_2, ...]

"""
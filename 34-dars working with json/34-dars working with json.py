import json

# 1st step 

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000} #Python formatida bu o'zgaruvchining tipi <dict>
# print(type(data)) 

# data_json = json.dumps(data) #json formatida bu o'zgaruvchining tipi <str>
# print(data_json)
# print(type(data_json))


# 2nd step

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" # Bu o'zgaruvchi <str> tipida turibdi
# print(type(talaba_json)) 
talaba = json.loads(talaba_json) # O'zgaruvchini json <str> holatidan python <dict> holatiga o'tkazildi 
# print(talaba)
# print(type(talaba))


# 3rd step

# new_file = 'data/car.json'
# with open(new_file, 'w') as f:
#     json.dump(data, f)

# new_file2 = 'data/student.json'
# with open(new_file2, 'w') as f2:
#     json.dump(talaba, f2)


# 4th step

# openfile = 'data/students.json'
# with open(openfile, 'r') as f:
#     students = json.load(f)
#     student1 = students['student'][0]
#     student2 = students['student'][1]
#     student3 = students['student'][2]

#     for i in [student1, student2, student3]:
#         print(f"{i['name']} {i['lastname']}, {i['id']} - course, student of {i['faculty']} faculty")


# 5th step

wikifile = 'data/api-result.json'
with open(wikifile, 'r') as f:
    cntnt = json.load(f)
    wikititle = cntnt['query']['pages']['13801']['title']
    wikitext = cntnt['query']['pages']['13801']['extract']
    print(f"Title: {wikititle}\nText:\n{wikitext}")    
import json
file=open('sample.json','a')

name=input('ad :')
surname=input('soyad :')

stud={
    'ad':name,
    'soyad':surname
}

convertDictToJson=json.dumps(stud)


file.write(convertDictToJson)
import json
f=open("sample.json","r")
dataFromJson=f.read()
convertJsonToDict=json.loads(dataFromJson)

for dct in convertJsonToDict:
    if dct["ad"]=="Ferid":
        convertJsonToDict.remove(dct)


print(convertJsonToDict)
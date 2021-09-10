import json
f=open('sample.json','r')

dataFromJson=f.read()

convertJsonToDict=json.loads(dataFromJson)
print(convertJsonToDict["ad"])
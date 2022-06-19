import requests
import csv
import json
def readFile(file):
    jsonArray = []
        
    with open(file, encoding='utf-8') as csvf:        
        csvReader = csv.DictReader(csvf)        
        for row in csvReader:            
            jsonArray.append(row)
    return jsonArray

    
data = readFile("transaction.txt")
res = requests.post(
    'http://localhost:5000/create', json=data)
if res.ok:
    print("success")

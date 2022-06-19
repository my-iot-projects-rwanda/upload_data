import requests
import csv
import serial
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
    print(data)
    ser = serial.Serial(
        port='COM36',  # plz change this according to your port number
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    ser.write(bytes(stringData), 'utf-8')
    ser.flush()
    print("successfully wrote to serial")


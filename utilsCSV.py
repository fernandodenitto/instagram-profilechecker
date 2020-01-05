# Utility Scripts per convertire oggetti (dict) in CSV
# Il file JSON viene passato come primo argomento mentre il file CSV da creare come secondo

import os
import sys
import json
import csv

fileJSON=sys.argv[1]
fileCSV=sys.argv[2]

dataJson=open(fileJSON,'r')

csvFile=open(fileCSV,'w')

listaJSON=json.loads(dataJson.read())

csvwriter = csv.writer(csvFile)

count = 0

for elem in listaJSON:
    for uselem in elem:
        if count == 0:
            header=elem.keys()
            print(elem.keys())
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(elem.values())

csvFile.close()
        


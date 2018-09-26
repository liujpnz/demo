import csv, json


csvFilePath = "transactions.csv"
jsonFilePath = "transactions.json"

#read csv and add data to dictionary
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        id = csvRow["txnid"]
        data[id] = csvRow


#write data to JSON file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))


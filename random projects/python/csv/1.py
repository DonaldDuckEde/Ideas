import csv

file = "info.csv"

with open(file, mode='r') as csv_file:
    totalSum = ""
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    
    for row in csv_reader:
        num1 = row[0]
        num2 = row[1]
        answer = row[2]
        
        totalSum = (num1, "X",  num2, "=", answer)
    
    print(totalSum)   
        
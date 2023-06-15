import csv   # comma seperated value

with open ('moshteri.csv','r') as file:
    csv_reader = csv.reader(file) # etlaat dakhel file csv mikhane va mireze dakhel variable
    for line in csv_reader:
        if 'name' not in line:
            print(f"name:{line[1]}--> city:{line[3]}")
import csv
with open('class.csv','r',encoding='utf-8',newline='') as file:
    # csv_writer = csv.writer(file)
    # csv_writer.writerow(['طه','نعمتی',15])
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(line)
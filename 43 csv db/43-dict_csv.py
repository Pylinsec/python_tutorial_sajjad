import csv

data = [{'name':'sajjad','lname':'ansaryan','age':15,'city':'jam'},
        {'name':'taha','lname':'nemati','age':15,'city':'jam'},
        {'name':'bardia','lname':'kamaei','age':14,'city':'jam'},
        {'name':'ali','lname':'bazyari','age':15,'city':'jam'}]


def write_dict():
    with open ('dict.csv','w',newline='') as file:
        # fieldnames --> list  az nam saesotoon 
        dict_writer = csv.DictWriter(file,fieldnames=('name','lname','age','city'))
        dict_writer.writeheader() # write sarsootin ya hemnan header dar line aval csv file 
        # rahelhal aval jehat write 
        # for line in data:
        #     dict_writer.writerow(line)
        # rahe hal do berye write 
        dict_writer.writerows(data)


def read_dict():
    with open('dict.csv','r') as file:
        dict_rerader = csv.DictReader(file)
        for line in dict_rerader:
          print(line['lname'])

read_dict()       
import sqlite3 , csv

#  sakhtan function beraye gerftan dadehga az database
def get_data_from_chinook():
    column_name=[]
    # connect to chinook
    db = sqlite3.connect('chinook.db')
    data = db.execute(" SELECT * FROM customers")
    # print(customer_data.fetchone()) # feghat radif aval miare
    # print(customer_data.fetchmany(size=30)) # bar asas meghdar size radif beraye ma barmigardanad

    # save information in customers 
    cusromers_data = data.fetchall()
    # add column name in culmn_name list
    for row in data.description:
        column_name.append(row[0])
    return cusromers_data , column_name    
    db.close()  



# sakhtan function beraye zakhire dadeha dar csv file 
def write_data_in_csv(customers_info , col_name):
    with open('data.csv','w',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(col_name)
        writer.writerows(customers_info)


customers_info , col_name = get_data_from_chinook()    
write_data_in_csv(customers_info , col_name)
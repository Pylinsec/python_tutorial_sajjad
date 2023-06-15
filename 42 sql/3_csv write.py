import csv

with open('moshteri.csv','a',newline='\n') as file: # neline --> jehat raften be line ba bad az write har khat 
    csv_writer = csv.writer(file )
    # writerow feghat yek satr dar qaleb list ya tuple mesl sarsootn behesh midi
    #                    id,name,Address,City,code posti,Country
    # csv_writer.writerow() # list , tuple,dict ,set , str
    csv_writer.writerow(('havij','taha','aliabad','jam',4564,'iran'))
    csv_writer.writerows([(5,'taha5','aliabad5','jam5',4564,'iran5'),(6,'taha6','aliabad6','jam6',4564,'iran6')])


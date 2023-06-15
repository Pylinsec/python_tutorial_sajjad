
import csv 

def makecsv():
    with open('file.csv','w' , newline='') as f:
        writer = csv.writer(f ,delimiter='*')
        # writer.writerow('taha nemati')
        writer.writerows(('taha','nemati','nohom'))


makecsv()        
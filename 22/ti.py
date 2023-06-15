import datetime 

# print(datetime.datetime(1999,11,10))
# current_time = datetime.datetime.now()
# print(current_time)
# print(current_time.strftime("%Y")) # format kamel sal 
# print(current_time.strftime("%y")) # format kochak shode 
# print(current_time.strftime("%m")) # mah ra be adad barmigardand 
# print(current_time.strftime("%B")) # %B --> month name 
# print(current_time.strftime("%h")) # %h --> month name hast be sooroot kholaseh 
# print(current_time.strftime("%H")) # bargardandan saat 

print(datetime.date.today())  # bargardandan tarikh  emrooz 
print(datetime.date.today().day) # rooz emrooz
print(datetime.date.today().month)  # month
print(datetime.date.today().year)# yeal ya sal 
now = datetime.datetime.now().time()# saat alan 
now = str(now)
print(now[:-7]) # feghat saat 

print(datetime.date.min) # 0001-01-01  kochaktarin sal moojood dar datetime 
print(datetime.date.max) # 9999-12-31   max sal ke mitevanad pooshesh dehad 

#  halat avval
now_date = datetime.datetime.now().date()
now_time = datetime.datetime.now().time()
my_year = datetime.datetime(9999,1,1)

print(f"date-->{now_date} , time --> {str(now_time)[:-7]}")


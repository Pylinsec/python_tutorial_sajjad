from tkinter import *
import time
ret=Tk()

# naghes ast!!!!!!!!!!!!!!!!!!!!!

barchasb= Label(ret)
barchasb.pack()

list1 =['sc2.png','sc1.png']
list2=[]
aks1 = PhotoImage(file='sc1.png')
aks2 = PhotoImage(file='sc2.png')
list2.append(aks1)
list2.append(aks2)
print(list2)
for makan in list2:
    
#     aks1 = PhotoImage(file=makan)
    barchasb.config(image=makan)
    ret.update()
    time.sleep(1)

ret.mainloop
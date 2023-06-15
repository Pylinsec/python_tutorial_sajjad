from tkinter import *


sajjad = Tk()
sajjad.geometry('500x500')#$ deqat shevad X  harf hast 
sajjad.title('sajjad')
# make widget label  --> barchasp 
# height --> ertefah   width --> pahna  fg --> rang font  bg --> background 
# font --> size matn  text --> matn label ma 
# label1 = Label(sajjad,bg='red',width=20,height=10 , text='top' , font=30) 
# label1.pack(side = 'top' ) 
# label2 = Label(sajjad,bg='red',width=20,height=10 , text='bottom' , font=30) 
# label2.pack(side = 'bottom') 
# label3 = Label(sajjad,bg='red',width=20,height=10,text='left',font=30) 
# label3.pack(side = 'left') 
# label4= Label(sajjad,bg='red',width=20,height=10,text='right' , font=30) 
# label4.pack(side = 'right') 
# label.pack(side = LEFT) --> RIGHT - TOP - BOTTOM


label4= Label(sajjad,bg='red',width=10,height=5,text='right' , font=30) 
# label4.pack(anchor=N)  # --> north --> N
# label4.pack(anchor='ne') # --> north east --> NE
# label4.pack(anchor='nw') # --> north west --> NW
# label4.pack(anchor='e') # -->east --> E
# label4.pack(anchor='w') # --> west--> W
label4.pack(anchor=SE) # --> south east --> SE
# label4.pack(anchor='sw') # --> south west --> SW
# label4.pack(anchor='s') # --> south  --> S
# label4.pack(anchor='center') # bala markaz 

sajjad.mainloop()
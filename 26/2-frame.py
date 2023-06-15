from tkinter import *

root = Tk()
root.geometry('200x200')
# tozihat
"""
Frame---> height  --> adad migiread
-width --> adad migirad
-bg --> rang zamineh 
-boder(khat dor)---> adad migirad tarjihan bin 1 ta 3
"""

frame = Frame(root,bg='red',width=100,height=50,border=3)
frame.pack()
frame1 = Frame(root,bg='blue',width=100,height=50,border=3)
frame1.pack(fill=X)

# tozihat
'''
hight--> adad migireh
width--> adad 
text--> reshteh , name migire
font--> font= adad --> size
bg--> background
fg --> foreground ya rang neveshteh 
image --> aks behesh midim 
'''
label1 = Label(frame,text='sajjad')
label1.pack()
label2= Label(frame1,text='ansaryan')
label2.pack(side='left')
label3= Label(frame1,text='kelas nohom',bg='yellow')
label3.pack(side='right')
root.mainloop()
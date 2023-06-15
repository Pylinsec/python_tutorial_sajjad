from tkinter import *
chesse = Tk()
chesse.title('chesse')
chesse.geometry('800x800')
main_frame = Frame(chesse,bd=15,bg='aqua')
main_frame.pack()
for i in range(8):
    frame = Frame(main_frame)
    frame.pack()
    if i % 2 == 0:
        colors = ['white','black']
        for j in range(8):
            lbl = Label(frame,padx=30,pady=25,bg=colors[j % 2])
            lbl.pack(side='left')
    else:
        colors = ['black','white']  
        for j in range(8):
            lbl = Label(frame ,padx=30,pady=25,bg=colors[j % 2])
            lbl.pack(side='left')   
chesse.mainloop()
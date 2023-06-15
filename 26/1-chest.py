from tkinter import *

window = Tk()
window.geometry('800x800')
window.config(border=3,background='yellow')
window.title('chese')

# make frames 
f1 = Frame(window,bg='white')
f1.pack()
f2 = Frame(window,bg='white')
f2.pack()
f3 = Frame(window,bg='white')
f3.pack()
f4 = Frame(window,bg='white')
f4.pack()
f5 = Frame(window,bg='white')
f5.pack()
f6 = Frame(window,bg='white')
f6.pack()
f7 = Frame(window,bg='white')
f7.pack()
# make label for f1 frame
f8 = Frame(window)
f8.pack()


# make label for f1 frame
colors1 = ['black','white']
colors2 = ['white','black']
# line1
for f in range(8):
    label1 = Label(f1,height=6,width=12,bg=colors1[f % 2 ==0])
    label1.pack(pady=10,padx=10,side='left',anchor='nw')
# line 2
for f in range(8):
    label1 = Label(f2,height=6,width=12,bg=colors2[f % 2 ==0])
    label1.pack(pady=10,padx=10,side='left',anchor='nw')
# line3
for f in range(8):
    label1 = Label(f3,height=6,width=12,bg=colors1[f % 2 ==0])
    label1.pack(pady=10,padx=10,side='left',anchor='nw')
# line 4
for f in range(8):
    label1 = Label(f4,height=6,width=12,bg=colors2[f % 2 ==0])
    label1.pack(pady=10,padx=10,side='left',anchor='nw')
# line5
for f in range(8):
    label1 = Label(f5,height=6,width=12,bg=colors1[f % 2 ==0])
    label1.pack(pady=10,padx=10,side='left',anchor='nw')
# line6
for f in range(8):
    label1 = Label(f6,height=6,width=12,bg=colors2[f % 2 ==0])
    label1.pack(pady=10,padx=10,side='left',anchor='nw')
# line7
for f in range(8):
    label1 = Label(f7,height=6,width=12,bg=colors1[f % 2 ==0])
    label1.pack(pady=10,padx=10,side='left',anchor='nw')
# line8
for f in range(8):
    label1 = Label(f8,height=6,width=12,bg=colors2[f % 2 ==0])
    label1.pack(pady=10,padx=10,side='left',anchor='nw')




window.mainloop()
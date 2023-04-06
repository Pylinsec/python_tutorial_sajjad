# hi sajjad how are you>

from tkinter import *
from tkinter import PhotoImage

win = Tk()
win.geometry('600x800')
win.title('Text')

# make text widget
# text = Text(win,width=500,height=400,font=('ds-digital',50))
#  state --> normal , disabled
img = PhotoImage(file='11.png')
text = Text(win,width=50,font=15,state=NORMAL,wrap=None)
# wrap --> char --> dar line harche zarfiat char bood mizare , agar 'word' bood bar asas zarfiat kelem poor mikone 
text.image_create(END,image = img) # image_create (position,image=img)
# for i in range(20):
#     # text.insert('N.M','matn') #  N shomreh line hast ke az adad 1 shoroo mishe , 
#     text.insert('1.0',i)
#      #  N shomreh line hast ke az adad 1 shoroo mishe , 
#     # m shomereh character hast ke az adad 0 shroo misheh 
# text.insert('1.10','sajjad')
matn = 'Furthermore, text widgets can be used to display links, images, and HTML, even using CSS styles'
text.insert('1.0',matn)
text.pack()
print(text.get('1.0','1.12')) # text.get(start='m.n' , end= 'm.n')

win.mainloop()
from tkinter import *


# wor = Tk()
# wor.geometry('620x660')
# wor.title('chess')
# wor.config(bg='white')

# color1=['lightblue','darkblue']

# for item1 in range(8):

#     if item1 % 2 == 1 :
#             color1=['darkblue','lightblue']

#     if item1 % 2 == 0 :
#         color1=['lightblue','darkblue']

#     for item2 in range(8):

#         barchasb = Label( wor , width=10 , height=5 , bg=color1[item2 % 2 ==0] )
#         barchasb.grid( row=item1  , column=item2 )

# wor.mainloop()

# --------------------------------------------------

man= Tk()

man.geometry('580x620')
man.title('login page')
man.config(bg='white')

barchasb = Label( man , width=30 , height=5, font=('times',15) , bg='white' , text='welcome to login page 🥳')
barchasb.grid( row=0 , column=0 , columnspan=3 )

neveshte1 = Entry( man , width=40 , font=5 , bg='lightblue')

neveshte1.grid( row=1 , column=2 , ipady=10)

barchasb1 = Label( man , width=10 , height=5, font=('times',15) , bg='white' , text='username😊:')
barchasb1.grid( row=1 , column=0 )

neveshte2 = Entry( man , width=40 , font=5 , bg='lightblue')

neveshte2.grid( row=2 , column=2 , ipady=10)

barchasb2 = Label( man , width=10 , height=5, font=('times',15) , bg='white' , text='email:')
barchasb2.grid( row=2 , column=0 )

neveshte3 = Entry( man , show=('*') , width=40 , font=5 , bg='lightblue')

neveshte3.grid( row=3 , column=2 , ipady=10)

barchasb2 = Label( man , width=10 , height=5, font=('times',15) , bg='white' , text='pasword:')
barchasb2.grid( row=3 , column=0 )

dokme = Button( man , width=8 , height=2 , bg='orange' , text='done' , font=('times',15) )
dokme.grid( row=4 , columnspan=3 )

barchasb3 = Label( man , width=50 , height=5, font=('times',15) , bg='white' , text='')
barchasb3.grid( row=5 , columnspan=3 )

t1 = Toplevel(man)


def done_gig():

    if neveshte2.get() == '' and neveshte1.get() == '' and neveshte3.get() == '':
        barchasb.config(taxt='yeky az entry ha khali ast lotfan dobar check konid')

    else:
        barchasb.config(taxt='shoma sabtenam shodid')

dokme.config(command=lambda:done_gig)






man.mainloop()
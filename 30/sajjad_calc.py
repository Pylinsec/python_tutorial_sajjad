from tkinter import *

wet= Tk()

wet.geometry('460x400')
wet.title('calculator')


ghab1 = Frame( wet , width = 300 , height = 400 , bg = 'gray' )
ghab1.grid( padx=10 , pady=10 )
ghab2 = Frame( ghab1 , width = 290 , height = 390 , bg = 'black' )
ghab2.grid( padx=10 , pady=10 )
ghab3 = Frame( ghab2 , width = 15 , height = 10 , bg = 'gray' , border= 3 )
ghab3.grid( pady=15 , ipady=2 , row=0 , column=0 , columnspan=4 , padx=14 )
neveshte1 = Entry( ghab3 , width = 46 , bg = 'white' , font = ('times' , 12))
neveshte1.grid(row=0 , column=0 , columnspan=4 )
 
dokme1 = Button( ghab2 , text='Clear (CE)' , width = 24, height = 2 , bg = 'gray' )

dokme1.grid( row=1 , column=0 , columnspan=2 , padx = 30)

dokme2 = Button( ghab2 , text='/' , width = 9 , height = 2 , bg = 'gray' )

dokme2.grid( row=1 , column=2 , pady=1  )

dokme3 = Button( ghab2 , text='X' , width = 9 , height = 2 , bg = 'gray' )
 
dokme3.grid( row=1 , column=3 , pady=1 , padx=24 )


dokme4 = Button( ghab2 , text='7' , width = 9 , height = 2 , bg = 'gray' )

dokme4.grid( row=2 , column=0 , padx=10)

dokme5 = Button( ghab2 , text='8' , width = 9 , height = 2 , bg = 'gray' )

dokme5.grid( row=2 , column=1 , padx=10)

dokme6 = Button( ghab2 , text='9' , width = 9 , height = 2 , bg = 'gray' )

dokme6.grid( row=2 , column=2 , pady=14  )

dokme7 = Button( ghab2 , text='-' , width = 9 , height = 2 , bg = 'gray' )

dokme7.grid( row=2 , column=3 , pady=15  )
 

dokme8 = Button( ghab2 , text='4' , width = 9 , height = 2 , bg = 'gray' )

dokme8.grid( row=3 , column=0 , padx=10)

dokme9 = Button( ghab2 , text='5' , width = 9 , height = 2 , bg = 'gray' )

dokme9.grid( row=3 , column=1 , padx=10)

dokme10 = Button( ghab2 , text='6' , width = 9 , height = 2 , bg = 'gray' )

dokme10.grid( row=3 , column=2 , pady=10  )

dokme11 = Button( ghab2 , text='+' , width = 9 , height = 2 , bg = 'gray' )

dokme11.grid( row=3 , column=3 , pady=10 )


dokme12 = Button( ghab2 , text='1' , width = 9 , height = 2 , bg = 'gray' )

dokme12.grid( row=4 , column=0 , padx=10 )

dokme13 = Button( ghab2 , text='2' , width = 9 , height = 2 , bg = 'gray' )

dokme13.grid( row=4 , column=1 , padx=10 )

dokme14 = Button( ghab2 , text='3' , width = 9 , height = 2 , bg = 'gray' )

dokme14.grid( row=4 , column=2 , pady=10  )

dokme15 = Button( ghab2 , text='=' , width = 9 , height = 6 , bg = 'gray' )

dokme15.grid( row=4 , column=3 , pady=10 , rowspan=2 )

dokme16 = Button( ghab2 , text='0' , width = 25 , height = 2 , bg = 'gray' )

dokme16.grid( row=5 , column=0 , pady=10 , columnspan=2 )

dokme17 = Button( ghab2 , text='.' , width = 9 , height = 2 , bg = 'gray' )

dokme17.grid( row=5 , column=2 , pady=10  )

wet.mainloop()

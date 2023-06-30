from tkinter import *

win = Tk()
win.geometry('850x650')
main_frame = Frame(win,width=800,height=600,bg='white',bd=10,relief=GROOVE)
main_frame.pack()
# frame_right
frame_right = Frame(main_frame,width=300,height=600,bd=10,bg='lightblue',relief=GROOVE)
frame_right.pack(side=RIGHT)
# frame_right_subframe
frame_right_1 = Frame(frame_right,width=300,height=150,bd=10,bg='aqua',relief=GROOVE)
frame_right_1.pack()
frame_right_2 = Frame(frame_right,width=300,height=150,bd=10,bg='aqua',relief=GROOVE)
frame_right_2.pack()
frame_right_3 = Frame(frame_right,width=300,height=150,bd=10,bg='aqua',relief=GROOVE)
frame_right_3.pack()
frame_right_4 = Frame(frame_right,width=300,height=150,bd=10,bg='aqua',relief=GROOVE)
frame_right_4.pack()
# make button
btn1 = Button(frame_right_4,text='test button',width=10,bg='red')
btn1.pack(side=LEFT,ipady=75)
btn2 = Button(frame_right_4,text='test button',width=10,bg='red')
btn2.pack(side=LEFT,ipady=20)
# frame_left
frame_left = Frame(main_frame,width=500,height=600,bd=10,bg='lightgreen',relief=GROOVE)
frame_left.pack(side=LEFT)
# frame_top
frame_left_top = Frame(frame_left,width=500,height=400,bd=10,bg='pink',relief=GROOVE)
frame_left_top.pack(side=TOP)
# frame_buttom
frame_left_buttom = Frame(frame_left,width=500,height=200,bd=10,bg='grey',relief=GROOVE)
frame_left_buttom.pack(side=BOTTOM)
win.mainloop()
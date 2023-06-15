from tkinter import *
import time

main = Tk()
label = Label(main)
label.pack()
img1 = PhotoImage(file='pic/11.png')
img2 = PhotoImage(file='pic/22.png')

#  image_list=os.lsdir('pic')
# for i in image_list:
# label.config(image=i)
label.config(image=img1)
main.update()
time.sleep(2)
label.config(image=img2)
main.update()
main.mainloop()
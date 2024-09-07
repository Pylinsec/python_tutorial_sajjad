from genericpath import isfile
import os 
'''
print('andaze be Byte',os.path.getsize('python\\01.jpg')) # bargardand andaze file  be byte neshan mide
print('andazeh be kByte',os.path.getsize('python\\01.jpg')/1024)
'''

# os.rename('path1','path2')
# os.rename('python\\01.jpg','..\\qloli.jpg') # rename --> kar avval rename  kar dovvom move


#os.path.isfile()  os.path.isdir()
print(os.path.isfile('python\\01.jpg'))  # agar file bood True bargardand 
print(os.path.isdir('python\\01.jpg'))  # agar folder bood True barmigardand
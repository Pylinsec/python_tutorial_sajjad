import os 

'''
# listdir('path') -->listi az folder va file haye dakhel oon mesir misazad 
list_folder = os.listdir('python')
list_folder.sort()
print(list_folder)
for item in list_folder:
    print(item)

'''

# *********************************************
'''
# os.path.join("a","b","c")  sakht path az a, b ,c --> a/b/c  or a\b\c
new = os.path.join("sajjad","ansaryan","5","qoli") 
print(new)

# os.path.exsits('path')  # agar masir voojood dasht True bargardan  nebood false barmigardanad
print(os.path.exists('python\\apple')) 
print(os.path.exists('python\\apple1')) 
'''

#**************************************
# os.getcwd()  current working directory :--> folderi ke alan dakhelesh hasti 
print(os.getcwd())
# os.chdir('H:\\python class')  # chdir('path') --> change directory 
# print(os.getcwd())
newpath = os.getcwd()
print('basename',os.path.basename(newpath))  # basename esharh be akarin file ya folder 
print('dirname',os.path.dirname(newpath))  # dirname eshareh be path darad ta file asli 
path_tuple = os.path.split('/a/b/c/d/e')
print('dirname',path_tuple[0]) # dirname barmigardanad 
print('basename',path_tuple[1]) # basename barmigardanad 






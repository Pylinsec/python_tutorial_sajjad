import shutil
import os
print('\\')
def make_file():
    with open('sajjad.txt','w') as f:
        f.write("sajjad ansaryan\t")

# make_file()

def make_copy(source_path , destination_path):
    # os.mkdir(source_path)
    shutil.copyfile(source_path,destination_path)
    
make_copy("sajjad","H:")
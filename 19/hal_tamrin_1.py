import os 

def make_folder(name):
    for i in range(5):
        os.mkdir(f"sajjad/{name}_{i}")

def make_file(name):
    for i in range(10):
        with open(f"sajjad/{name}_{i}.txt","a") as f:
            pass

def list_chiz():
    list_file = os.listdir("sajjad")
    for item in list_file:
        item_path = f"sajjad/{item}"
        os.rename(item_path, f"sajjad/havij {item} golabi")

# make_folder('golabi')
# make_file('qoli')
list_chiz()
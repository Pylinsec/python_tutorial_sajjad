#  mode r read file  , mode w -> har dafe khrab mikard dobare az aval  , mode a --> adame avali minevaesh
with open("sajjad.txt","a") as file:
    # s = file.writable() --> moshakhas mikone ke dar mode write hast ya khair
    # print(s)
    text = '''sajjad
    ansaryan
    15'''
    # file.write(text)
    file.writelines('taha1','nemati1')


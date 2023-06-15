# mashgh 1
with open("matn.txt","w") as matn:
    matn.writelines("""sajjad erfan ee""")
with open("matn.txt","r") as matn:
    e=matn.readlines()
    w=1
    o=0
    p=[]
    for a in e:
        for r in a:
            if r==" ":
                o+=1
        if "\n" in a:
             w+=1
    for i in e:
        if "e" in i:
            y=i.replace("e","E")
            p.append(y)
        else:
            p.append(i)
    for u in p:
        with open("matn.txt","w") as matn:    
            matn.writelines(u)
    
print(f"tedad khat ha = {w}\n")
print(f"tedad space ha = {o}\n")
print(f"tedade kalamat = {o+1}\n")
print(p)
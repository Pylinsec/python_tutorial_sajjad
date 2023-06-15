#  yadavari make file 

# . --> yani haminja  .. yani khane baba  ../.. boro khane baba bozorg 
# path dar windows  ba \\ hast : mesal H:\\home\\sajad\\file.txt
# dar linux ba / joda mishan  : mesal H:/home/sajad/file.txt
for i in range(10):
    with open (f'golabi\\{i}','w') as f:
        f.write('sajjad ansaryan')


#  arbitrary(دلخواه) *args  --> daryaft arguman ha ba tedad namaloom  ya be tedad delkhah

def family(*kids):
    print(kids)
    print(type(kids)) # tuple hast  
    for i in kids:
        print(i)

# family('golabi','qoli','reza','havij','levashak')

#  keyword argument  **kwargs  ersal dicttionary ba item ha ye delkhah 
def food(**miveh):
    print(type(miveh))
    print(miveh)

food(name='lemon',taste='salty' , age= 14) #  deqat shevad ke ersal kardan be soorat dict nist  
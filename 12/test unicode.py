str = 'سجاد انصاريان '
a = str.encode()  # tabdil string farsi be binary ya heman 0,1 
print(type(a))
print(a.decode()) # tabdil binary be string
print(b'\xd8\xb3\xd8\xac\xd8\xa7\xd8\xaf \xd8\xa7\xd9\x86\xd8\xb5\xd8\xa7\xd8\xb1\xd9\x8a\xd8\xa7\xd9\x86 '.decode())
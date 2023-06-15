cinama_bahman = False
theatr_shar = True
borj_milad = False
maney = True
ticket_price = 2000
sajad_money = 5000
a = cinama_bahman or theatr_shar or borj_milad
day_off = "sunday"
c = sajad_money > ticket_price
a = c and a 
d = day_off =="friday" and a

print("sajad mitavand be cinema berevad:" , d)

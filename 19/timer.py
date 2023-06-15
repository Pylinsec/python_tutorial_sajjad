import time

def timer(second):
    time.sleep(0.05)
    min = second // 60
    sec = second % 60
    if min <10:
        min = f"0{min}"
    if sec >= 10:
        print(f"{min}:{sec}",end="\r")
    else:
        print(f"{min}:0{sec}",end="\r")

    new_second = second -1
    if new_second >= 0:
        timer(new_second)
    else:
        print("00:00")    
 

timer(100)    
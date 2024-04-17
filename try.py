import time as t
data=input("enter the length of time")
def countdown(data):
    while data:
        mins,secs=divmod(data,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        t.sleep(1)
        data=data-1
        print("tik tik",data)

countdown(int(data))
from tkinter import*
import datetime
from tkinter.messagebox import*
from tkinter.ttk import*
import winsound
body=Tk()
body.title("my personal alarm clock")
body.config(bg="grey")
body.geometry("250x250")

def alarm():
    if a1.get()=="AM":
      x=int(b1.get())
      y=int(b2.get())
    if a1.get()=="PM":
        x=int(b1.get())+12
        y=int(b2.get())
    showinfo("notification","alarm has been set")
    while True:
        if x==datetime.datetimenow().hour and y== datetime.datetimenow().minute:
           for j in range(0,100):
               winsound.Beep(1000,100)   
               break

label1=Label(body,text="hours") 
label2=Label(body,text="minutes:")    
label1.place(relx=0.1,rely=0.1)
label2.place(relx=0.5,rely=0.1)   
b1=Entry(body)  
b2=Entry(body)
b1.place(relx=0.2,rely=0.1)
b2.place(relx=0.6,rely=0.1)
c1=Button(body,text="set alarm",command=alarm)
c1.place(relx=0.4,rely=0.5)
a1=Combobox(body,values=("AM,""PM"))
a1.place(relx=0.42,rely=0.3)
label3=Label(body,text="AM OR PM")
label3.place(relx=0.35,rely=0.3)
mainloop()
import random
from tkinter import StringVar,Label,Tk,Entry

Window=Tk()
Window.geometry("400x100")
Window.title("guessing hall simulator")
Window.resizable(0,0)

same_choice=StringVar()
switched_choice=StringVar()
same_choice.set(0)
switched_choice.set(0)
no_sample=Entry()
Label(text="same choice").place(x=80,y=8)
Label(text="switched choice").place(x=80,y=40)
Label(textvariable=same_choice,font=(15)).place(x=180,y=8)
Label(textvariable=switched_choice,font=(15)).place(x=100,y=70)
no_sample.place(x=100,y=70)

def simulator(event):
    same_choice_result=0
    switched_choice_result=0
    samples=int(no_sample.get())
    doors=["GOLD","silver CAR","bhaa BHEDA"]
    for _ in range(samples):
        simulated_doors=doors.copy()
        random.shuffle(simulated_doors)
        first_choice=random.choice(simulated_doors)
        simulated_doors.remove(first_choice)
        openes_doors=(
            simulated_doors[0]if simulated_doors[0]!="GOLD" else simulated_doors[1]
        )
        simulated_doors.remove(openes_doors)
        switched_second_choice=simulated_doors[0]
        if first_choice=="GOLD":
            same_choice_result+=1
            same_choice.set(same_choice_result)
        elif switched_second_choice=="GOLD":
            switched_second_choice+=1
            switched_choice.set(switched_choice_result)
        else:
            print("in your dream baby")

no_sample.bind("<Return>",simulator)




Window.mainloop()


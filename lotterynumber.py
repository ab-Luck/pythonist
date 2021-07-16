
from tkinter import *
import random
import time
import datetime

#======================================
def lottery1():
    a=random.randint(1,49)
    b=random.randint(1,49)
    c=random.randint(1,49)
    d=random.randint(1,49)
    e=random.randint(1,49)
    f=random.randint(1,49)
    n1.set(a)
    n2.set(b)
    n3.set(c)
    n4.set(d)
    n5.set(e)
    n6.set(f)
    return
lottery=Tk()
lottery.geometry('800x400')
frame=Frame(lottery)
frame.pack()
lottery.title("lottery number generator")

#================variable==============
n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
n5=StringVar()
n6=StringVar()
time1=StringVar()
date1=StringVar()
time1.set(time.strftime("%H:%M:%S"))
#===============frame=================
var=StringVar()
var.set('lottery numbers generator')
frame1=Frame(lottery)
frame1.pack(side=TOP)
lbl=Label(frame1,textvariable=var,bg='powder blue',font=('arial',50),width=24)
lbl.pack(side=TOP)
lbl=Label(frame1,textvariable="",width=24)
lbl.pack(side=TOP)
lbl=Label(frame1,textvariable="",width=24)
lbl.pack(side=TOP)
lbl=Label(frame1,textvariable="",width=24)
lbl.pack(side=TOP)


frame2=Frame(lottery)
frame2.pack(side=TOP)
txtdisplay=Entry(frame2,textvariable=n1, font=('arial',30),insertwidth=1,bd=20,justify='center',width=4)
txtdisplay.pack(side=LEFT)
txtdisplay=Entry(frame2,textvariable=n2, font=('arial',30),insertwidth=1,bd=20,justify='center',width=4)
txtdisplay.pack(side=LEFT)
txtdisplay=Entry(frame2,textvariable=n3, font=('arial',30),insertwidth=1,bd=20,justify='center',width=4)
txtdisplay.pack(side=LEFT)
txtdisplay=Entry(frame2,textvariable=n4, font=('arial',30),insertwidth=1,bd=20,justify='center',width=4)
txtdisplay.pack(side=LEFT)
txtdisplay=Entry(frame2,textvariable=n5, font=('arial',30),insertwidth=1,bd=20,justify='center',width=4)
txtdisplay.pack(side=LEFT)
txtdisplay=Entry(frame2,textvariable=n6, font=('arial',30),insertwidth=1,bd=20,justify='center',width=4)
txtdisplay.pack(side=LEFT)

frame3=Frame(lottery)
frame3.pack(side=TOP)
btn=Button(frame3,state=DISABLED,text="")
btn.pack(side=TOP)
btn=Button(frame3,command=lottery1,padx=8,pady=8,bd=8,font=('arial',26),text="lottery number generator",bg='powder blue')
btn.pack(side=TOP)
frame4=Frame(lottery)
frame4.pack(side=TOP)
lbltime=Label(frame4,textvariable=time1,font=('arial',22),bd=8,bg='cyan')
lbltime.pack(side=LEFT)

lottery.mainloop()
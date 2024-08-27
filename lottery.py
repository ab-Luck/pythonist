
from tkinter import *
import random
import time
import datetime

#======================================
def lottery1():
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,10)
    d=random.randint(1,10)
    e=random.randint(1,10)
    f=random.randint(1,10)
    
    
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
lottery.title("Lottery Number Generator")

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
date1.set(datetime.datetime.now())
#===============frame=================
var=StringVar()
var.set('Lottery Numbers Generator')
frame1=Frame(lottery)
frame1.pack(side=TOP)
lbl=Label(frame1,textvariable=var,bg='#808080',font=('arial',50),width=24)
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
btn=Button(frame3,command=lottery1,padx=8,pady=8,bd=8,font=('arial',26),text="Click Here" ,bg='powder blue')
btn.pack(side=TOP)
frame4=Frame(lottery)
frame4.pack(side=TOP)
lbltime=Label(frame4,textvariable=time1,text='Time: ',font=('arial',22),bd=8,bg='cyan')
lbltime.pack(side=LEFT)
frame5=Frame(lottery)
frame5.pack(side=TOP)
lbldate=Label(frame4,textvariable=date1,text='Time: ',font=('arial',22),bd=8,bg='cyan')
lbldate.pack(side=BOTTOM)


lottery.mainloop()
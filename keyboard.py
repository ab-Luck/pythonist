import tkinter as tk
from functools import partial
from tkinter import*
import tkinter 

Keyboard_App=tkinter.Tk()
Keyboard_App.title("onscreen keyboard")
Keyboard_App['bg']='powder blue'
Keyboard_App.resizable(0,0)

def select(value):
    if value==" SPACE ":
        entry.insert(tkinter.END, ' ')
    elif value=="TAB":
        entry.insert(tkinter.END, '  ')
    elif value=="SHIFT":
        entry.insert(tkinter.END, '{}')
    else:
        entry.insert(tkinter.END,value)
            

label1=Label(Keyboard_App,text="onscreen keyboard",font=('arial',30,'bold'),bg='powder blue',fg='black').grid(row=0,columnspan=40)
entry=Text(Keyboard_App,width=138,font=('arial',10,'bold'))
entry.grid(row=1,columnspan=40)

buttons=[
    '!','q','w','e','r','t','y','u','i','o','p','<-','7','8','9','-'
    ,'TAB','a','s','d','f','g','h','j','k','l','[',']','4','5','6','+'
    ,'SHIFT','z','x','c','v','b','n','m',',','.','?','SHIFT','1','2','3','/'
    ,' SPACE '
]
varRow=2
varColumn=0
for button in buttons:
    command=lambda x=button: select(x)
    if button !=" SPACE ":
        tkinter.Button(Keyboard_App,text=button,command=command,font=('arial',12,'bold'),bd=12,
                       
                       width=5,padx=3,pady=3,bg='powder blue',activebackground="#ffffff",
                       activeforeground="#000990", relief='raised').grid(row=varRow,column=varColumn)
    if button ==" SPACE ":
        tkinter.Button(Keyboard_App,text=button,command=command,font=('arial',12,'bold'),bd=12,
                       
                       padx=3,pady=3,width=118,bg='powder blue',activebackground="#ffffff",
                       activeforeground="#000990", relief='raised').grid(row=6,columnspan=16)    
    varColumn +=1
    if varColumn>15 and varRow==2:
        varColumn=0
        varRow+=1
    if varColumn>15 and varRow==3:
        varColumn=0
        varRow+=1    
        

Keyboard_App.mainloop()        
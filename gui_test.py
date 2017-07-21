
import tkinter as tk
from functools import partial as pto
from tkinter import Tk,Button,X
from tkinter.messagebox import showinfo,showwarning,showerror
WARN='warn'
CRIT='crit'
REGU='regu'
SIGN={
    'do not enter':CRIT,
    'railroad crossing':WARN,
    '55\nspeed limit':CRIT,
    'wrong way':CRIT,
    'merging traffic':WARN,
    'one way':REGU
}

critCB=lambda:showerror('Error','Error button pressed')
warnCB=lambda:showwarning('Warning','Warning button pressed')
infoCB=lambda:showinfo('Info','Info button pressed')

top=Tk()
top.title('road sign')
Button(top,text='quit',command=top.quit,bg='red',fg='white').pack()
Mybutton=pto(Button,top)
critButton=pto(Mybutton,command=critCB,bg='white',fg='red')
warnButton=pto(Mybutton,command=warnCB,bg='goldenrod1')
reguButton=pto(Mybutton,command=infoCB,bg='white')

for eachsign in SIGN:
    singtpye=SIGN[eachsign]
    cmd='%sButton(text=%r%s).pack(fill=X,expand=True)'%(singtpye,eachsign,'.upper()' if singtpye==CRIT else '.title()')
    eval(cmd)

top.mainloop()

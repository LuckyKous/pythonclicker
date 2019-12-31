#coding:utf-8
from tkinter import *
import time
bitcoin = 0
ncpu = 1
nram = 1
rboost = 0
root = Tk()
clickwindow = Tk()
clickwindow.title("Bitcoin Clicker")
clickwindow.geometry('200x200')

b = StringVar()
b.set(bitcoin)

def click():
    global bitcoin
    global rboost
    if rboost == 0:
        bitcoin += 1*nram
        b.set(bitcoin)
    else:
        bitcoin += 1*nram*2
        b.set(bitcoin)

bitl = Label(clickwindow, textvariable=b)
bitl.grid(column=0, row=0)

pupwindow = Tk()
pupwindow.title("Améliorations")
pupwindow.geometry('350x200')

c = StringVar()
r = StringVar()
d = StringVar()
c.set(ncpu)
r.set(nram)
d.set(rboost)

def cpu():
    global bitcoin
    global ncpu
    if bitcoin >= 99:
        ncpu += 0
        c.set(ncpu)
        bitcoin -= 99
        b.set(bitcoin)

def ram():
    global bitcoin
    global nram
    if bitcoin >= 99:
        nram += 0
        r.set(nram)
        bitcoin -= 99
        b.set(bitcoin)

imgBitcoin = PhotoImage(file='bitcoin.png', width=100, height=100)
button = Button(click(), image=imgBitcoin, command=click)

imgCPU = PhotoImage(file='cpu.png', width=100, height=100)
button2 = Button(pupwindow, image=imgCPU, command=cpu)

imgRAM = PhotoImage(file='cpu.png', width=100, height=100)
button3 = Button(pupwindow, image=imgCPU, command=ram)

#imgBOOST = PhotoImage(file='cpu.png', width=100, height=100)
#button4 = Button(root, image=imgCPU, command=boost)

cpul = Label(pupwindow, textvariable=c)
cpul.grid(column=1, row=0)
raml = Label(pupwindow, textvariable=r)
raml.grid(column=0, row=1)
#boostl = Label(root, textvariable=d)

#button.pack()
#bitl.pack()
#button2.pack()
#cpul.pack()
#button3.pack()
#raml.pack()
#button4.pack()
#boostl.pack()
root.mainloop()
# coding:utf-8
# PRÉREQUIS#
# ----------------------#
from tkinter import *
bitcoin = 0
ncpu = 1
nram = 1
window = Tk()
window.title("Bitcoin Clicker")
window.geometry('300x200')
b = StringVar()
c = StringVar()
r = StringVar()
b.set(bitcoin)
c.set(ncpu)
r.set(nram)
#----------------------#

#DÉFINITIONS#
#----------------------#
def click():
    global bitcoin
    bitcoin += 1*nram
    b.set(bitcoin)

def cpu():
    global bitcoin
    global ncpu
    if bitcoin >= 200:
        ncpu += 1
        c.set(ncpu)
        bitcoin -= 200
        b.set(bitcoin)

def ram():
    global bitcoin
    global nram
    if bitcoin >= 100:
        nram += 1
        r.set(nram)
        bitcoin -= 100
        b.set(bitcoin)
#----------------------#

bitl = Label(window, textvariable=b)

imgBitcoin = PhotoImage(file='bitcoin.png')
button = Button(window, image=imgBitcoin, command=click)

imgCPU = PhotoImage(file='cpu.png')
button2 = Button(window, image=imgCPU, command=cpu)

imgRAM = PhotoImage(file='ram.png', width=200, height=200)
button3 = Button(window, image=imgRAM, command=ram)

cpul = Label(window,textvariable=c)
raml = Label(window, textvariable=r)


button.grid(column=1, row=1)
bitl.grid(column=0, row=1)
button2.grid(column=1, row=2)
cpul.grid(column=0, row=2)
button3.grid(column=1, row=3)
raml.grid(column=0, row=3)
window.mainloop()

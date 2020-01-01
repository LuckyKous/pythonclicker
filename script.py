# coding:utf-8
# PRÉREQUIS#
# ----------------------#
from tkinter import *
import tkinter.font as tkFont
bitcoin = 0
ncpu = 1
nram = 1
window = Tk()
window.title("Bitcoin Clicker")
window.geometry('720x480')
window.resizable(False, False)
window.configure(bg="#bbbbbb")
b = StringVar()
c = StringVar()
r = StringVar()
b.set(bitcoin)
c.set(ncpu)
r.set(nram)
fnum = tkFont.Font(size=72)
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
buttonbtc = Button(window, image=imgBitcoin, command=click)

imgCPU = PhotoImage(file='cpu.png')
buttoncpu = Button(window, image=imgCPU, command=cpu)

imgRAM = PhotoImage(file='ram.png', width=200, height=200)
buttonram = Button(window, image=imgRAM, command=ram, bd=0, bg="#bbbbbb")

cpul = Label(window,textvariable=c, bg="#bbbbbb", fg="#333333")
raml = Label(window, textvariable=r, bg="#bbbbbb", fg="#333333", highlightcolor="red")

btctext = Label(window, text="Bitcoin", bg="#bbbbbb", fg="#333333", font="fnum")
cputext = Label(window, text="CPU", bg="#bbbbbb", fg="#333333", font="fnum")

btctext.place(x=85,y=110)
buttonbtc.place(x=10,y=140)
bitl.place(x=85,y=360)
cputext.place(x=400,y=110)
buttoncpu.pack(side="right")
cpul.pack(side="right")
buttonram.pack(side="right")
raml.pack(side="right")
window.mainloop()

# coding:utf-8
# PRÉREQUIS#
# ----------------------#
from tkinter import *
import tkinter.font as tkFont
from math import *
import time
import random
import threading
from pynput.keyboard import Listener, KeyCode
bitcoin = 0 # Nb original de BTC
ncpu = 1 # Nb original de CPU
nram = 1 # Nb original de RAM
pram = 100 # Prix original de RAM
pcpu = 200 # Prix original de CPU
window = Tk()
window.title("Bitcoin Clicker")
window.geometry('720x480')
window.resizable(False, False)
window.configure(bg="#bbbbbb")
b = StringVar() # Variable nb BTC
c = StringVar() # Variable nb CPU
r = StringVar() # Variable nb RAM
pr = StringVar()
pc = StringVar()
b.set(bitcoin)
c.set(ncpu)
r.set(nram)
pr.set(pram)
pc.set(pcpu)
fnum = tkFont.Font(size=72)
emergency_key = KeyCode(char='s')
ram_key = KeyCode(char='r')
cpu_key = KeyCode(char='c')
btc_key = KeyCode(char='b')
cpudelay = StringVar()
#----------------------#

#DÉFINITIONS#
#----------------------#


def click():
    global bitcoin
    global nram
    bitcoin += 1*nram
    bitcoin = int(bitcoin)
    b.set(bitcoin)

def ram():
    global bitcoin
    global nram
    global pram
    if bitcoin >= pram:
        nram += 1
        r.set(nram)
        bitcoin -= pram
        bitcoin = int(bitcoin)
        b.set(bitcoin)
        pram += 0.2*pram
        pram = int(pram)
        pr.set(pram)

def cpu(): # Non fonctionnel, nécessite du threading
    global bitcoin
    global ncpu
    global pcpu
    if bitcoin >= pcpu:
        if pcpu <= 99:
            ncpu += 1
            c.set(ncpu)
            bitcoin -= pcpu
            bitcoin = int(bitcoin)
            b.set(bitcoin)
            pcpu += 0.2*pcpu
            pcpu = int(pcpu)
            pc.set(pcpu)
            cpudelay = 1-pcpu/100
            if cpu_thread.running:
                END
            else:
                cpu_thread.start_cpu()

class UseCpu(threading.Thread): # Portion de code sur le threading empruntée et modifiée à : https://nitratine.net/blog/post/python-auto-clicker/
    def __init__(self, delay):
        super(UseCpu, self).__init__()
        self.delay = cpudelay
        self.running = False
        self.program_running = True

    def start_cpu(self):
        self.running = True

    def run_cpu(self):
        global bitcoin
        while self.program_running:
            while self.running:
                bitcoin += bitcoin+1
                b.set(bitcoin)
                time.sleep(self.delay)
            time.sleep(0.1)

    def emergency_exit(self):
        self.program_running = False

cpu_thread = UseCpu(cpudelay)
cpu_thread.start()

#----------------------#

imgBitcoin = PhotoImage(file='bitcoin.png')
buttonbtc = Button(window, image=imgBitcoin, command=click, bd=0, bg="#bbbbbb")

imgRAM = PhotoImage(file='ram.png', width=200, height=200)
buttonram = Button(window, image=imgRAM, command=ram, bd=0, bg="#bbbbbb")

imgCPU = PhotoImage(file='cpu.png')
buttoncpu = Button(window, image=imgCPU, command=cpu, bd=0, bg="#bbbbbb")

bitl = Label(window, textvariable=b, bg="#bbbbbb", fg="#333333")
raml = Label(window, textvariable=r, bg="#bbbbbb", fg="#333333")
cpul = Label(window, textvariable=c, bg="#bbbbbb", fg="#333333")

btctext = Label(window, text="Bitcoin", bg="#bbbbbb", fg="#333333", font="fnum")
ramtext = Label(window, text="RAM", bg="#bbbbbb", fg="#333333", font="fnum")
cputext = Label(window, text="CPU", bg="#bbbbbb", fg="#333333", font="fnum")

pramlt = Label(window, text="Prix : ", bg="#bbbbbb", fg="#333333", font="fnum")
pcpult = Label(window, text="Prix : ", bg="#bbbbbb", fg="#333333", font="fnum")
pramlv = Label(window, textvariable=pr, bg="#bbbbbb", fg="#333333", font="fnum")
pcpulv = Label(window, textvariable=pc, bg="#bbbbbb", fg="#333333", font="fnum")

btctext.place(x=85,y=90)
buttonbtc.place(x=10,y=140)
bitl.place(x=85,y=110)

cputext.place(x=598,y=90)
buttoncpu.pack(side="right")
cpul.place(x=598,y=110)
pcpult.place(x=550,y=350)
pcpulv.place(x=590,y=350)

ramtext.place(x=398,y=90)
buttonram.pack(side="right")
raml.place(x=398,y=110)
pramlt.place(x=350,y=350)
pramlv.place(x=390,y=350)

window.mainloop()

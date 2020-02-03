# coding:utf-8
# PRÉREQUIS#
# ----------------------#


from tkinter import * # Import de tkinter pour l'interface utilisateur
import tkinter.font as tkFont # Import des polices d'écriture de tkinter
from math import * # Import du module math
import time # Import du module time
#import random # Import du module random
import threading # Import du threading
from threading import Thread
import sys
#import os
import json
import simpleaudio as sa
#from pydub import AudioSegment
#from pydub.playback import play
bitcoin = 0 # Nb original de BTC
ncpu = 1 # Nb original de CPU
nram = 1 # Nb original de RAM
pram = 100 # Prix original de RAM
pcpu = 200 # Prix original de CPU
musicvar = "base"
playing = "true"
window = Tk() # Définition de l'interface
window.title("Bitcoin Clicker") # Titre de la fenêtre
window.geometry('720x480') # Taille de la fenêtre
window.resizable(False, False) # Empêche l'utilisateur de redimensionner la fenêtre
window.configure(bg="#bbbbbb") # Définit la couleur de fond de la fenêtre
b = StringVar() # Variable nb BTC
c = StringVar() # Variable nb CPU
r = StringVar() # Variable nb RAM
#rand = StringVar() # Variable aléatoire
pr = StringVar() # Variable du prix de la RAM
pc = StringVar() # Variable du prix de la RAM
b.set(bitcoin) # Définit la valeur de bitcoin
c.set(ncpu) # Définit la valeur de CPU
r.set(nram) # Définit la valeur de RAM
pr.set(pram) # Définit la valeur du prix de RAM
pc.set(pcpu) # Définit la valeur du prix de CPU
fnum = tkFont.Font(size=72) # Définit la valeur par défaut de la police d'écriture fnum
sauvefont = tkFont.Font(size=144) # Définit la valeur par défaut de la police d'écriture fnum
cpudelay = StringVar() # Définit la valeur du délai du CPU
e = Entry(window)
cheatvar = StringVar()
#musique = AudioSegment.from_file("music.wav", format="wav")
#play(musique)

playing = "true"
#emergency_key = KeyCode(char='s')
#ram_key = KeyCode(char='r')
#cpu_key = KeyCode(char='c')
#btc_key = KeyCode(char='b')
#cpudelay = StringVar()
#----------------------#

#DÉFINITIONS#
#----------------------#

#def main():
#    f=open("guru99.txt", "r")
#    f1 = f.readlines()
#        contents =f.read()

def cheatcode():
    global bitcoin
    global ncpu
    global pcpu
    global cpudelay
    global nram
    global pram
    global fnum
    cheatvar = e.get()
    if cheatvar == "argent" :
        bitcoin += 1000
        b.set(bitcoin)
    elif cheatvar == "thomas" :
        musicvar == "thomas"
    elif cheatvar == "musique" :
        musicvar == "base"
    print(e.get())


def load():
    global bitcoin
    global ncpu
    global pcpu
    global cpudelay
    global nram
    global pram
    global fnum
    with open('sauve.json', 'r') as f:
        sauve_json = json.load(f)
    bitcoin = sauve_json["bitcoin"]
    b.set(bitcoin)
    ncpu = sauve_json["ncpu"]
    c.set(ncpu)
    nram = sauve_json["nram"]
    r.set(nram)
    pcpu = sauve_json["pcpu"]
    pc.set(pcpu)
    pram = sauve_json["pram"]
    pr.set(pram)


def click(): # Définition de la fonction click
    global bitcoin # Appelle la variable bitcoin
    global nram # Appelle la variable nram
    bitcoin += 1*nram # Ajoute 1 multiplié par nram à bitcoin
    bitcoin = int(bitcoin) # Arrondi bitcoin à l'entier
    b.set(bitcoin) # Met à jour la variable bitcoin


def ram():  # Définition de la fonction ram
    global bitcoin  # Appelle la variable bitcoin
    global nram  # Appelle la variable nram
    global pram  # Appelle la variable pram
    if bitcoin >= pram:  # On vérifie si il y a assez de bitcoin pour acheter une ram
        nram += 1  # On ajoute une ram
        r.set(nram)  # Mise à jour de la ram
        bitcoin -= pram  # Retrait du prix de la ram aux bitcoin
        bitcoin = int(bitcoin)  # Arrondi bitcoin à l'entier
        b.set(bitcoin)  # Met à jour bitcoin
        pram += 0.2*pram  # Augmente le prix de la ram 'pram' par 0.2 + pram (1.2)
        pram = int(pram)  # Arrondi de pram à l'entier
        pr.set(pram)  # Mise à jour de pram


def cpu(): # Non fonctionnel, nécessite du threading
    global bitcoin
    global ncpu
    global pcpu
    global cpudelay
    if bitcoin >= pcpu:
        ncpu += 1
        c.set(ncpu)
        bitcoin -= pcpu
        bitcoin = int(bitcoin)
        b.set(bitcoin)
        pcpu += 0.2*pcpu
        pcpu = int(pcpu)
        pc.set(pcpu)
        cpudelay = 1-pcpu/100


def save():
    global bitcoin
    global ncpu
    global pcpu
    global cpudelay
    global nram
    global pram
    global fnum
    sauve = {"bitcoin": bitcoin, "ncpu": ncpu, "nram": nram, "pcpu": pcpu, "pram": pram} # Sauvegarde des variables dans un vichier json
    with open("sauve.json", "w") as write_file: # Sauvegarde des variables dans un vichier json
        json.dump(sauve, write_file, indent=4) # Sauvegarde des variables dans un vichier json


class Cpu(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global bitcoin
        global ncpu
        while 1:
            time.sleep(1)
            bitcoin += 1*ncpu
            b.set(bitcoin)


class Music(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while playing == "true":
            if musicvar == "thomas":
                wave_base_obj = sa.WaveObject.from_wave_file("thomas.wav")
                play_base_obj = wave_base_obj.play()
                play_base_obj.wait_done()
                playing == "false"
            elif musicvar == "base":
                wave_base_obj = sa.WaveObject.from_wave_file("music.wav")
                play_base_obj = wave_base_obj.play()
                play_base_obj.wait_done()
                playing == "false"

    def stop(self):
        if musicvar == "base":
            wave_base_obj = sa.WaveObject.from_wave_file("music.wav")
            play_base_obj = wave_base_obj.play()
            play_base_obj.stop()
            playing == "false"
        elif musicvar == "thomas":
            wave_base_obj = sa.WaveObject.from_wave_file("thomas.wav")
            play_base_obj = wave_base_obj.play()
            play_base_obj.stop()
            playing == "false"

# Création des threads
threadcpu = Cpu()
threadmusic = Music()

#----------------------#


#background_image = PhotoImage(file="fond.png")
#background_label = Label(window, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

cc = Button(window, text="Utiliser un code", width=16, command=cheatcode)
#cc.place(x=450,y=27)
cc.place(x=577,y=32)

stopsoundbutton = Button(window, text="Stopper les sons", width=16, command=threadmusic.stop)

#stopsoundbutton.place(x=577,y=50)

imgBitcoin = PhotoImage(file='bitcoin.png')
buttonbtc = Button(window, image=imgBitcoin, command=click, bd=0, bg="#bbbbbb") # Bouton bitcoin qui appelle la fonction click

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

titlelabel = Label(window, text="Bitcoin Clicker", bg="#bbbbbb", fg="#333333", font="sauvefont")

savebutton = Button(window, text='Sauvegarder', command=save, bd=0, bg="#bbbbbb", font="sauvefont")
loadbutton = Button(window, text='Charger une sauvegarde', command=load, bd=0, bg="#bbbbbb", font="sauvefont")

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

titlelabel.place(x=315,y=30)

savebutton.place(x=320,y=380)
loadbutton.place(x=280,y=420)

e = Entry(window, width=20)
e.place(x=575,y=10)

cheatvar = e.get()

threadcpu.start()
threadmusic.start()

window.mainloop()

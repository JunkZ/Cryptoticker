import cryptocompare
import requests
from tkinter import *
from tkinter import font
from tkinter import ttk
import time
import threading

coin = input ("Please input target cryptocurrency \n")
curr = input ("Please input target counter-currency \n")

def kill(*args):
    root.destroy()
    
def Crypto():
    BTCPRICE = cryptocompare.get_price(coin,curr=curr)
    print(BTCPRICE)
    v.set(BTCPRICE)
    root.after(2000, Crypto)
    root.config(cursor="none")

    
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", kill)

root.after(1000, Crypto)

BTCPRICE = cryptocompare.get_price(coin)
F = font.Font(family='Helvetica', size=128, weight='bold')
v = StringVar()
v.set(BTCPRICE)
Label = ttk.Label(root, textvariable=v, font=F, foreground="gold", background="black")
Label.place(relx=0.5, rely=0.5, anchor=CENTER)


mainloop()

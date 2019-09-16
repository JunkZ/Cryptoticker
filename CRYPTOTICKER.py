#Copyright (c) 2017-present Klas Mannberg

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

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

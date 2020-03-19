#!/usr/local/bin/python3
import tkinter
# from tkinter import *
from tkinter import ttk
# tkinter.Button(None, text='button').pack()
# tkinter.mainloop()
window = tkinter.Tk()
btn = ttk.Button(None, text='button')
btn.grid(column=0, row=0)
# tkinter.mainloop()
window.mainloop()
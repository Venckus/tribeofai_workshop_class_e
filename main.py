#!/usr/local/bin/python3
import tkinter
# from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class User(object):
    def __init__(self, name):
        self.name = name

# class Chat(object):
#     def process(self, label):

def start_chat():
    txt_input = name_input.get()
    name = validate_name(txt_input)
    label = 'Your name is: ' + name
    introduce.configure(text = label) #, state='disabled')
    # name_input.configure(state='disabled')
    # welcome = f'Welcome {name} :)'
    # history_txt.configure(text = welcome)
    # chat = Chat()
    create_chat_gui(name) #, chat)
    return User(name)

def create_chat_gui(name): #, chat):
    # button
    send_btn = ttk.Button(window, text="send")#.pack(side = "left") #, command=chat.process)
    send_btn.grid(row=3) # column=0, 
    # input
    chat_input = tkinter.Entry(window, width=100)#.pack(side = "left")
    chat_input.grid(row=3) # column=1,
    welcome_msg = f'Hello {name}!'
    # chat history field
    history_txt = tkinter.Label(window, text=welcome_msg,
                                width=380,height=200, bg="yellow")#.pack(side = "left")
    history_txt.grid(row=4) # column=0, 

    # create chat text area
    # chat_history = scrolledtext.ScrolledText(window, text=welcome_msg, width=380,height=400)#, state='disabled')
    # chat_history.grid(column=0, row=4)
    # inputs = tkinter.Entry(window, width=300)
    # inputs.grid(column=0, row=3)

def validate_name(input_name):
    return input_name if input_name != "" else 'Anonymous'


window = tkinter.Tk()
window.title("Chat Bot")
window.geometry('400x600')

# intro text here
intro = tkinter.Label(window, text="Chat with the Bot.", font=('Roboto', 16))
intro.grid(row=0) # column=0, 

# ask for name label
introduce = tkinter.Label(window, text="Enter your name please")
introduce.grid(row=1) # column=0, 

# name text input box
name_input = tkinter.Entry(window, width=10)
name_input.grid(row=1) # column=1, 

start_chat_btn = ttk.Button(window, text="start chat", command=start_chat)# , bg="yellow"
# start_chat_btn = tkinter.Button(text="start chat")#.pack()
user_name = start_chat_btn.grid(row=1) # column=4, 
user = User(user_name)

window.mainloop()

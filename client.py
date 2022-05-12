# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:50:07 2022

@author: Andreea
"""

from socket import *
from threading import Thread
#import tkinter

def receive():
    while True:
        msg = client_socket.recv(BUFSIZ).decode("utf8")
        if msg == "quit":
            client_socket.close()
            break
        if not msg:
            break
        print(msg)
def send():
    while True:
        msg = input()
        if msg == "quit":
            print("You have been disconnected from Tweeter")
            break
        else:
            client_socket.send(bytes(msg, "utf8"))
#def send():
 #   try:
  #      while True:
   #         msg = input()
    #except KeyboardInterrupt:
    #           client_socket.close()
    #else:
     #   client_socket.send(bytes(msg, "utf8"))
       
#def send(event=None):  # event is passed by binders.
 #   msg = my_msg.get()
  #  my_msg.set("")  # Clears input field.
   # client_socket.send(bytes(msg, "utf8"))
   # if msg == "quit":
    #    client_socket.close()
     #   top.quit()


#def on_closing(event=None):
 #   my_msg.set("{quit}")
  #  send()

#top = tkinter.Tk()
#top.title("Tweeter")

#messages_frame = tkinter.Frame(top)
#my_msg = tkinter.StringVar()  
#my_msg.set("Type your messages here.")
#scrollbar = tkinter.Scrollbar(messages_frame) 
#msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
#scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
#msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
#msg_list.pack()
#messages_frame.pack()

host = input('Enter host: ')
port = input('Enter port: ')
if not port:
    port = 33000
else:
    port = int(port)

BUFSIZ = 1024
ADDR = (host, port)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
send_thread = Thread(target=send)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()
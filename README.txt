For this application I used Spyder from Anaconda.

How to build the program:
1.open Anaconda prompt (one to run the server script 
and one for each client)
2.to run the server sript, write "python C:\Users\Andreea\Desktop\server.py" (I put
the path of the server script from my computer as an example,
you need to change it with the path of the file
from your computer) and press "enter"
3.after this, the message "waiting for connection"
will appear
4.now, for each client, we open an Anaconda Prompt and write
"python C:\Users\Andreea\Desktop\client.py" and press "enter"
5.once you press enter, the message "enter host" will appear, and you need 
to introduce 127.0.0.1 to enter the chat
6.also, a port is expected, but it is not mandatory, so you can skip entering a port 
by pressing enter
7.to finally enter the chat, pick and write your nickname and start chatting 
!! You need to repeat each instruction from 4 to 7 (inclusively), changing the nickname 
for each of them
I didn't manage to stop the server when pressing CTRL-C, but I managed to do something
similar for each client, respectively when a client types "quit", he will be disconnected
from the chat. I left the code with my attempt as a comment in the "client" script.  
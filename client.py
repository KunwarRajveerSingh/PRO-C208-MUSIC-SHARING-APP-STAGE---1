import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os


PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox =  None
textarea= None
labelchat = None
text_message = None
filePathLabel = None


def musicWindow():

   
    print("\n\t\t\t\tMUSIC SHARING")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectlabel = Label(window, text= "Select Song", bg='LightSkyBlue', font = ("Calibri",8))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window, height=10, width =39, activestyle='dotbox', bg='LightSkyBlue', borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10,y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)


    playButton = Button(window, text="Play", width=10, bd=1, bg='SkyBlue', font = ("Calibri",10))
    playButton.place(x=30,y=200)

    stopButton = Button(window, text="Stop", width=10, bd=1, bg='SkyBlue', font = ("Calibri",10))
    stopButton.place(x=200, y=200)

    uploadButton = Button(window, text="Upload", width=10, bd=1, bg='SkyBlue', font = ("Calibri",10))
    uploadButton.place(x=30,y=250)

    downloadButton = Button(window, text="Download", width=10, bd=1, bg='SkyBlue', font = ("Calibri",10))
    downloadButton.place(x=200,y=250)

    infoLable = Label(window, text="", fg="blue", font=("Calibri", 10))
    infoLable.place(x=4, y=280)

    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    
       
    musicWindow()

setup()
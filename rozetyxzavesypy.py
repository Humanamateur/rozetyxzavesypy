#!/usr/bin/env python3
from tkinter import *
from pynput.mouse import Listener
from tkinter import font as tkFont

#window
mainWindow = Tk()
screenW = mainWindow.winfo_screenwidth()
screenH = mainWindow.winfo_screenheight()

#colors
bgColor = "#CB273A"
fgColor = "#E18779"
bgEntryColor = "#E49527"
fgEntryColor = "#165C73"

mainWindow.geometry(str(screenW) + 'x' + str(screenH))
mainWindow.title('Electropoli RD login')
mainWindow['bg'] = bgColor

#fonts
Gothic7B = tkFont.Font(family="Gothic", size=int(screenH/10), weight="bold")
Gothic54 = tkFont.Font(family="Gothic", size=int(screenH/60))
Gothic30B = tkFont.Font(family="Gothic", size=int(screenH/35), weight="bold")


def on_click(x, y, button, pressed):
    pass
mainWindow.mainloop()

#Title 
titleLabel = Label(mainWindow, text="ELECTROPOLI")
titleLabel.place(relx=0.2, rely=0.1)
titleLabel['font'] = Gothic7B
titleLabel['bg'] = bgColor
titleLabel['fg'] = fgColor



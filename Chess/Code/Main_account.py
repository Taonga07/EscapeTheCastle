from tkinter import Tk, Label, PhotoImage
from tkinter import*
import tkinter
import Account_Login
import sys

def Open():
    window = Tk()
    window.title("Chess - " + Account_Login.username1 + "'s account")
    canvas = Canvas(window, width = 630, height = 354)      
    canvas.pack() 

    def Home():
        window.destroy()
        start.main_account_screen()
    def Register():
        start.register()
    def LogIn():
        window.destroy()
        start.login()
    def code():
        window.destroy()
        app.start()

    #creating the rooot menu

    root_menu = tkinter.Menu(window)
    window.config(menu = root_menu)

    #creating subs menu 

    home_menu = tkinter.Menu(root_menu)
    acsess_menu = tkinter.Menu(home_menu)
    root_menu.add_cascade(label = "Home", menu = home_menu)
    home_menu.add_cascade(label = "Acsess", menu = acsess_menu)
    acsess_menu.add_command(label = "Home", command = Home)
    acsess_menu.add_command(label = "Register", command = Register)
    acsess_menu.add_command(label = "Log in", command = LogIn)
    home_menu.add_command(label = "code", command = code)
    
if __name__ =="__main__":
    Open()

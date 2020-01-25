from tkinter import *
import loading_screen
import os.path
import os

path = "/media/tempuser/THOMAS/Digi@Local/MyCode/Python/4 - Green/people/"

def register():
    destroy_all()
    global register_screen
    register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("250x200")
    
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()
    

def login():
    global login_screen
    destroy_all()
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("250x220")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
def register_user():
 
    list_of_files = os.listdir(path)
    username_info = username.get()
    password_info = password.get()
    
    if username_info not in list_of_files:
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        file = open(path + username_info, 'w')
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
    else:
        User_Taken()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir(path)
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Main_account.open()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
def User_Taken():
    global User_Taken_screen
    User_Taken_screen = Tk()
    User_Taken_screen.title("Error")
    User_Taken_screen.geometry("130x60")
    Label(User_Taken_screen, text="User taken", fg="red", font=("calibri", 11)).pack()
    Button(User_Taken_screen, text="OK", command=delete_User_Taken).pack()

def password_not_recog():
    global password_not_recog_screen
    password_not_recog_screen = Tk()
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("130x60")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Tk()
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("130x60")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def destroy_all():
    for widget in main_screen.winfo_children():
        if isinstance(widget, Toplevel):
            widget.destroy()
    main_screen.destroy()
 
def delete_User_Taken():
    User_Taken_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("290x200")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()


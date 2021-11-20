#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import os

# student registration window
def register():
    global register_screen
    
    register_screen = Toplevel(main_screen)
    register_screen.title("Student Register")
    register_screen.geometry("300x350")

    global name
    global emailid
    global mobileno
    global username
    global password
    global name_entry
    global emailid_entry
    global mobileno_entry
    global username_entry
    global password_entry
    name = StringVar()
    emailid = StringVar()
    mobileno = StringVar()
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter student details below ").pack()
    Label(register_screen, text=" ").pack()
    name_lable = Label(register_screen, text="Name ")
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    emailid_lable = Label(register_screen, text="Emailid ")
    emailid_lable.pack()
    emailid_entry = Entry(register_screen, textvariable=emailid)
    emailid_entry.pack()
    mobileno_lable = Label(register_screen, text="MobileNo. ")
    mobileno_lable.pack()
    mobileno_entry = Entry(register_screen, textvariable=mobileno)
    mobileno_entry.pack()                                                                   
    username_lable = Label(register_screen, text="Username ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register ", width=10, height=1, command = register_user).pack()

# supervisor registeration window
def newsupervisor():
    global newsupervisor_screen
    newsupervisor_screen = Toplevel(main_screen)
    newsupervisor_screen.title("Register ")
    newsupervisor_screen.geometry("300x350")

    global name
    global emailid
    global mobileno
    global username
    global password
    global name_entry
    global emailid_entry
    global mobileno_entry
    global username_entry
    global password_entry
    name = StringVar()
    emailid = StringVar()
    mobileno = StringVar()
    username = StringVar()
    password = StringVar()

    Label(newsupervisor_screen, text="Supervisor details below ").pack()
    Label(newsupervisor_screen, text="").pack()
    name_lable = Label(newsupervisor_screen, text="Name ")
    name_lable.pack()
    name_entry = Entry(newsupervisor_screen, textvariable=name)
    name_entry.pack()
    emailid_lable = Label(newsupervisor_screen, text="Email ")
    emailid_lable.pack()
    emailid_entry = Entry(newsupervisor_screen, textvariable=emailid)
    emailid_entry.pack()
    mobileno_lable = Label(newsupervisor_screen, text="Mobile No ")
    mobileno_lable.pack()
    mobileno_entry = Entry(newsupervisor_screen, textvariable=mobileno)
    mobileno_entry.pack()    
    username_lable = Label(newsupervisor_screen, text="Username ")
    username_lable.pack()
    username_entry = Entry(newsupervisor_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(newsupervisor_screen, text="Password ")
    password_lable.pack()
    password_entry = Entry(newsupervisor_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(newsupervisor_screen, text=" ").pack()
    Button(newsupervisor_screen, text="Register ", width=10, height=1, command = newsupervisor_user).pack()


# login window 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x350")
    Label(login_screen, text="Enter login details").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# student register button
def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(register_screen, text="Student Registration Success", fg="green", font=("calibri", 11)).pack()

# supervisor register button
def newsupervisor_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(newsupervisor_screen, text="Supervisor Registration Success", fg="green", font=("calibri", 11)).pack()

# login button 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            invalid_password()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Login Successful")
    login_success_screen.geometry("250x150")
    Label(login_success_screen, text="Login Successful").pack()
    Button(login_success_screen, text="OK",width=10, height=1, command=delete_login_success).pack()

# invalid password
def invalid_password():
    global invalid_password_screen
    invalid_password_screen = Toplevel(login_screen)
    invalid_password_screen.title("Error")
    invalid_password_screen.geometry("250x150")
    Label(invalid_password_screen, text="Invalid Password ").pack()
    Button(invalid_password_screen, text="OK",width=10, height=1, command=delete_invalid_password).pack()

#user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("200x150")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",width=10, height=1, command=delete_user_not_found_screen).pack()

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()


def delete_invalid_password():
    invalid_password_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# main window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("450x400")
    main_screen.title("Account Login")
    Label(text="Login and Register", bg="#856ff8", width="300", height="2", font=("playfair display", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Student Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Supervisor Register", height="2", width="30", command=newsupervisor).pack()        
    main_screen.mainloop()


main_account_screen()








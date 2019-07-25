from tkinter import *
import os
from pymysql import*
from tkinter import messagebox as msg

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("1000x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="red").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    
    #username_label.grid(register_screen,row=0,column=0)
    
    username_lable.pack()
    username_entry = Entry(register_screen,textvariable=username)
    #username_entry.grid(register_screen,row=0,column=1)
    username_entry.pack()
    contactnumber_lable = Label(register_screen, text="contact number * ")
    contactnumber_lable.pack()
    contactnumber_entry = Entry(register_screen)
    contactnumber_entry.pack()
    fathername_lable = Label(register_screen, text="father name * ")
    fathername_lable.pack()
    fathername_entry = Entry(register_screen)
    fathername_entry.pack()
    dateofbirth_lable = Label(register_screen, text="Date of birth(YYYY-MM-DD ) * ")
    dateofbirth_lable.pack()
    dateofbirth_entry = Entry(register_screen)
    dateofbirth_entry.pack()
    emailid_lable = Label(register_screen, text="Email Id * ")
    emailid_lable.pack()
    emailid_entry = Entry(register_screen)
    emailid_entry.pack()


    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="red", command = register_user).pack()

 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("3000x2500")
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
 
# Implementing event on register button
 
def register_user():
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
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
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    #Button(login_success_screen, text="OK", command=delete_login_success).pack()
    Button(login_success_screen, text="OK", command=menu).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
def deposit():
    global n1
    global a1
    global if1
    global am1
    global deposit_screen
    deposit_screen = Toplevel(main_screen)
    deposit_screen.title("deposit")
    deposit_screen.geometry("3000x2500")
    Label(deposit_screen, text="Please enter details below to login").pack()
    Label(deposit_screen, text="").pack()

    name_lable = Label(deposit_screen, text="name * ")
    name_lable.pack()
    n1 = Entry(deposit_screen)
    n1.pack()

    account_lable = Label(deposit_screen, text="Account number * ")
    account_lable.pack()
    a1 = Entry(deposit_screen)
    a1.pack()

    ifsc_lable = Label(deposit_screen, text="IFSC code * ")
    ifsc_lable.pack()
    if1 = Entry(deposit_screen)
    if1.pack()

    amount_lable = Label(deposit_screen, text="Amount * ")
    amount_lable.pack()
    am1 = Entry(deposit_screen)
    am1.pack()

    #account_lable = Label(deposit_screen, text="Account number * ")
    Label(deposit_screen, text="").pack()
    Button(deposit_screen, text="deposit", width=10, height=1, bg="red", command = save).pack()
    Label(deposit_screen, text="").pack()
    Button(deposit_screen,text="GO HOME", height="2", width="10",fg='black',bg='orange', command=main_menu).pack()
    Label(deposit_screen,text="").pack(side=left)
def main_menu():
    deposit_screen.destroy()
def save():
    con=connect(db='so',user='root',passwd='system',host='localhost')
    cur=con.cursor()
    #eno=int(account_entry.get())
    name=n1.get()
    account=int(a1.get())
    amount=int(am1.get())
    ifsc=int(if1.get())
    i=cur.execute("insert into emp3 values(%s,'%d',%d, %d)"%(name,account,amount,ifsc))
    if i>=1:
	    con.commit()
	    msg.showinfo('Information','Reocrd Saved')
	    a1.delete(0,'end')
	    n1.delete(0,'end')
	    am1.delete(0,'end')
            
    con.close()
def withdraw():
    global withdraw_screen
    withdraw_screen = Toplevel(main_screen)
    withdraw_screen.title("Withdraw")
    withdraw_screen.geometry("3000x2500")
    Label(withdraw_screen, text="Please enter details below to login").pack()
    Label(withdraw_screen, text="").pack()

    name_lable = Label(withdraw_screen, text="name * ")
    name_lable.pack()
    n1 = Entry(withdraw_screen)
    n1.pack()

    account_lable = Label(withdraw_screen, text="Account number * ")
    account_lable.pack()
    a1 = Entry(withdraw_screen)
    a1.pack()

    ifsc_lable = Label(withdraw_screen, text="IFSC code * ")
    ifsc_lable.pack()
    if1 = Entry(withdraw_screen)
    if1.pack()

    amount_lable = Label(withdraw_screen, text="Amount * ")
    amount_lable.pack()
    am1 = Entry(withdraw_screen)
    am1.pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen, text="withdraw", width=10, height=1, bg="red", command = save).pack()
    Label(withdraw_screen, text="").pack()
    Button(withdraw_screen,text="GO HOME", height="2", width="10",fg='black',bg='orange', command=main_menu1).pack()
    Label(withdraw_screen,text="").pack(side=left)
def main_menu1():
    withdraw_screen.destroy()
    
def menu():
    global menu_screen
    menu_screen = Toplevel(main_screen)
    menu_screen.title("menu")
    menu_screen.geometry("3000x2500")
    Label(menu_screen,text="Select Your Choice", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(menu_screen,text="").pack()    
    Button(menu_screen,text="Deposit", height="2", width="30",fg='black',bg='violet', command=deposit).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen,text="Withdraw", height="2", width="30",fg='black',bg='orange', command=withdraw).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen,text="Balance", height="2", width="30",fg='black',bg='orange', command=balance).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen,text="FUND TRANSFER", height="2", width="30",fg='black',bg='orange', command=fund_transfer).pack()
    Label(menu_screen,text="").pack()
    Button(menu_screen,text="logout", height="2", width="10",fg='black',bg='orange', command=logout2).pack()
    Label(menu_screen,text="").pack(side=left)
def logout2():
    menu_screen.destroy()
def balance():
    global balance_screen
    balance_screen=Toplevel(main_screen)		
    balance_screen.title("balance enquiry")
    withdraw_screen.geometry("300x250")
    Label(withdraw_screen, text="Please enter details below to login").pack()
    Label(withdraw_screen, text="").pack()    
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x2500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="50",fg='black',bg='green' ,font=("Arial Bold", 10)  ,command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="5", width="50",fg='black',bg='blue',font=("Arial Bold", 10), command=register).pack()
    Label(text="").pack()
    Button(text="Deposit", height="5", width="50",fg='black',bg='violet',font=("Arial Bold", 10), command=deposit).pack()
    Label(text="").pack()
    Button(text="Withdraw", height="5", width="50",fg='black',bg='orange',font=("Arial Bold", 10), command=withdraw).pack()
    Label(text="").pack()
 
    main_screen.mainloop()
 
 
main_account_screen()


      







      
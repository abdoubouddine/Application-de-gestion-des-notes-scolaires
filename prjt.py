from tkinter import *
import tkinter.messagebox
import csv
import pandas as pd


#header des colonnes des fichiers des modules
global fieldNames
fieldNames=['Username','Mark']

#creer le fichier des logins csv
with open('Logins.csv','w',newline='') as csvfile1:
    fieldnames=['Username','Password','Module']
    writer=csv.DictWriter(csvfile1,fieldnames=fieldnames)
    writer.writeheader()
#=====================================================================================================

#creer la 1e fenetre
window=Tk()
window.title("Login Window")
window.config(bg='white')
width = 1024
height = 720
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)
image=PhotoImage(file='logo.gif')
w=image.width()
h=image.height()
canvas=Canvas(window,width=w,height=h,bg='blue')
canvas.pack(fill=X)
canvas.create_image(1.35*w,0.5*h,anchor=CENTER,image=image)
Label(window,text='Hello Professor ,\n Hope you are doing fine.\n To register your new module,please click on New in the menu bar.\n To add/update or view or delete marks, please click on  Account in the menu bar.',bg='yellow',font=("Arial black",17)).pack(fill=X,pady='30',ipady="50")
#=====================================================================================================

#QUITTER dans File (barre de menu)
def exit():
    if tkinter.messagebox.askyesno('Quit','Are you sure to quit?'):
        window.destroy()
    else:
        tkinter.messagebox.showinfo('Return','You would like to return then')

#RENITIALISER
def resetN():
    note.delete(0,END)

def resetP():
    password.delete(0,END)

def resetP2():
    passWord.delete(0, END)

#VARIABLES
usrnm=StringVar()
pwd=StringVar()
mdle=StringVar()
mark=IntVar()
username=StringVar()
passWord=StringVar()
nom_etud=StringVar()
#=====================================================================================================


#JOIN du nouveau prof

 #----- interface graphique------#

def register():
    global w2
    w2 = Toplevel()
    w2.title("Register")
    w2.config(bg='grey')
    width = 900
    height = 520
    screen_width = w2.winfo_screenwidth()
    screen_height = w2.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    w2.geometry("%dx%d+%d+%d" % (width, height, x, y))
    w2.resizable(0, 0)
    registerForm()

def registerForm():
    global username
    global password
    global module
    topRegister = Frame(w2, width=600, height=100, bd=1, relief=SOLID)
    topRegister.pack(side=TOP, pady=20)
    lbl_text = Label(topRegister, text="Enter the inputs below please", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    options = Frame(topRegister, width=600)
    options.pack(side=TOP, pady=50)
    lbl_username = Label(options, text="Username :", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lblPwd = Label(options, text="Password:", font=('arial', 25), bd=18)
    lblPwd.grid(row=1)
    lbl_mdl = Label(options, text="Module :", font=('arial', 25), bd=18)
    lbl_mdl.grid(row=2)
    lbl_result = Label(options, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(options, textvariable=usrnm, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(options, textvariable=pwd, font=('arial', 25), width=15,show='*')
    password.grid(row=1, column=1)
    module= Entry(options, textvariable=mdle, font=('arial', 25), width=15)
    module.grid(row=2, column=1)
    btn_add = Button(options, text="Register", font=('arial', 18), width=30, command=check)
    btn_add.grid(row=3, columnspan=2, pady=20)

    # ----- fonction de verification des modules existants------#

def check():
    file=open('logins.csv','r')
    reader = csv.DictReader(file)
    c=0
    for row in reader:
        if module.get() == row[fieldnames[2]]:
            username.delete(0, END)
            password.delete(0, END)
            module.delete(0, END)
            tkinter.messagebox.showwarning('Warning', 'This module has already a professor')
            c=1
            break
    #enregistrement des nouvelles infos
    if c==0:
        file=open(r'logins.csv','a',newline='')
        writer=csv.DictWriter(file,fieldnames)
        writer.writerow({'Username': username.get(), 'Password': password.get(),'Module': module.get()})
        tkinter.messagebox.showinfo('Done',"This module is registred")
        w2.destroy()

#=====================================================================================================

#AUTHENTIFICATION DU PROF

    #----- interface graphique------#

def login2():
    global w3
    w3 = Toplevel()
    w3.title("Login")
    w3.config(bg='grey')
    width = 900
    height = 520
    screen_width = w3.winfo_screenwidth()
    screen_height = w3.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    w3.geometry("%dx%d+%d+%d" % (width, height, x, y))
    w3.resizable(0, 0)
    login2Form()


def login2Form():
    global userName
    global pass_Word
    top_login = Frame(w3, width=600, height=100, bd=1, relief=SOLID)
    top_login.pack(side=TOP, pady=20)
    lbl_text = Label(top_login, text="Enter the inputs below please", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    options = Frame(top_login, width=600)
    options.pack(side=TOP, pady=50)
    lbl_username = Label(options, text="Username :", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_pwd = Label(options, text="Password :", font=('arial', 25), bd=18)
    lbl_pwd.grid(row=1)
    lbl_result = Label(options, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    userName = Entry(options, textvariable=username, font=('arial', 25), width=15)
    userName.grid(row=0, column=1)
    pass_Word = Entry(options, textvariable=passWord, font=('arial', 25), width=15, show='*')
    pass_Word.grid(row=1, column=1)
    btn_login = Button(options, text="Login", font=('arial', 18), width=30, command=verify)
    btn_login.grid(row=2, column=0, pady=20)


    #----- fonction de verification du compte du prof------#

def verify():
    global file
    with open('logins.csv', 'r') as file:
        reader = csv.DictReader(file)
        c = 0
        for row in reader:
            if (userName.get() == row[fieldnames[0]] and pass_Word.get()==row[fieldnames[1]]):
                file=row[fieldnames[2]]   #--save fichier du module selon les infos du prof--#
                Login() #--fonction login définie au dessous--#
                c=1
                break
        if c==0:
            tkinter.messagebox.showwarning('WARNING','Utilisateur introuvable')
        userName.delete(0,END)
        pass_Word.delete(0,END)
#=====================================================================================================


# SAISIR LE NOM DE L'ETUDIANT

     # ----- interface graphique------#

def Login():
    global root
    root = Toplevel(w3)
    root.title("Student Login")
    root.config(bg='white')
    width = 800
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    show_login()


def show_login():
    global nom
    topLogin = Frame(root, width=600, height=100, bd=1, relief=SOLID)
    topLogin.pack(side=TOP, pady=20)
    lbl_text = Label(topLogin, text="Enter the inputs below please", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    options = Frame(topLogin, width=600)
    options.pack(side=TOP, pady=50)
    lbl_usrnm = Label(options, text="Student's name :", font=('arial', 25), bd=18)
    lbl_usrnm.grid(row=1)
    lbl_result = Label(options, text="", font=('arial', 18))
    lbl_result.grid(row=2, columnspan=2)
    nom = Entry(options, textvariable=nom_etud, font=('arial', 25), width=15)
    nom.grid(row=1, column=1)
    btn_choice = Button(options, text="Action", font=('arial', 18), width=30, command=verify_check)
    btn_choice.grid(row=2, columnspan=2, pady=20)


       #----- Faut remplir le champ------#
def verify_check():
    if nom.get() == "":
        tkinter.messagebox.showerror('ERROR',
                                     'Merci de remplir les champs')
    # si le champ est rempli, on passe à la fonction choice définie au dessous
    else:
        choice()

#=====================================================================================================

#CHOISIR (ADD/UPDATE ;  DELETE  ; VIEW)

      #----- interface graphique------#
def choice():
    global login
    login=Toplevel(root)
    login.title("Login")
    window.config(bg='blue')
    width = 900
    height = 520
    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    login.geometry("%dx%d+%d+%d" % (width, height, x, y))
    login.resizable(0, 0)
    show_choices()

def show_choices():
    TopChoice = Frame(login, width=600, height=100, bd=1, relief=SOLID)
    TopChoice.pack(side=TOP, pady=20)
    lbl_text = Label(TopChoice, text="Choose one of the options below", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    options=Frame(login,width=600)
    options.pack(side=TOP,pady=50)
    btn_add = Button(options, text="Add/Update", font=('arial', 18), width=30, command=L_add)
    btn_add.grid(row=1, pady=20)
    btn_delete = Button(options, text="Delete", font=('arial', 18), width=30, command=delete)
    btn_delete.grid(row=3, pady=20)
    btn_view = Button(options, text="View", font=('arial', 18), width=30, command=view)
    btn_view.grid(row=2, pady=20)

#=====================================================================================================

def quitter():

    root.destroy()
#=====================================================================================================

# COMMANDE AJOUTER LA NOTE DE L'ETUDIANT DANS LE FICHIER DU MODULE ADEQUAT

      #----- interface graphique------#

def L_add():
    global w4
    w4 = Toplevel()
    w4.title("Student Login")
    w4.config(bg='white')
    width = 800
    height = 400
    screen_width = w4.winfo_screenwidth()
    screen_height = w4.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    w4.geometry("%dx%d+%d+%d" % (width, height, x, y))
    w4.resizable(0, 0)
    show_l_add()

def show_l_add():
    global note
    topLogin = Frame(w4, width=600, height=100, bd=1, relief=SOLID)
    topLogin.pack(side=TOP, pady=20)
    lbl_text = Label(topLogin, text="Enter the input below please", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    options = Frame(topLogin, width=600)
    options.pack(side=TOP, pady=50)
    lbl_note= Label(options, text="Student's mark :", font=('arial', 25), bd=18)
    lbl_note.grid(row=1)
    lbl_result = Label(options, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    note = Entry(options, textvariable=mark, font=('arial', 25), width=15)
    note.grid(row=2, column=1)
    btn_choice = Button(options, text="Action", font=('arial', 18), width=30, command=add)
    btn_choice.grid(row=2, column=0, pady=20)


    # ----- fonction ajouter------#
def add():
    if note.get() == "":
        tkinter.messagebox.showerror('ERROR',
                                     'Merci de remplir les champs')
    else:
        with open(file+'.csv','w',newline="") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
            writer.writeheader()
        with open(file+'.csv','r') as csvFile:
            reader = csv.DictReader(csvFile)
            c=0
            for row in reader:
                if nom.get()==row[fieldnames[0]]:
                    tkinter.messagebox.showwarning('Warning','Cet étudiant est déjà présent')
                    c=1
                    break
            if c==0:
                with open(file+'.csv', 'a') as csvFile:
                    writer2 = csv.DictWriter(csvFile,fieldNames)
                    writer2.writerow({'Username': nom.get(), 'Mark': note.get()})
    w4.destroy()
#=====================================================================================================

#SUPPRIMER LES INFOS DE L'ETUDIANT

def delete():
    data=pd.read_csv(file+'.csv',index_col="Username")
    data.drop([nom.get()],inplace=True)
    data.to_csv(file+".csv")
    tkinter.messagebox.showinfo('alert'," Mark is removed!")
    login.destroy()

#=====================================================================================================

#IMPRIMER LES INFOS DE L'ETUDIANT DANS LE SHELL DU PYTHON

def view():
    with open(file+'.csv', 'r') as fich:
        reader = csv.DictReader(fich)
        for row in reader:
            if row[fieldNames[0]] == nom.get():
                a=row['Username']
                b=row['Mark']
                print(a,b)
                break


#=====================================================================================================

#creation d'une barre de menu
menu_bar=Menu(window)
#creer un premier menu
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New',command=register)
file_menu.add_command(label='Account',command=login2)
file_menu.add_command(label='Quitter',command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

#configurer notre fenetre pour ajouter cette barre de menu
window.config(menu=menu_bar)

#LABEL WIDGET

image1=PhotoImage(file='ob_5f5da1_login-en.gif')
w1=image1.width()
h1=image1.height()
canvas1=Canvas(window,width=w1,height=2*h1,bg='grey',highlightthickness=0)
canvas1.pack(pady=10,fill=X)
canvas1.create_image(1.35*w,h,anchor=CENTER,image=image1)


#=====================================================================================================

#afficher le tout
window.mainloop()


from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk
from tkinter import Tk, Frame, Canvas, PhotoImage


root = Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)


background=ImageTk.PhotoImage(file='925.png')
backgroundlabel=Label(root,image=background)
backgroundlabel.grid()



def connection():
    conn = pymysql.connect(
        host='localhost', user='root', password='Kasmis@27', db='SQL_1'
    )
    return conn


def next():
    root.destroy()
    import Login2


def signin():
    username = user.get()
    password = code.get()

    conn = connection()
    cursor = conn.cursor()

    # Assuming you have a table named 'users' with columns 'username' and 'password'
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    if result:
        root.destroy()
        import Menu
    else:
        messagebox.showerror("Invalid", "Invalid username and/or password")


img = PhotoImage(file='download.png')
Label(root, image=img, bg='white').place(x=150, y=100)

frame = Frame(root, width=350, height=350, bg="white", relief="ridge", borderwidth=5)
frame.place(x=480, y=70)



heading = Label(frame, text='Sign in', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=120, y=5)

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Mocrosoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'User name')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)



Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    code.delete(0,'end')
def on_leav(e):
    if code.get()=='':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Mocrosoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>",on_leav)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

signin = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=next)
signin.place(x=215, y=270)

root.mainloop()

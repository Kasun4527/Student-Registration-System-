from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk

window = Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

background=ImageTk.PhotoImage(file='925.png')
backgroundlabel=Label(window,image=background)
backgroundlabel.grid()

def back():
    window.destroy()
    import Login
def connection():
    conn = pymysql.connect(
        host='localhost', user='root', password='Kasmis@27', db='SQL_1'
    )
    return conn


def signup():
    username = user.get()
    password = code.get()
    conform_password = conform_code.get()

    if password == conform_password:
        try:
            conn = connection()
            cursor = conn.cursor()

            # Assuming you have a table named 'users' with columns 'username' and 'password'
            query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
            cursor.execute(query)
            conn.commit()
            conn.close()

            messagebox.showinfo('Signup', 'Successfully signed up')
            window.destroy()
            import Login

        except Exception as e:
            messagebox.showerror('Error', f'Error: {str(e)}')

    else:
        messagebox.showerror('Invalid', "Both passwords should match")


def sign():
    messagebox.showerror('Invalid', "Both Passwords should match")


img = PhotoImage(file='download.png')
Label(window, image=img, border=0, bg='white').place(x=150, y=125)

frame = Frame(window, width=350, height=390, bg='#fff',relief="ridge",borderwidth=5)
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 24, 'bold'))
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
        code.insert(0,'Password')
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Mocrosoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>",on_leav)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

def on_enter(e):
    conform_code.delete(0,'end')
def on_leave(e):
    if conform_code.get()=='':
        conform_code.insert(0,'Conform Password')
conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Mocrosoft Yahei UI Light', 11))
conform_code.place(x=30, y=220)
conform_code.insert(0, 'Conform Password')
conform_code.bind("<FocusIn>",on_enter)
conform_code.bind(("<FocusOut>",on_leave))

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=90, y=340)

signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=back)
signin.place(x=200, y=340)

window.mainloop()

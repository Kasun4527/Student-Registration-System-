import pymysql
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, Label




def connection():
    conn = pymysql.connect(
        host='localhost', user='root', password='Kasmis@27', db='SQL_1'
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tags="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Microsoft Yahei UI Light', 10, 'bold'))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

def setph(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * from students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    if (studid == "" or studid == " ") or (fname == "" or fname == " ") or (lname == "" or lname == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students VALUES('" + studid + "','" + fname + "','" + lname + "','" + address + "','" + phone + "')")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exists")
            return

    refreshTable()

def reset():
    decision = messagebox.askquestion("Warning!", "Delete all data?")
    if decision != "yes":
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Error deleting data")

    refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        studid = str(my_tree.item(selected_item)['values'][0])
        fname = str(my_tree.item(selected_item)['values'][1])
        lname = str(my_tree.item(selected_item)['values'][2])
        address = str(my_tree.item(selected_item)['values'][3])
        phone = str(my_tree.item(selected_item)['values'][4])

        setph(studid, 1)
        setph(fname, 2)
        setph(lname, 3)
        setph(address, 4)
        setph(phone, 5)

    except IndexError:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE STUDID='" +
                   studid + "' or FNAME='" +
                   fname + "' or LNAME='" +
                   lname + "' or ADDRESS='" +
                   address + "' or PHONE='" +
                   phone + "' ")

    try:
        result = cursor.fetchall()
        for num in range(0, 5):
            setph(result[0][num], (num + 1))

        conn.commit()
        conn.close()

    except:
        messagebox.showinfo("Error", "No data found")

def delete():
    decision = messagebox.askquestion("Warning!", "Delete the selected data")

    if decision != "yes":
        return
    else:
        selected_items = my_tree.selection()

        # Check if any item is selected
        if not selected_items:
            messagebox.showinfo("Error", "Please select an item to delete.")
            return

        selected_item = selected_items[0]
        deletedata = str(my_tree.item(selected_item)['values'][0])

        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE STUDID='" + str(deletedata) + "'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry, an error occurred")
            return

        refreshTable()


def clear_entries():
    studidEntry.delete(0, 'end')
    fnameEntry.delete(0, 'end')
    lnameEntry.delete(0, 'end')
    addressEntry.delete(0, 'end')
    phoneEntry.delete(0, 'end')
    ph1.set("")
    ph2.set("")
    ph3.set("")
    ph4.set("")
    ph5.set("")

def update():
    selectedStudid = ""
    try:
        selected_item = my_tree.selection()[0]
        selectedStudid = str(my_tree.item(selected_item)['values'][0])

    except IndexError:
        messagebox.showinfo("Error", "Please select a data row")
        return

    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())

    if (studid == "" or studid.isspace()) or (fname == "" or fname.isspace()) or (lname == "" or lname.isspace()) or (address == "" or address.isspace()) or (phone == "" or phone.isspace()):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET STUDID='" +
                           studid + "',FNAME='" +
                           fname + "',LNAME='" +
                           lname + "',ADDRESS='" +
                           address + "',PHONE='" +
                           phone + "' WHERE STUDID='" +
                           selectedStudid + "' ")
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showinfo("Error", f"Error updating data: {e}")
            return

    refreshTable()

root = Tk()
root.resizable(0, 0)
root.title("Student Registration System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)


background_image = Image.open("1080.png")  # Replace with the actual path to your image file
background_photo = ImageTk.PhotoImage(background_image)


background_label = Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, width=830, height=450, bg="white", relief="ridge", borderwidth=5)
frame.place(x=5, y=150)





frame = tk.Frame(root,bg='white')


ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

label = Label(root, text="Student Registration System", fg="#57a1f8",bg='white', font=('Microsoft Yahei UI Light', 17, 'bold'))
label.grid(row=0, column=0, columnspan=8, rowspan=1, padx=50, pady=40)




studidLabel = Label(root, text="Student ID ",bg='white',fg='#57a1f8', font=('Microsoft Yahei UI Light', 12, 'bold'))
fnameLabel = Label(root, text="Firstname",bg='white',fg='#57a1f8', font=('Microsoft Yahei UI Light', 12, 'bold'))
lnameLabel = Label(root, text="Lastname",bg='white',fg='#57a1f8', font=('Microsoft Yahei UI Light', 12, 'bold'))
addressLabel = Label(root, text="Address",bg='white',fg='#57a1f8', font=('Microsoft Yahei UI Light', 12, 'bold'))
phoneLabel = Label(root, text="Phone",bg='white',fg='#57a1f8', font=('Microsoft Yahei UI Light', 12, 'bold'))

studidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5, sticky='w')
fnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5, sticky='w')
lnameLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5, sticky='w')
addressLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5, sticky='w')
phoneLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5, sticky='w')

studidEntry = ttk.Entry(root, width=60, font=('Microsoft Yahei UI Light', 10, 'bold'), textvariable=ph1)
studidEntry.grid(row=3, column=1, columnspan=1, padx=5, pady=0)

fnameEntry = ttk.Entry(root, width=60, font=('Microsoft Yahei UI Light', 10, 'bold'), textvariable=ph2)
fnameEntry.grid(row=4, column=1, columnspan=1, padx=5, pady=0)

lnameEntry = ttk.Entry(root, width=60, font=('Microsoft Yahei UI Light', 10, 'bold'), textvariable=ph3)
lnameEntry.grid(row=5, column=1, columnspan=1, padx=5, pady=0)

addressEntry = ttk.Entry(root, width=60, font=('Microsoft Yahei UI Light', 10, 'bold'), textvariable=ph4)
addressEntry.grid(row=6, column=1, columnspan=1, padx=5, pady=0)

phoneEntry = ttk.Entry(root, width=60, font=('Microsoft Yahei UI Light', 10, 'bold'), textvariable=ph5)
phoneEntry.grid(row=7, column=1, columnspan=1, padx=5, pady=0)

addBtn = Button(
    root, width=10, padx=65, pady=7, text="Add", bg='#57a1f8', fg='White', font=('Verdana', 10, 'bold'), command=add
)
updateBtn = Button(
    root, width=10, padx=65, pady=7, text="Update", bg='#57a1f8', fg='White', font=('Verdana', 10, 'bold'), command=update
)

deleteBtn = Button(
    root, width=10, padx=65, pady=7, text="Delete", bg='#57a1f8', fg='White', font=('Verdana', 10, 'bold'), command=delete
)

searchBtn = Button(
    root, width=10, padx=65, pady=7, text="Search", bg='#57a1f8', fg='White', font=('Verdana', 10, 'bold'), command=search
)
resetBtn = Button(
    root, width=10, padx=65, pady=7, text="Reset", bg='#57a1f8', fg='White', font=('Verdana', 10, 'bold'), command=reset
)

selectBtn = Button(
    root, width=10, padx=65, pady=7, text="Select", bg='#57a1f8', fg='White', font=('Verdana', 10, 'bold'), command=select
)
clearBtn = Button(
    root, width=10, padx=65, pady=7, text="Clear", bg='#57a1f8', fg='White', font=('Verdana', 10, 'bold'), command=clear_entries
)

addBtn.grid(row=2, column=5, columnspan=1, rowspan=1)
updateBtn.grid(row=4, column=5, columnspan=1, rowspan=1)
searchBtn.grid(row=6, column=5, columnspan=1, rowspan=1)
deleteBtn.grid(row=8, column=5, columnspan=1, rowspan=1)
selectBtn.grid(row=11, column=5, columnspan=1, rowspan=1)
resetBtn.grid(row=14, column=5, columnspan=1, rowspan=1)
clearBtn.grid(row=17, column=5, columnspan=1, rowspan=1)


my_tree = ttk.Treeview(root)
my_tree["columns"] = ("Stud ID", "Firstname", "Lastname", "Address", "Phone")



my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Stud ID", anchor=W, width=170,)
my_tree.column("Firstname", anchor=W, width=150)
my_tree.column("Lastname", anchor=W, width=150)
my_tree.column("Address", anchor=W, stretch=165)
my_tree.column("Phone", anchor=W, width=150)

my_tree.heading("Stud ID", text="Student ID", anchor="w")
my_tree.heading("Firstname", text="Firstname", anchor=W)
my_tree.heading("Lastname", text="Lastname", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("Phone", text="Phone", anchor=W)
refreshTable()

root.mainloop()

import tkinter.messagebox
from tkinter import  *
import random as rd
import datetime 
import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",password="nishayadav")
cur=con.cursor()
cur = con.cursor(buffered=True) 
cur.execute("create database if not exists hello")

cur.execute("use hello")

cur.execute("create table if not exists apt"
            "("
            "idno varchar(12) primary key,"
            "name char(20),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")



#  Message for registration
def entry():
    global e1,e2,e3,e4,e5,e6
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()
        
    cur.execute('insert into apt values(%s,%s,%s,%s,%s,%s)',(p1,p2,p3,p4,p5,p6,))
    con.commit()
    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")

#  For registration 
def register():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    label=Label(root1,text="REGISTER YOURSELF",font='arial 25 bold')
    label.pack()
    frame=Frame(root1,height=500,width=200)
    frame.pack()
    l1=Label(root1,text="PATIENT ID")
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root1)
    e1.place(x=100,y=130)
    l2=Label(root1,text="NAME")
    l2.place(x=10,y=170)
    e2=tkinter.Entry(root1)
    e2.place(x=100,y=170)
    l3=Label(root1,text="AGE")
    l3.place(x=10,y=210)
    e3=tkinter.Entry(root1)
    e3.place(x=100,y=210)
    l4=Label(root1,text="GENDER M\F")
    l4.place(x=10,y=250)
    e4=tkinter.Entry(root1)
    e4.place(x=100,y=250)
    l5=Label(root1,text="PHONE")
    l5.place(x=10,y=290)
    e5=tkinter.Entry(root1)
    e5.place(x=100,y=290)
    l6=Label(root1,text="BLOOD GROUP")
    l6.place(x=10,y=330)
    e6=tkinter.Entry(root1)
    e6.place(x=100,y=330)
    b1=Button(root1,text="SUBMIT",command=entry)
    b1.place(x=150,y=370)
    
    root.resizable(False,False)
    root1.mainloop()


root=Tk()
root.geometry("900x700")
root.config(background="white")
root.resizable(0,0)
label=Label(root,text=" CITY HOSPITAL    ",font="arial 40 bold",bg='white').place(x=180,y=20)
b1=Button(root,text=  "     Registration  ",font=("arial 20 bold",15,"bold"),bd=0,bg='white',command=register).place(x=120,y=240)
b2=Button(root,text=  " Appointment       ",font=("arial 20 bold",15,"bold"),bd=0,bg='white').place(x=380,y=240)
b3=Button(root,text=  "   List of Doctors  ",font=("arial 20 bold",15,"bold"),bd=0,bg='white').place(x=120,y=430)
b4=Button(root,text=  "Services available",font=('arial 20 bold',15,"bold"),bd=0,bg='white').place(x=380,y=430)
b5=Button(root,text=  "Modify data       ",font=('arial 20 bold',15,"bold"),bd=0,bg='white').place(x=620,y=240)
b6=Button(root,text=  "        Exit     ",font=('arial 20 bold',15,"bold"),bd=0,command=root.destroy,bg='white').place(x=620,y=430)

root.mainloop()

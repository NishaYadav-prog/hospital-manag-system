from tkinter import  *

    
root=Tk()
root.geometry("900x700")
root.config(background="white")
root.resizable(0,0)


label=Label(root,text=" CITY HOSPITAL    ",font="arial 40 bold",bg='white').place(x=180,y=20)
b1=Button(root,text=  "     Registration  ",font=("arial 20 bold",15,"bold"),bd=0,bg='white').place(x=120,y=240)
b2=Button(root,text=  " Appointment       ",font=("arial 20 bold",15,"bold"),bd=0,bg='white').place(x=380,y=240)
b3=Button(root,text=  "   List of Doctors  ",font=("arial 20 bold",15,"bold"),bd=0,bg='white').place(x=120,y=430)
b4=Button(root,text=  "Services available",font=('arial 20 bold',15,"bold"),bd=0,bg='white').place(x=380,y=430)
b5=Button(root,text=  "Modify data       ",font=('arial 20 bold',15,"bold"),bd=0,bg='white').place(x=620,y=240)
b6=Button(root,text=  "        Exit     ",font=('arial 20 bold',15,"bold"),bd=0,command=root.destroy,bg='white').place(x=620,y=430)
      

root.mainloop()

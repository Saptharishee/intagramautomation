
from login_insta_to_import import *
#print("point1")
import tkinter
from tkinter import *
loginbut=Button(top,text="Login insta with default ",bg="blue",fg="white",font=("Impact",20),command=login)
loginbut.place(x=75,y=400)
t1=Label(top,text="INSTABOT-GUI",bg="pink",fg="white",font=("Times New Roman",40))
t1.place(x=100,y=10)
l1=Label(top,text="1.message in group",fg='black',font=("Constantia",30))
l1.place(x=20,y=80)
b1=Button(top,text="run",bg="blue",fg="white",font=("Impact",20),command=message_ingrp)

b1.place(x=400,y=80)
top.mainloop()

from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry("500x500")
window.configure(background="grey", borderwidth=5,relief="solid")

def button_clicked(item):
    number1=Ent.get()
    Ent.delete(0,END)
    Ent.insert(0,str(number1)+str(item))

def button_clear():
    Ent.delete(0,END)

def button_add():
    first_number=Ent.get()
    global f_number
    global operation
    operation="addition"
    f_number=float(first_number)
    Ent.delete(0,END)
def button_subtraction():
    first_number=Ent.get()
    global f_number
    global operation
    operation="subtraction"
    f_number=float(first_number)
    Ent.delete(0,END)
def button_multiplication():
    first_number=Ent.get()
    global f_number
    global operation
    operation="multiplication"
    f_number=float(first_number)
    Ent.delete(0,END)
def button_division():
    first_number=Ent.get()
    global f_number
    global operation
    operation="division"
    f_number=float(first_number)
    Ent.delete(0,END)
def button_percentage():
    first_number=Ent.get()
    global f_number
    global operation
    operation="percentage"
    f_number=float(first_number)
    Ent.delete(0,END)

def button_cube():
    first_number=Ent.get()
    global f_number
    global operation
    operation="cube"
    f_number=float(first_number)
    Ent.delete(0,END)

def button_square():
    first_number=Ent.get()
    global f_number
    global operation
    operation="square"
    f_number=float(first_number)
    Ent.delete(0,END)






def button_equal():
    second_number = Ent.get()

    Ent.delete(0,END)

    if operation=="addition":
        Ent.insert(0,f_number+float(second_number))
    elif operation=="subtraction":
        Ent.insert(0,f_number-float(second_number))
    elif operation=="multiplication":
        Ent.insert(0,f_number*float(second_number))
    elif operation=="division":
        Ent.insert(0,f_number/float(second_number))
    elif operation=="percentage":
        Ent.insert(0,f_number/100)
    elif operation=="square":
        Ent.insert(0,f_number*f_number)
    elif operation=="cube":
        Ent.insert(0,f_number*f_number*f_number)



Ent=Entry(window,width=35)
button1=Button(text="7",width=8,height=3,command=lambda:button_clicked(7))
button2=Button(text="8",width=8,height=3,command=lambda:button_clicked(8))
button3=Button(text="9",width=8,height=3,command=lambda:button_clicked(9))
button4=Button(text="4",width=8,height=3,command=lambda:button_clicked(4))
button5=Button(text="5",width=8,height=3,command=lambda:button_clicked(5))
button6=Button(text="6",width=8,height=3,command=lambda:button_clicked(6))
button7=Button(text="1",width=8,height=3,command=lambda:button_clicked(1))
button8=Button(text="2",width=8,height=3,command=lambda:button_clicked(2))
button9=Button(text="3",width=8,height=3,command=lambda:button_clicked(3))
button10=Button(text="%",width=8,height=3,command=button_percentage)
button11=Button(text="0",width=8,height=3,command=lambda:button_clicked(0))
button12=Button(text=".",width=8,height=3,command=lambda:button_clicked("."))
button13=Button(text="+",width=8,height=3,command=button_add)
button14=Button(text="-",width=8,height=3,command=button_subtraction)
button15=Button(text="*",width=8,height=3,command=button_multiplication)
button16=Button(text="/",width=8,height=3,command=button_division)
button17=Button(text="AC",width=8,height=3,command=button_clear)
button18=Button(text="=",width=8,height=3,command=button_equal)
button19=Button(text="^3",width=8,height=3,command=button_cube)
button20=Button(text="^2",width=8,height=3,command=button_square)
Ent.grid(row=0,columnspan=5,padx=10,pady=10,ipady=20)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1,padx=(20,20))
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button10.grid(row=4,column=0)
button11.grid(row=4,column=1)
button12.grid(row=4,column=2)
button13.grid(row=5,column=0)
button14.grid(row=5,column=1)
button15.grid(row=5,column=2)
button16.grid(row=3,column=3)
button17.grid(row=4,column=3)
button18.grid(row=5,column=3)
button19.grid(row=1,column=3)
button20.grid(row=2,column=3)


window.mainloop()
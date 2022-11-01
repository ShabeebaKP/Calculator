from tkinter import *

window=Tk()
window.geometry("1000x1000")
window.title("calculator")
window.configure(bg="pink")

def hello():
    print("Button clicked")
button1=Button(text="ok",width=30,height=10,command=hello)
button2=Button(text="ok",width=30,height=10,command=hello)

label=Label(window,text="welcome")
button1.grid(row=0,column=0,padx=(50,0),pady=(0,0))
button2.grid(row=0,column=1)

T=Text(window,height=10,width=10)

T.grid()




window.mainloop()
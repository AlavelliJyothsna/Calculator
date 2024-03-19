from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.configure(background="black")
e=Entry(root,width=27,borderwidth=10,fg="white",bd=13,bg="black",justify="right",font=("Arial",0,"bold"))
e.grid(row=0,column=0,columnspan=10,padx=1,pady=1)

def buttonclick(number):
   current=e.get()
   e.delete(0,END)
   e.insert(0,str(current)+str(number))
def clear():
  e.delete(0,END)
def buttonadd():
  firstnum=e.get()
  global fnum
  global math
  math="add"
  fnum=int(firstnum)
  e.delete(0,END)

def equal():
  secondnum=e.get()
  e.delete(0,END)
  if math=="add":
    e.insert(0,fnum+int(secondnum))
  elif math=="sub":
    e.insert(0,fnum-int(secondnum))
  elif math=="mul":
    e.insert(0,fnum*int(secondnum))
  elif math=="div":
    e.insert(0,fnum/int(secondnum))
  elif math=="pow":
    e.insert(0,fnum**int(secondnum))

def sub():
  firstnum=e.get()
  global fnum
  global math
  math="sub"
  fnum=int(firstnum)
  e.delete(0,END)
  return
def mul():
  firstnum=e.get()
  global fnum
  global math
  math="mul"
  fnum=int(firstnum)
  e.delete(0,END)
  return
def div():
  firstnum=e.get()
  global fnum
  global math
  math="div"
  fnum=int(firstnum)
  e.delete(0,END)
  return
def pow():
  firstnum=e.get()
  global fnum
  global math
  math="pow"
  fnum=int(firstnum)
  e.delete(0,END)
  return

button1=Button(root,text="1",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(1),font=("Arial"))
button2=Button(root,text="2",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(2),font=("Arial"))
button3=Button(root,text="3",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(3),font=("Arial"))
button4=Button(root,text="4",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(4),font=("Arial"))
button5=Button(root,text="5",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(5),font=("Arial"))
button6=Button(root,text="6",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(6),font=("Arial"))
button7=Button(root,text="7",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(7),font=("Arial"))
button8=Button(root,text="8",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(8),font=("Arial"))
button9=Button(root,text="9",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(9),font=("Arial"))
button0=Button(root,text="0",width=9,height=2,fg="white",bg="black",command=lambda:buttonclick(0),font=("Arial"))

buttonadd=Button(root,text="+",width=9,height=2,fg="white",bg="black",command=buttonadd,font=("Arial"))
buttonsub=Button(root,text="-",width=9,height=2,fg="white",bg="black",command=sub,font=("Arial"))
buttonmul=Button(root,text="*",width=9,height=2,fg="white",bg="black",command=mul,font=("Arial"))
buttondiv=Button(root,text="/",width=9,height=2,fg="white",bg="black",command=div,font=("Arial"))
buttonequl=Button(root,text="=",width=9,height=2,fg="white",bg="black",command=equal,font=("Arial"))
buttonclear=Button(root,text="clear",width=9,height=2,fg="white",bg="black",command=clear,font=("Arial"))
buttonpow=Button(root,text="pow",width=9,height=2,fg="white",bg="black",command=pow,font=("Arial"))
buttonquit=Button(root,text="exit",width=9,height=2,fg="white",bg="black",command=root.quit,font=("Arial"))

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonadd.grid(row=4,column=1)
buttonsub.grid(row=4,column=2)
buttonmul.grid(row=5,column=0)
buttondiv.grid(row=5,column=1)
buttonclear.grid(row=6,column=0)
buttonequl.grid(row=5,column=2)
buttonpow.grid(row=6,column=1)
buttonquit.grid(row=6,column=2)

root.mainloop()
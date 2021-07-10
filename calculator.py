from tkinter import*
tk = Tk()
tk.geometry("354x460")
tk.title("Calculator")

tk.config(background='Dark gray')


operator = ""
textin = StringVar()

def click_button(num):
  global operator
  operator = operator + str(num)
  textin.set(operator) 
def equlbut():
  try:
       global operator
       op=str(eval(operator))
       textin.set(op)
       operator=''
  except:
      textin("error")

def clrbut():
     global operator
     textin.set('')
     operator=''

     
text=Entry(tk,font=("Courier New",12,'bold'),textvar=textin,width=65,bd=10,bg='red')
text.pack(side=TOP)

but1=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

butdot=Button(tk,padx=47,pady=14,bd=4,bg='white',command=lambda:click_button("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)

butpl=Button(tk,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:click_button("+"),font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(tk,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:click_button("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(tk,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:click_button("*"),font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(tk,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:click_button("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(tk,padx=14,pady=119,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)

butequal=Button(tk,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)
tk.mainloop()

from tkinter import *
w1=Tk()
w1.title('CONVERTER')
def sel():
   w2=Tk()
   w2.title('CONVERTER')
   def formats(x):
       y=len(x)
       n=str(x)
       t=tuple(n)
       z=''
       for e in range (2,y):
              z=z+t[e]
       return z
   if(d.get()=='Binary to Decimal'):
      l1=Label(w2,font=("times new roman",30))
      l1.pack(side=TOP)
      s1=d.get()
      l1.config(text=s1)
      def btd():
          num=e1.get()
          i=int(num,2)
          e2.delete(0,END)
          e2.insert(0,i)
      l1=Label(w2,font=("times new roman",30))
      l1.pack(side=TOP)
      l2=Label(w2,text="Enter a number in 0 or 1 only",font=("times new roman",20))
      l2.place(x=200,y=200)
      e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
      e1.place(x=540,y=210)
      e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
      e2.place(x=540,y=310)
      b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=btd)
      b.place(x=340,y=270)
   elif(d.get()=='Binary to Octal'):
       l1=Label(w2,font=("times new roman",30))
       l1.pack(side=TOP)
       s1=d.get()
       def bto():
          num=e1.get()
          i=int(num,2)
          z=oct(i)
          i=formats(z)
          e2.delete(0,END)
          e2.insert(0,i)
       l1.config(text=s1)
       l2=Label(w2,text="Enter a number in 0 or 1 only",font=("times new roman",20))
       l2.place(x=200,y=200)
       e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
       e1.place(x=540,y=210)
       e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
       e2.place(x=540,y=310)
       b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=bto)
       b.place(x=340,y=270)
   elif(d.get()=='Binary to Hexadecimal'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=d.get()
    def bth():
       num=e1.get()
       i=int(num,2)
       z=hex(i)
       i=formats(z)
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 1 only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=540,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=bth)
    b.place(x=340,y=270)
  
 

def sel1():
 w2=Tk()
 w2.title('CONVERTER')
 def formats(x):
       y=len(x)
       n=str(x)
       t=tuple(n)
       z=''
       for e in range (2,y):
              z=z+t[e]
       return z
 if(b1.get()=='Decimal to Binary'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=b1.get()
    def dtb():
       num=e1.get()
       num1=int(num)
       z=bin(num1)
       i=formats(z)
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 9 only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=540,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=dtb)
    b.place(x=340,y=270)
 elif(b1.get()=='Decimal to Octal'):
      l1=Label(w2,font=("times new roman",30))
      l1.pack(side=TOP)
      s1=b1.get()
      def dto():
          num=e1.get()
          num1=int(num)
          z=oct(num1)
          i=formats(z)
          e2.delete(0,END)
          e2.insert(0,i)
      l1.config(text=s1)
      l2=Label(w2,text="Enter a number in 0 or 9 only",font=("times new roman",20))
      l2.place(x=200,y=200)
      e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
      e1.place(x=540,y=210)
      e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
      e2.place(x=540,y=310)
      b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=dto)
      b.place(x=340,y=270)
 elif(b1.get()=='Decimal to Hexadecimal'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=b1.get()
    def dth():
       num=e1.get()
       num1=int(num)
       z=hex(num1)
       i=formats(z)
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 9 only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=540,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=dth)
    b.place(x=340,y=270)

def sel2():
 w2=Tk()
 w2.title('CONVERTER')
 def formats(x):
       y=len(x)
       n=str(x)
       t=tuple(n)
       z=''
       for e in range (2,y):
              z=z+t[e]
       return z
 if(b2.get()=='Octal to Binary'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=b2.get()
    def otb():
       num=e1.get()
       num1=int(num,8)
       z=bin(num1)
       i=formats(z)
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 7 only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=540,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=otb)
    b.place(x=340,y=270)
 elif(b2.get()=='Octal to Decimal'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=b2.get()
    def otd():
       num=e1.get()
       i=int(num,8)
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 7 only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=540,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=otd)
    b.place(x=340,y=270)
 elif(b2.get()=='Octal to Hexadecimal'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=b2.get()
    def oth():
       num=e1.get()
       num1=int(num,8)
       z=hex(num1)
       i=formats(z)
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 7 only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=540,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=oth)
    b.place(x=340,y=270)

def sel3():
 w2=Tk()
 w2.title('CONVERTER')
 def formats(x):
       y=len(x)
       n=str(x)
       t=tuple(n)
       z=''
       for e in range (2,y):
              z=z+t[e]
       return z
 if(b4.get()=='Hexadecimal to Binary'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=b4.get()
    def htb():
       num=e1.get()
       num1=int(num,16)
       z=bin(num1)
       i=formats(z)
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 9 and a to f only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=650,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=htb)
    b.place(x=340,y=270)
 elif(b4.get()=='Hexadecimal to Octal'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=b4.get()
    def hto():
       num=e1.get()
       num1=int(num,16)
       z=oct(num1)
       i=formats(z)
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 9 and a to f only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=650,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=hto)
    b.place(x=340,y=270)
 elif(b4.get()=='Hexadecimal to Decimal'):
    l1=Label(w2,font=("times new roman",30))
    l1.pack(side=TOP)
    s1=b4.get()
    def htd():
       num=e1.get()
       num1=int(num,16)
       i=num1
       e2.delete(0,END)
       e2.insert(0,i)
    l1.config(text=s1)
    l2=Label(w2,text="Enter a number in 0 or 9 and a to f only",font=("times new roman",20))
    l2.place(x=200,y=200)
    e1=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e1.place(x=650,y=210)
    e2=Entry(w2,bd=4,bg='tan1',font=("times new roman",20))
    e2.place(x=540,y=310)
    b=Button(w2,text="Answer",bd=4,font=("times new roman",20),bg='cyan',command=htd)
    b.place(x=340,y=270)
 

l=Label(w1,text="CONVERSIONS",font=("times new roman",30))
l.pack(side=TOP)

m1=Menubutton(w1,text="Binary to",font=("times new roman",25),relief=RAISED)
m1.place(x=2,y=250)
m1.menu= Menu(m1, tearoff = 0 )
m1["menu"]  =  m1.menu
d=StringVar()

m1.menu.add_radiobutton(label="Decimal",variable=d,value='Binary to Decimal',command=sel)
m1.menu.add_radiobutton(label="Octal",variable=d,value='Binary to Octal',command=sel)
m1.menu.add_radiobutton(label="Hexadecimal",variable=d,value='Binary to Hexadecimal',command=sel)
m1.place(x=10,y=250)



m2=Menubutton(w1,text="Decimal to",font=("times new roman",25),relief=RAISED)
m2.place(x=400,y=250)
m2.menu= Menu(m2, tearoff = 0 )
m2["menu"]  =  m2.menu
b1=StringVar()
m2.menu.add_radiobutton(label="Binary",variable=b1,value='Decimal to Binary',command=sel1)
m2.menu.add_radiobutton(label="Octal",variable=b1,value='Decimal to Octal',command=sel1)
m2.menu.add_radiobutton(label="Hexadecimal",variable=b1,value='Decimal to Hexadecimal',command=sel1)
m2.place(x=400,y=250)

m3=Menubutton(w1,text="Octal to",font=("times new roman",25),relief=RAISED)
m3.place(x=800,y=250)
m3.menu= Menu(m3, tearoff = 0 )
m3["menu"]  =  m3.menu
b2=StringVar()
m3.menu.add_radiobutton(label="Binary",variable=b2,value='Octal to Binary',command=sel2)
m3.menu.add_radiobutton(label="Decimal",variable=b2,value='Octal to Decimal',command=sel2)
m3.menu.add_radiobutton(label="Hexadecimal",variable=b2,value='Octal to Hexadecimal',command=sel2)
m3.place(x=800,y=250)

m4=Menubutton(w1,text="Hexadecimal to",font=("times new roman",25),relief=RAISED)
m4.place(x=1200,y=250)
m4.menu= Menu(m4, tearoff = 0 )
m4["menu"]  =  m4.menu
b4=StringVar()
m4.menu.add_radiobutton(label="Binary",variable=b4,value='Hexadecimal to Binary',command=sel3)
m4.menu.add_radiobutton(label="Octal",variable=b4,value='Hexadecimal to Octal',command=sel3)
m4.menu.add_radiobutton(label="Decimal",variable=b4,value='Hexadecimal to Decimal',command=sel3)
m4.place(x=1110,y=250)

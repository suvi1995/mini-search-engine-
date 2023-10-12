from tkinter import*
from tkinter import ttk
from tkinter import messagebox as m
import wikipedia as wiki
import random as r
from PIL import ImageTk, Image
def search():
    un=entry.get()
    ps=psw_entry.get()
    ps1=psw1_entry.get()
    username_info=username.get()
    password_info=password.get()
    cpassword_info=password.get()
    if ps=="" and ps1=="":
        m.showerror("","Please Enter Details")
    elif ps!=ps1:
        m.showerror("","Password Mismatch")
    elif ps==ps1:
        m.showinfo("","Signup Successfully")    
        w=Tk()
        w.geometry("1980x1080")
        w.title("Comic World")
        w.config(bg="sky blue")
        frame=Frame(w,width=700,height=600,bg="#2c3e50")
        frame.place(x=500,y=10)      
        def update(data):
            lst.delete(0,END)
            for i in data:
                lst.insert(0,i)
        def fillout(e):
                search_entry.delete(0,END)
                search_entry.insert(0,lst.get(ACTIVE))
        def check(e):
            typed=search_entry.get()
            if typed=="":
                data=items
            else:
                data=[]
                for i in items:
                    if typed.lower()in i.lower():
                        data.append(i)
                        update(data)
        search=Label(frame,text="Comic World",bg="#2c3e50",fg="pink",font="times 25 bold")
        search.place(x=260,y=10)
        search_entry=Entry(frame,width=50,font="times 15",selectbackground="blue",selectforeground="black",fg="#0040ff")
        search_entry.place(x=100,y=80)
        lst=Listbox(frame,width=50,font="times 15 bold",fg="#0040ff")
        lst.place(x=100,y=150)
        items=["Kingdom Come","Oishinbo","Casper the Friendly Ghost","Dragon Ball","The Adventures of Tintin","Spike and Suzy","Main article: List of manhwa","Peanuts","Doraemon","Diabolik","Bleach"]
        update(items)
        lst.bind("<<ListboxSelect>>",fillout)
        search_entry.bind("<KeyRelease>",check)
        def search_info():
           se=search_entry.get()
           ent=wiki.summary(se,sentences=8)
           global s
           s=Tk()
           s.geometry("1980x1080")
           s.title(se)
           s.config(bg="sky blue")
           Label(s,text=se, font="times 25 bold",bg="sky blue").place(x=700,y=10)
           lab=Label(s,text=""+ent,font="times 15 bold",bg="sky blue",padx=10,pady=30,relief="raised",wrap="1200").place(x=250,y=50)
           b1=Button(s,text="Exit",font="times 15 bold",command=s.destroy,activebackground="red")
           b1.place(x=750,y=500)
        b=Button(frame,text="Search",font="times 15 bold",command=search_info,activebackground="green")
        b.place(x=320,y=400)
        b=Button(w,text="Logout",font="times 15 bold",command=signin,activebackground="red")
        b.place(x=1400,y=10)
    
def signin():
    w1=Tk()
    w1.geometry("1980x1080")
    w1.title("Comic World")
    w1.config(bg="Sky blue")
    frame2=Frame(w1,width=600,height=400,bg="#2c3e50")
    frame2.place(x=500,y=0)
    heading1=Label(frame2,text="Comic World",font="Arial 25 bold", fg="#ff0040",bg="#2c3e50")
    heading1.place(x=250,y=20)
    heading3=Label(frame2,text="SignIn",font="Arial 20 bold", fg="pink",bg="#2c3e50")
    heading3.place(x=290,y=80)
    uname1=Label(frame2,text="User Name:",font="Arial 15 bold", fg="pink",bg="#2c3e50")
    uname1.place(x=50,y=150)
    entry1=Entry(frame2,textvariable=username,width=20,font="Arial 15 bold")
    entry1.place(x=250,y=150)
    pw=Label(frame2,text="Password:",font="Arial 15 bold", fg="pink",bg="#2c3e50")
    pw.place(x=50,y=200)
    pw_entry=Entry(frame2,textvariable=password,width=20,show="*",font="Arial 15 bold")
    pw_entry.place(x=250,y=200)
    b=Button(frame2,text="Signin",font="Arial 13 bold", fg="pink",bg="#2c3e50",activebackground="green",command=search)
    b.place(x=290,y=280)
def main_screen():
    global screen
    global frame
    screen=Tk()
    screen.geometry("1980x1080")
    screen.title("Comic World")
    screen.config(bg="Sky blue")
    c = Canvas(screen, width=1990, height=800, bg='white')
    c.grid(row=2, column=3)
    img = ImageTk.PhotoImage(Image.open("image.jpg"))  
    c.create_image(0, 0, anchor=NW, image=img)
    frame=Frame(screen,width=800,height=800,bg="#8000ff")
    frame.place(x=910,y=0)
    global username
    global password
    global cpassword
    global uname
    global entry
    global psw_entry
    global psw1_entry
    username=StringVar()
    password=StringVar()
    cpassword=StringVar()
    heading=Label(frame,text="Comic World",font="Arial 25 bold", fg="#ff0040",bg="#8000ff")
    heading.place(x=240,y=20)
    heading2=Label(frame,text="SignUp",font="Arial 20 bold", fg="pink",bg="#8000ff")
    heading2.place(x=290,y=80)
    uname=Label(frame,text="User Name:",font="Arial 15 bold", fg="pink",bg="#8000ff")
    uname.place(x=50,y=150)
    entry=Entry(frame,textvariable=username,width=20,font="Arial 15 ")
    entry.place(x=250,y=150)
    psw=Label(frame,text="Create Password:",font="Arial 15 bold", fg="pink",bg="#8000ff")
    psw.place(x=50,y=200)
    psw_entry=Entry(frame,textvariable=password,width=20,show="*",font="Arial 15 bold")
    psw_entry.place(x=250,y=200)
    psw1=Label(frame,text="Conform Password:",font="Arial 15 bold", fg="pink",bg="#8000ff")
    psw1.place(x=50,y=260)
    psw1_entry=Entry(frame,textvariable=cpassword,width=20,show="*",font="Arial 15 bold")
    psw1_entry.place(x=250,y=260)
    b=Button(frame,text="Signup",font="Arial 13 bold", fg="pink",bg="#8000ff",activebackground="green",command=search)
    b.place(x=290,y=330)
    label=Label(frame,text="Already have account?",font="Arial 15 bold", fg="pink",bg="#8000ff")
    label.place(x=120,y=380)
    b1=Button(frame,text="Signin",font="Arial 13 bold", fg="pink",bg="#8000ff",activebackground="green",command=signin)
    b1.place(x=370,y=380)
    screen.mainloop()
main_screen()



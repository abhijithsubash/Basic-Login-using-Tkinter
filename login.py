from tkinter import *
from tkinter import messagebox
f = open('userinfo.txt','a+')
a = f.read()
g = a.splitlines()
j = []
for i in g:
    j.append(i.split('||'))
frame = Tk()
frame.geometry('400x550')
lbl1 = Label(frame, text='username')
lbl1.place(relx=0.2, rely=0.2, anchor=W)
lbl2 = Label(frame, text='password')
lbl2.place(relx=0.2, rely=0.3, anchor=W)
txt1 = Entry(frame)
txt1.place(relx=0.5, rely=0.2, anchor=W)
txt2 = Entry(frame, show='*', width=20)
txt2.place(relx=0.5, rely=0.3, anchor=W)


def clicked():
    txt = txt1.get()
    psw = txt2.get()
    if txt == 'admin' and psw == '1234':
            def clk():
                newwin.quit()
            newwin = Toplevel()
            newwin.geometry('400x550')
            display = Label(newwin, text="Welcome")
            display.place(relx=0.5, rely=0.4, anchor=CENTER)
            btn1 = Button(newwin, text='logout', command=clk)
            btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
    elif txt == '' and psw == '':
        messagebox.showwarning('no way')
    else:
        messagebox.showwarning('Message', "The username and password entered doesn't match")


btn = Button(frame, text='login', command=clicked)
btn.place(relx=0.4, rely=0.4, anchor=W)
frame.mainloop()
from tkinter import *
from connect.rs_t import fo_user, fr_user
from connect.rs_i import follow, followed_by


win = Tk()
win.title("rs-wallboard --- alpha 0.0.3")
win.geometry("1080x720")
win.minsize(800,600)
win.configure(bg='white')

frame    = Frame(win, bg='grey', bd=1, relief=SUNKEN, width='300')
frame2   = Frame(win, bg='yellow', bd=1, relief=SUNKEN, width='300')

frame5   = Frame(win, bg='blue', bd=1, relief=SUNKEN)

t_logo   = PhotoImage(file="./assets/twitter-logo.png")
i_logo   = PhotoImage(file="./assets/instagram.png")

t_pic    = Label(frame, image=t_logo, bg='white').pack()
t_label1 = Label(frame, text="Nombre de followers:", bg='white', fg='black',  font=("arial italic", 18)).pack()
t_data1  = Label(frame, text=fo_user, fg='black', bg='white', font=("arial italic", 16)).pack()
t_label2 = Label(frame, text="Nombre de follow:", bg='white', fg='black', font=("arial italic", 18)).pack()
t_data2  = Label(frame, text=fr_user, fg='black', bg='white', font=("arial italic", 16)).pack()


i_pic    = Label(frame2, image=i_logo, bg='white').pack()
i_label1 = Label(frame2, text="Nombre de followers:", bg='white', fg='black',  font=("arial italic", 18)).pack()
i_data1  = Label(frame2, text=followed_by, fg='black', bg='white', font=("arial italic", 16)).pack()
i_label2 = Label(frame2, text="Nombre de follow:", bg='white', fg='black', font=("arial italic", 18)).pack()
i_data2  = Label(frame2, text=follow, fg='black', bg='white', font=("arial italic", 16)).pack()


btn      = Button(frame5, text='Quitter', command=win.destroy).pack()

frame.pack(expand='YES')
frame2.pack(expand='YES')
frame5.pack(expand='YEs')
win.mainloop()
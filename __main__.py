from tkinter import *
from .connect.rs_t import fo_user, fr_user
from .connect.rs_i import follow, followed_by


win = Tk()
win.title("rs-wallboard --- alpha 0.0.5")
win.geometry("1280x400")
win.minsize(1080,300)
win.configure(bg='white')

bgcolor  = 'white'

frame    = Frame(win, bg=bgcolor)
frame2   = Frame(win, bg=bgcolor)
frame3   = Frame(win, bg=bgcolor)
frame4   = Frame(win, bg=bgcolor)

#logos
t_logo   = PhotoImage(file="rs-wallboard/assets/twitter.png")
i_logo   = PhotoImage(file="rs-wallboard/assets/instagram.png")
l_logo   = PhotoImage(file="rs-wallboard/assets/linkedin.png")
f_logo   = PhotoImage(file="rs-wallboard/assets/facebook.png")

#Twitter
t_pic    = Label(frame, image=t_logo, bg=bgcolor).pack()
t_label1 = Label(frame, text="Nombre de followers:", bg=bgcolor, fg='black',  font=("arial italic", 18)).pack()
t_data1  = Label(frame, text=fo_user, fg='black', bg=bgcolor, font=("arial italic", 16)).pack()
t_label2 = Label(frame, text="Nombre de follow:", bg=bgcolor, fg='black', font=("arial italic", 18)).pack()
t_data2  = Label(frame, text=fr_user, fg='black', bg=bgcolor, font=("arial italic", 16)).pack()

#Instagram
i_pic    = Label(frame2, image=i_logo, bg=bgcolor).pack()
i_label1 = Label(frame2, text="Nombre de followers:", bg=bgcolor, fg='black',  font=("arial italic", 18)).pack()
i_data1  = Label(frame2, text=followed_by, fg='black', bg=bgcolor, font=("arial italic", 16)).pack()
i_label2 = Label(frame2, text="Nombre de follow:", bg=bgcolor, fg='black', font=("arial italic", 18)).pack()
i_data2  = Label(frame2, text=follow, fg='black', bg=bgcolor, font=("arial italic", 16)).pack()

#Linkedin
l_pic    = Label(frame3, image=l_logo, bg=bgcolor).pack()
l_label1 = Label(frame3, text="Nombre de relations:", bg=bgcolor, fg='black',  font=("arial italic", 18)).pack()
l_data1  = Label(frame3, text=followed_by, fg='black', bg=bgcolor, font=("arial italic", 16)).pack()
l_label2 = Label(frame3, text="Nombre de vues:", bg=bgcolor, fg='black', font=("arial italic", 18)).pack()
l_data2  = Label(frame3, text=follow, fg='black', bg=bgcolor, font=("arial italic", 16)).pack()

#Facebook
f_pic    = Label(frame4, image=f_logo, bg='white').pack()
f_label1 = Label(frame4, text="Nombre d'amis:", bg='white', fg='black',  font=("arial italic", 18)).pack()
f_data1  = Label(frame4, text=fo_user, fg='black', bg='white', font=("arial italic", 16)).pack()
f_label2 = Label(frame4, text="Nombre de posts:", bg='white', fg='black', font=("arial italic", 18)).pack()
f_data2  = Label(frame4, text=fr_user, fg='black', bg='white', font=("arial italic", 16)).pack()


frame.pack(expand='YES', side=LEFT)
frame2.pack(expand='YES', side=LEFT)
frame3.pack(expand='YES', side=RIGHT)
frame4.pack(expand='YES', side=RIGHT)

win.mainloop()
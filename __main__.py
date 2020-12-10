from tkinter import *
from .connect.rs_t import fo_user, fr_user
from .connect.rs_i import follow, followed_by


win = Tk()
win.title("rs-wallboard --- alpha 0.0.3")
win.geometry("1280x400")
win.minsize(1080,300)
win.configure(bg='white')

frame    = Frame(win, bg='white')
frame2   = Frame(win, bg='white')
frame3   = Frame(win, bg='white')
frame4   = Frame(win, bg='white')

t_logo   = PhotoImage(file="rs-wallboard/assets/twitter-logo.png")
i_logo   = PhotoImage(file="rs-wallboard/assets/instagram.png")

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

'''
TESTS
'''
t_pic    = Label(frame3, image=t_logo, bg='white').pack()
t_label1 = Label(frame3, text="Nombre de followers:", bg='white', fg='black',  font=("arial italic", 18)).pack()
t_data1  = Label(frame3, text=fo_user, fg='black', bg='white', font=("arial italic", 16)).pack()
t_label2 = Label(frame3, text="Nombre de follow:", bg='white', fg='black', font=("arial italic", 18)).pack()
t_data2  = Label(frame3, text=fr_user, fg='black', bg='white', font=("arial italic", 16)).pack()

i_pic    = Label(frame4, image=i_logo, bg='white').pack()
i_label1 = Label(frame4, text="Nombre de followers:", bg='white', fg='black',  font=("arial italic", 18)).pack()
i_data1  = Label(frame4, text=followed_by, fg='black', bg='white', font=("arial italic", 16)).pack()
i_label2 = Label(frame4, text="Nombre de follow:", bg='white', fg='black', font=("arial italic", 18)).pack()
i_data2  = Label(frame4, text=follow, fg='black', bg='white', font=("arial italic", 16)).pack()

'''
FIN TESTS
'''

frame.pack(expand='YES', side=LEFT)
frame2.pack(expand='YES', side=LEFT)
frame3.pack(expand='YES', side=RIGHT)
frame4.pack(expand='YES', side=RIGHT)

win.mainloop()
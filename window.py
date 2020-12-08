from tkinter import *
from connect.rs_t import fo_user, fr_user
from connect.rs_i import follow, followed_by


win = Tk()
win.title("rs-wallboard --- alpha 0.0.2")
win.geometry("800x600")
win.configure(bg='white')


t_logo = PhotoImage(file="./assets/twitter-logo.png")
i_logo = PhotoImage(file="./assets/instagram.png")

t_pic = Label(win, image=t_logo, bg='white').pack(anchor="nw", padx=50, pady=10)

t_label1 = Label(win, text="Nombre de followers:", bg='white', fg='black',  font=("arial italic", 18)).pack(anchor='nw', padx=5, pady=5)
t_data1 = Label(win, text=fo_user, fg='black', bg='white', font=("arial italic", 16)).pack(anchor='nw', padx=80)
t_label2 = Label(win, text="Nombre de follow:", bg='white', fg='black', font=("arial italic", 18)).pack(anchor='nw', padx=5)
t_data2 = Label(win, text=fr_user, fg='black', bg='white', font=("arial italic", 16)).pack(anchor='nw', padx=80)


i_pic = Label(win, image=i_logo, bg='white').pack(anchor="nw", padx=50,pady=20)

i_label1 = Label(win, text="Nombre de followers:", bg='white', fg='black',  font=("arial italic", 18)).pack(anchor='w', padx=5, pady=5)
i_data1 = Label(win, text=followed_by, fg='black', bg='white', font=("arial italic", 16)).pack(anchor='w',padx=80)
i_label2 = Label(win, text="Nombre de follow:", bg='white', fg='black', font=("arial italic", 18)).pack(anchor='w', padx=5)
i_data2 = Label(win, text=follow, fg='black', bg='white', font=("arial italic", 16)).pack(anchor='w', padx=80)


btn = Button(win, text='Quitter', command = win.destroy).pack(anchor='s')

win.mainloop()
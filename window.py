from tkinter import *
from rs_t import fo_user, fr_user


win = Tk()
win.title("rs-wallboard --- alpha 0.0.1")
win.geometry("800x600")
t_label1= Label(win, text="Nombre de followers:", fg='black',  font=("arial italic", 18)).pack(anchor='nw', padx=5, pady=5)
t_data1 = Label(win, text=fo_user, fg='black', font=("arial italic", 16)).pack(anchor='nw', padx=5)
t_label2 = Label(win, text="Nombre de follow:", fg='black', font=("arial italic", 16)).pack(anchor='nw', padx=5)
t_data2 = Label(win, text=fr_user, fg='black', font=("arial italic", 16)).pack(anchor='nw', padx=5)


bou1 = Button(win, text='Quitter', command = win.destroy).pack(anchor='s')
win.mainloop()
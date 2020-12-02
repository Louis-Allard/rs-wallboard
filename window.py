from tkinter import *
from rs_t import fo_user, fr_user


win = Tk()
win.title("rs-wallboard --- alpha 0.0.1")
win.geometry("800x600")

t_label1= Label(win, text="Nombre de followers:", fg='black')
t_data1 = Label(win, text=fo_user, fg='black')
t_label2 = Label(win, text="Nombre de follow:", fg='black')
t_data2 = Label(win, text=fr_user, fg='black')

t_label1.pack()
t_data1.pack()
t_label2.pack()
t_data2.pack()

bou1 = Button(win, text='Quitter', command = win.destroy)
bou1.pack()
win.mainloop()
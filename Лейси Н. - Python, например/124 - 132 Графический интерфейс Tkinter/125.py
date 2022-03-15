import random
from tkinter import *


def click():
    dice_num = random.randint(1, 6)
    num_label = Label(win, text=f'You random dice number: {dice_num}')
    num_label.place(x=25, y=75, width=400, height=25)


win = Tk()
win.title('Random dice number')
win.geometry('450x200')

but = Button(text='Click Her', command=click)
but.place(x=25, y=25, width=400, height=25)
win.mainloop()




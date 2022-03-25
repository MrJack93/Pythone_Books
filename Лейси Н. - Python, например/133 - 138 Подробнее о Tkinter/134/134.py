import random
from tkinter import *


def verify():
    answer = num_2 + num_1
    num = int(lab_entry.get())
    if answer == num:
        lab_out['image'] = png_true
    else:
        lab_out['image'] = png_false
    lab_entry.delete(0, END)


def next_answer():
    global num_1, num_2
    num_1, num_2 = random.randint(10, 50), random.randint(10, 50)
    lab_1['text'] = f'{num_1} + {num_2}'


win = Tk()
win.wm_iconbitmap('code.ico')
win.title('Numbers games')
win.geometry('100x200')
win.config(bg='#C4C4C4')

num_1, num_2 = random.randint(10, 50), random.randint(10, 50)

lab_1 = Label(text=f'{num_1} + {num_2} ', bg='#C4C4C4')
lab_1.pack()

lab_entry = Entry(bg='#E5E5E5')
lab_entry.pack()
lab_entry['justify'] = 'center'
lab_entry['relief'] = 'ridge'

but = Button(text='Next', command=next_answer)
but.pack()
but['relief'] = 'ridge'

but1 = Button(text='Verify', command=verify)
but1.pack()
but1['relief'] = 'ridge'

png_true = PhotoImage(file='true.png')
png_false = PhotoImage(file='false.png')

lab_out = Label()
lab_out.pack()

win.mainloop()

from tkinter import *


def click():
    name = lab_entry.get()
    lab_out['text'] = f' Hello {name}'
    lab_entry.delete(0, END)


win = Tk()
win.wm_iconbitmap('code.ico')
win.title('Names')
win.geometry('600x400')
win.config(bg='#C4C4C4')

logo = PhotoImage(file='Union.png')
logo_image = Label(image=logo, bg='#C4C4C4')
logo_image.place(x=162, y=16, width=276, height=224)

lab_1 = Label(text='Enter your name:', bg='#C4C4C4')
lab_1.place(x=19, y=256, width=127, height=40)

lab_entry = Entry(bg='#E5E5E5')
lab_entry.place(x=162, y=256, width=422, height=40, )
lab_entry['justify'] = 'center'
lab_entry['relief'] = 'ridge'

but = Button(text='Press me', command=click)
but.place(x=19, y=336, width=127, height=40)
but['relief'] = 'ridge'

lab_out = Message(text='', bg='#E5E5E5')
lab_out.place(x=162, y=336, width=422, height=40, )
lab_out['justify'] = 'center'
lab_out['relief'] = 'ridge'

win.mainloop()

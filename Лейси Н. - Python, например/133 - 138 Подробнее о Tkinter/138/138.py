from tkinter import *


def click():
    name = in_box.get()
    in_box.delete(0, END)
    file_name = name + '.gif'
    photo['file'] = file_name


win = Tk()
win.wm_iconbitmap('code.ico')
win.title('Emoji')
win.geometry('400x400')
win.config(bg='#C4C4C4')

in_box = Entry()
in_box.pack()

but = Button(text='Click for select image', command=click)
but.pack()
but['relief'] = 'ridge'

photo = PhotoImage(file='1.gif')
photo_box = Label(win, image=photo)
photo_box.image = photo
photo_box.pack()

win.mainloop()

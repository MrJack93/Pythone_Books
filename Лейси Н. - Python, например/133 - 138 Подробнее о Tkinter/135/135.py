from tkinter import *


def click():
    sel = select_color.get()
    win.config(bg=sel)


win = Tk()
win.wm_iconbitmap('code.ico')
win.title('Color Change')
win.geometry('100x200')
win.config(bg='#C4C4C4')

but = Button(text='Click to change color', command=click)
but.pack()
but['relief'] = 'ridge'

select_color = StringVar(win)
select_color.set('Select color')

color_list = OptionMenu(win, select_color, "black", "red", "green")
color_list.pack()

win.mainloop()

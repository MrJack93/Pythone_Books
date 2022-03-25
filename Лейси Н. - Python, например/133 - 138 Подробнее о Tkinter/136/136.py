from tkinter import *


def click():
    name = in_box.get() + ', ' + select_sex.get()
    list_box.insert(END, name)
    in_box.delete(0, END)


win = Tk()
win.wm_iconbitmap('code.ico')
win.title('Names/Sex')
win.geometry('100x200')
win.config(bg='#C4C4C4')

in_box = Entry()
in_box.pack()

select_sex = StringVar(win)
select_sex.set('Select sex')

sex_list = OptionMenu(win, select_sex, "W", "M")
sex_list.pack()

but = Button(text='Click to add in list', command=click)
but.pack()
but['relief'] = 'ridge'

list_box = Listbox()
list_box.pack()

win.mainloop()

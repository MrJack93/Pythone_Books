from tkinter import *


def click():
    name = in_box.get() + ', ' + select_sex.get()
    list_box.insert(END, name)
    in_box.delete(0, END)


def save():
    name = list_box.get(0, END)
    with open('readme.txt', 'a') as f:
        f.writelines('\n'.join(name))


def view():
    with open('readme.txt', 'r') as f:
        print(f.read())


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

but2 = Button(text='Clear list', command=lambda: list_box.delete(0, END))
but2.pack()
but2['relief'] = 'ridge'

but3 = Button(text='Save to .txt', command=save)
but3.pack()
but3['relief'] = 'ridge'

but4 = Button(text='View in console', command=view)
but4.pack()
but4['relief'] = 'ridge'

list_box = Listbox()
list_box.pack()

win.mainloop()

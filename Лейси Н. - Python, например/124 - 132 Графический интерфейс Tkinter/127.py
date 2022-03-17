from tkinter import *


def but_add():
    name = box_input.get()
    list_box.insert(END, name.title())
    box_input.delete(0, END)
    box_input.focus()


def but_clear():
    list_box.delete(0, END)
    box_input.focus()


win = Tk()
win.title('Name list')
win.geometry('350x300')

label_1 = Label(text='Enter name for add in list:')
label_1.pack()

box_input = Entry()
box_input['justify'] = 'center'
box_input.pack()

but_1 = Button(text="Add to list", command=but_add)
but_1.pack()

but_2 = Button(text="Clear list", command=but_clear)
but_2.pack()

list_box = Listbox()
list_box.pack()

win.mainloop()

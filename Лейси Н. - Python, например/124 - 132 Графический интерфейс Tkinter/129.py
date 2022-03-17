from tkinter import *


def but_add():
    num = box_input.get()
    if num.isdigit():
        list_box.insert(END, num)
        box_input.delete(0, END)
    else:
        list_box.delete(0, END)
        box_input.delete(0, END)


win = Tk()
win.title('Num list integers')
win.geometry('300x300')

label_1 = Label(text='Enter num for add in list:')
label_1.pack()

box_input = Entry()
box_input['justify'] = 'center'
box_input.pack()

but_1 = Button(text="Add to list", command=but_add)
but_1.pack()

but_2 = Button(text="Clear list", command=lambda: list_box.delete(0, END))
but_2.pack()

list_box = Listbox()
list_box.pack()

win.mainloop()

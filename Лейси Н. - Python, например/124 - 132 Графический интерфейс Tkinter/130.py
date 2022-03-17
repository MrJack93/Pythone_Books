from tkinter import *


def but_add():
    num = box_input.get()
    if num.isdigit():
        list_box.insert(END, num)
        box_input.delete(0, END)
    else:
        list_box.delete(0, END)
        box_input.delete(0, END)


def save_csv():
    tmp = list_box.get(0, END)
    file = open('save_num.csv', 'w')
    count = 0
    for i in tmp:
        new_record = tmp[count] + '\n'
        file.write(str(new_record))
        count += 1
    file.close()
    label_4 = Label(text='Record Saved')
    label_4.pack()


win = Tk()
win.title('Num list integers')
win.geometry('300x300')

label_1 = Label(text='Enter num for add in list:')
label_1.pack()

box_input = Entry()
box_input['justify'] = 'center'
box_input.pack()

but_1 = Button(text="Add to list",
               command=but_add)
but_1.pack()

but_2 = Button(text="Clear list",
               command=lambda: list_box.delete(0, END))
but_2.pack()

but_3 = Button(text="Save to .csv",
               command=save_csv)
but_3.pack()

list_box = Listbox()
list_box.pack()

win.mainloop()

from tkinter import *
import csv


def create_csv():
    file = open('name_age.csv', 'w')
    new_record = 'Name, Age\n'
    file.write(str(new_record))
    file.close()


def save_csv():
    name = box_input_name.get()
    age = box_input_age.get()
    file = open('name_age.csv', 'a')
    new_record = f'{name}, {age}\n'
    file.write(str(new_record))
    file.close()
    box_input_age.delete(0, END)
    box_input_name.delete(0, END)


def open_csv():
    file = open('name_age.csv', 'r')
    tmp_list = []
    for info in file:
        tmp_list.append(info)
    index = 0
    for i in tmp_list:
        data = tmp_list[index]
        list_box.insert(END, data)
        index += 1



win = Tk()
win.title('Name and age to CSV')
win.geometry('300x350')

label_name = Label(text='Enter name')
label_name.pack()

box_input_name = Entry()
box_input_name['justify'] = 'center'
box_input_name.pack(pady=10)

label_age = Label(text='Enter age')
label_age.pack()

box_input_age = Entry()
box_input_age['justify'] = 'center'
box_input_age.pack(pady=10)

but_1 = Button(text="Create new CSV",
               command=create_csv)
but_1.pack(pady=10)

but_2 = Button(text="Add to CSV",
               command=save_csv)
but_2.pack(pady=10)

but_3 = Button(text="open.csv",
               command=open_csv)
but_3.pack(pady=10)

list_box = Listbox()
list_box.pack(pady=10)

win.mainloop()

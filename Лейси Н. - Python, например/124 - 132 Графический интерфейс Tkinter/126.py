from tkinter import *


def click_sum():
    num = input_box.get()
    num = int(num)
    answer = out_message['text']
    answer = int(answer)
    total = num + answer
    out_message['text'] = total


def click_restart():
    pass


num = 0
rest = 0

win = Tk()
win.title('Sum number input')
win.geometry('450x300')

in_label = Label(text='Enter number for sum:')
in_label.place(x=25, y=25, width=400, height=25)

input_box = Entry(text=0)
input_box.place(x=150, y=75, width=150, height=25)
input_box['justify'] = 'center'
input_box.focus()

but_sum = Button(text='Click to sum', command=click_sum)
but_sum.place(x=185, y=125, width=80, height=25)

out_label = Label(text=f'Answer = {num}')
out_label.place(x=175, y=225, width=100, height=25)

out_message = Message(text=0)
out_message.place(x=175, y=250, width=100, height=25)

but_restart = Button(text='Click to restart', command=click_restart)
but_restart.place(x=175, y=175, width=100, height=25)


win.mainloop()

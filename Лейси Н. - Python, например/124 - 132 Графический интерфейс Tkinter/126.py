from tkinter import *


def click_sum():
    global num
    num_in = int(input_box.get())
    total = num_in + num
    out_label['text'] = f'Answer : {num} + {num_in} = {total}'
    num = total


def click_restart():
    global num
    num = rest
    out_label['text'] = f'Answer : {num} '


num = 0
rest = 0

win = Tk()
win.title('Sum number input')
win.geometry('450x300')

in_label = Label(text='Enter number for sum:')
in_label.pack()

input_box = Entry()
input_box['justify'] = 'center'
input_box.pack()


but_sum = Button(text='Click to sum', command=click_sum)
but_sum.pack()


but_restart = Button(text='Click to restart', command=click_restart)
but_restart.pack()

out_label = Label(text=f'Answer = {num}')
out_label.pack()

win.mainloop()

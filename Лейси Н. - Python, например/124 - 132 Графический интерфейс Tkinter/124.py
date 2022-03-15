from tkinter import *


def call():
    num = entry_box.get()
    label_hello = Label(window, text=f'Hello {num} !')
    label_hello.place(x=30, y=125, width=200, height=25)
    label_hello['bg'] = 'red'
    label_hello['fg'] = 'white'


window = Tk()
window.title('Hello!')
window.geometry('260x200')

entry_box = Entry()
entry_box.place(x=30, y=75, width=200, height=25)
entry_box['justify'] = 'center'

button = Button(text='Enter your name and press me ', command=call)
button.place(x=30, y=25, width=200, height=25)

window.mainloop()

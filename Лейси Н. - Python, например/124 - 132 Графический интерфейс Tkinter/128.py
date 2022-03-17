from tkinter import *


def to_km():
    km = int(in_box.get())
    miles = km * 1.6093
    label_2['text'] = f'{km} Km in miles: {miles}'
    in_box.delete(0, END)


def to_miles():
    miles = int(in_box.get())
    km = miles * 0.6214
    label_2['text'] = f'{miles} miles in Km: {km}'
    in_box.delete(0, END)


win = Tk()
win.title('Km, mills converter')
win.geometry('250x150')

label_1 = Label(text='Enter value for convert:')
label_1.pack()

in_box = Entry()
in_box['justify'] = 'center'
in_box.pack()

but_km = Button(text='To Km', command=to_km)
but_km.pack()

but_miles = Button(text='To Miles', command=to_miles)
but_miles.pack()

label_2 = Label(text='')
label_2.pack()

win.mainloop()

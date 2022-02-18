
import csv

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    print(f' {x + 1} - {tmp[x]}')
    x = x + 1

del_row = int(input('Enter row number to delete: '))
tmp.remove(tmp[del_row - 1])

y = 0
for row in tmp:
    print(f' {y + 1} - {tmp[y]}')
    y = y + 1

edit_row = int(input('Enter row number to edit: '))
tmp.remove(tmp[edit_row - 1])

title = input('Enter title: ')
author = input('Enter new name: ')
year = input('Enter new earth: ')
new_record = [title + ', ' + author + ', ' + year]

tmp.insert((edit_row - 1), new_record)

file = open('Books.csv', 'w')

for data in range(len(tmp)):
    new_record = str(data) + '\n'
    file.write(str(new_record))
file.close()

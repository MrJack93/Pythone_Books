import csv

file = open('Books.csv', 'a')
title = input('Enter title: ')
author = input('Enter new name: ')
year = input('Enter new earth: ')
new_record = title + ', ' + author + ', ' + year + '\n'
file.write(str(new_record))
file.close()

file = open('Books.csv', 'r')
for row in file:
    print(row)
file.close()

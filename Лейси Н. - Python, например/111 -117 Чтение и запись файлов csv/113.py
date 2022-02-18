
import csv

in_data = int(input('How much data row you input? '))

for i in range(0, in_data):
    file = open('Books.csv', 'a')
    title = input('Enter title: ')
    author = input('Enter new author: ')
    year = input('Enter new year: ')
    new_record = title + ', ' + author + ', ' + year + '\n'
    file.write(str(new_record))
    file.close()


file = open('Books.csv', 'r')
search = input('Enter author: ')
reader = csv.reader(file)
count = 0
for row in file:
    if search in str(row):
        print(row)
        count += 1
if count == 0:
    print('There are no books by this author ')


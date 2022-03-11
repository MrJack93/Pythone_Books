import csv

menu = '1) Add to file''\n' \
       '2) View all records''\n' \
       '3) Delete record''\n' \
       '4) Quit program''\n'

tmp = []
file_data = list(csv.reader(open('Salaries.csv')))
for row in file_data:
    tmp.append(row)


def add():
    name = str.title(input('Enter name: '))
    salaries = input('Enter salaries: ')
    tmp.append([name, salaries])


def view():
    num = 1
    for i in tmp:
        print(f'{num}: {i}')
        num += 1


def delete():
    view()
    del_rec = int(input('Select number for delete: '))
    del tmp[del_rec - 1]


def save():
    file_data_save = open('Salaries.csv', 'w')
    x = 0
    for a in tmp:
        new_rec = f'{tmp[x][0]}, {tmp[x][1]}\n'
        file_data_save.write(new_rec)
        x += 1
    file_data_save.close()


try_again = True
while try_again:
    print(menu)
    selection = int(input('Enter the number of your selection: '))
    if selection == 1:
        add()
    elif selection == 2:
        view()
    elif selection == 3:
        delete()
    elif selection > 4:
        print('Error selection')
    else:
        save()
        print('Program quit')
        try_again = False


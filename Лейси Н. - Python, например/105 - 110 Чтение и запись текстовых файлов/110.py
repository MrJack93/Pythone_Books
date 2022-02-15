
file = open('106_Names.txt', 'r')
print(file.read())
file.close()

file = open('106_Names.txt', 'r')
selectedname = input('Enter selected name: ')
selectedname = selectedname + '\n'
for row in file:
    if row != selectedname:
        file = open('110_Names.txt', 'a')
        new_rec = row
        file.write(new_rec)
        file.close()
file.close()


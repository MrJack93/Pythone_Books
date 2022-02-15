
file = open('109_Subject.txt', 'w')
file.write('History\n')
file.close()
print('1) Create a new file\n2) Display the file\n3) Add a new item to the file')
select = int(input('Make a selection 1, 2 or 3: '))
while select > 3:
    print('(Error) Try again')
    select = int(input('Make a selection 1, 2 or 3: '))
if select == 1:
    subject = str.title(input('Enter school subject: '))
    file = open('109_Subject.txt', 'w')
    file.write(f'{subject}\n')
    file.close()
elif select == 2:
    file = open('109_Subject.txt', 'r')
    print(file.read())
else:
    subject = str.title(input('Enter school new subject: '))
    file = open('109_Subject.txt', 'a')
    file.write(f'{subject}\n')
    file.close()
    file = open('109_Subject.txt', 'r')
    print(file.read())

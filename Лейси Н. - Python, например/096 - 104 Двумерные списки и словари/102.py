
data = {}
for i in range(0, 4):
    name = str.title(input('Enter name: '))
    age = int(input('Enter age: '))
    size = int(input('Enter size chose: '))
    data[name] = {'Age': age, 'Size': size}
print(data)
name_in = str.title(input('Enter selected name: '))

print(f'Your selected data: {name_in} {data[name_in]}')

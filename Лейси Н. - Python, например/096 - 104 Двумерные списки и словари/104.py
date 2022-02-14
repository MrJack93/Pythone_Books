
data = {}
for i in range(0, 2):
    name = str.title(input('Enter name: '))
    age = int(input('Enter age: '))
    size = int(input('Enter size chose: '))
    data[name] = {'Age': age, 'Size': size}

name_del = str.title(input('Enter name for delete: '))
del data[name_del]

for name in data:
    print('Name:', name, 'Age:', data[name]['Age'], 'Size chose', data[name]['Size'])

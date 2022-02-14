
data = {}
for i in range(0, 2):
    name = str.title(input('Enter name: '))
    age = int(input('Enter age: '))
    size = int(input('Enter size chose: '))
    data[name] = {'Age': age, 'Size': size}

print(data)

for name in data:
    print('Name:', name, 'Age: ', data[name]['Age'])


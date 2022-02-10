name = str.title(input('Enter your name: '))
count = 0
for i in name.lower():
    if i == 'a' or i == 'o' or i == 'u' or i == 'i' or i == 'e' or i == 'y':
        count += 1
print(f'Voles in {name} - {count}')

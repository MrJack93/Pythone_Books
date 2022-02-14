
data_sale = {'John': {'N': 3846, 'S': 8463, 'E': 8441, 'W': 2694},
             'Toma': {'N': 4432, 'S': 6784, 'E': 4737, 'W': 3622},
             'Anna': {'N': 5229, 'S': 4802, 'E': 5820, 'W': 1859},
             'Maya': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}

print(data_sale)

name = str.title(input('Enter name: '))
region = str.title(input('Enter region: '))

print(f'Your data: {data_sale[name][region]}')

new_data_sale = int(input('Enter new data: '))
data_sale[name][region] = new_data_sale

print(f'Your new data: {data_sale[name]}')

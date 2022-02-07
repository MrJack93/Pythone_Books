
friends_list = []
for friend in range(1, 4):
    friends_input = friends_list.append(str(input(f'Enter friend number {friend}: ')))
question = 'Yes'
while question == 'Yes':
    question = str.title(input('Would you like to add another name? '))
    if question == 'No':
        break
    friends_input = friends_list.append(str(input('Enter friend: ')))
print(f'You have, {len(friends_list)} coming to party')

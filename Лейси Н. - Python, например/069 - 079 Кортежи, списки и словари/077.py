
friends_list = []
for friend in range(1, 4):
    friends_input = friends_list.append(str.title(input(f'Enter friend number {friend}: ')))
question = 'Yes'
while question == 'Yes':
    question = str.title(input('Would you like to add another name? '))
    if question == 'No':
        break
    friends_input = friends_list.append(str.title(input('Enter friend: ')))
print(f'You have, {len(friends_list)} friends coming to party')
print(f'Your list friends: {friends_list}')
question = str.title(input('Enter one of the names in the list: '))
friend_index = friends_list.index(question)
print(f'Friend index: {friend_index}')
friends_del = str.title(input('Do you want this person to attend the party? '))
if friends_del == 'No':
    del friends_list[friend_index]
print(f'Your list friends: {friends_list}')

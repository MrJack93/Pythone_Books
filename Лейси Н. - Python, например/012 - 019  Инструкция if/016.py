
raning = str.lower(input('Is it raining? '))
if raning == 'yes':
    windy = str.lower(input('is it windy outside? '))
    if windy == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')

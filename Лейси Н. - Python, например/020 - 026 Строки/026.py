
word = input('Enter a word to convert: '.lower())
if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    convert_word = word.strip(word[0]) + 'way'
    print(convert_word)
else:
    print(word.strip(word[0]) + word[0] + 'ay')

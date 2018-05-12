word = str(input('Введите слово:'))
new_word = ''
if word =='':
    print ('Ведена пустая строка')
else:
    for i in range(int(len(word)/2)):
        new_word += word[i]
    for i in range(len(word)-1, int(len(word)/2)-1, -1):
        new_word += word[i]
    print(new_word)

word = str(input('Введите слово:'))
new_word = ''
if word =='':
    print ('Введена пустая строка')
else:
    new_word = ''
    for i in range(len(word)):
        new_word = word[-i-1] + new_word
        print (new_word)
    
        
    

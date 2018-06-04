words = []
hints = {}

with open('words.csv') as file:
	for line in file:
		line = line.strip()
		word_and_hints = line.split(',')
		word = word_and_hints[0]
		cur_hints = word_and_hints[1:]
		words.append(word)
		hints[word] = cur_hints

import random

word = random.choice(words)
cur_hints = hints[word]
hint = random.choice(cur_hints)

print('Угадайте слово на месте "...":')
print(hint)
print()

attempts = 0

while True:
	print('Попыток сделано:', attempts)
	print()
	print('Введите слово: ', end='')
	guess = input()
	attempts += 1
	if guess == word:
		print('Вы угадали!')
		print('Использовано попыток:', attempts)
		break
	else:
		print('Неверно, попробуйте её раз')
		print()


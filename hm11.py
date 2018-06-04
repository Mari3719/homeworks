import re

with open('eat.txt', encoding='utf-8') as file:
	text = file.read()

# https://ru.wiktionary.org/wiki/%D1%81%D1%8A%D0%B5%D1%81%D1%82%D1%8C
pattern = r'\b(съе)(м|шь|ст|дим|дите|дят|л|ла|ло|ли|в|вши|вший|денный)\b'

matches = re.findall(pattern, text)

words = []

for match in matches:
	word = ''.join(match)
	if not(word in words):
		words.append(word)

for word in words:
	print(''.join(word))


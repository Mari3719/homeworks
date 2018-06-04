import re

sentences = []

with open('input.txt', encoding='utf-8') as file:
	for line in file:
		line_sentences = re.split('[.?!]', line)
		for sentence in line_sentences:
			sentence = sentence.strip()
			if len(sentence) > 0:
				sentence = re.sub('[,:;-]', '', sentence)
				sentences.append(sentence)

def change_word(word):
	new_word = [letter * word.count(letter) for letter in word]
	return ''.join(new_word)

def change_sentence(sentence):
	words = [change_word(word) for word in sentence.split(' ')]
	return ' '.join(words)
	
sentences = [change_sentence(s) for s in sentences]

with open('output.txt', 'w', encoding='utf-8') as file:
	for sentence in sentences:
		file.write(sentence + '\n')

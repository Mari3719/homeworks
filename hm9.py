def ask_filename():
	filename = input('Введите название файла: ')
	return filename

def words_from_file(filename):
	with open(filename, encoding='utf-8') as f:
		text = f.read()
		words = text.split()
		for i in range(len(words)):
			words[i] = words[i].replace(',', '').replace('.', '').replace('?', '').replace('!', '')
		return words

def words_lengths(words):
	lengths = {}
	for word in words:
		if word[-3:] == 'ous':
			l = len(word)
			lengths[word] = l
	return list(lengths.values())

def average(lengths):
	sum = 0
	for l in lengths:
		sum += l
	return sum / len(lengths)

filename = ask_filename()
words = words_from_file(filename)
lenghts = words_lengths(words)

count = len(lenghts)
avg = average(lenghts)

print('Различных слов на -ous:', count)
print('Их среднаяя длина:', avg)


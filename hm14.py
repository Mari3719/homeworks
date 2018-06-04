import os
import re

dirs = []
files = []
i = 0

for path in os.listdir():
	if os.path.isdir(path):
		dirs.append(path)
		words = re.findall(r'\w+', path)
		if len(words) > 1:
			i = i + 1
	elif os.path.isfile(path):
		files.append(path)

print('Число папок, название которых состоит из более чем одного слова, равно %i' % i)
print()
print('Все файлы и папки, находящиеся в текущей папке:')
for path in dirs:
	print(path)
for path in files:
	print(path)

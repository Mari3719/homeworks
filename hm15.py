import os

names = []

for root, dirs, files in os.walk('.'):
	for file in files:
		name, ext = os.path.splitext(file)
		if not(name in names):
			names.append(name)

print('Разных названий файлов без учёта расширений: %i' % len(names))

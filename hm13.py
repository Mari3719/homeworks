import re

with open('input.txt', encoding='utf-8') as file:
	text = file.read()
	
pattern = r'\b(динозавр)(|а|ам|ах|е|ами|ов|ом|у|ы)\b'
replacement = r'кот\2'

text = re.sub(pattern, replacement, text)

pattern = r'\b(Динозавр)(|а|ам|ах|е|ами|ов|ом|у|ы)\b'
replacement = r'Кот\2'

text = re.sub(pattern, replacement, text)

with open('output.txt', 'w', encoding='utf-8') as file:
	file.write(text)

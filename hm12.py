
import re

with open('Томат.txt', encoding='utf-8') as file:
	text = file.read()

pattern = r'<tr><td.*?>Семейство.*?</td><td.*?><a.*?>(.*?)</a></td></tr>'

match = re.search(pattern, text)

if match:
	kind = match.group(1)
	print(kind)
else:
	print('Не найдено')


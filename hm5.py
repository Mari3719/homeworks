with open('text.txt', encoding = 'utf-8') as f:
     text = f.read()
symbols_to_remove = ',.:;!?"-()' 
for s in symbols_to_remove: 
     text = text.replace (s, '')
words = text.split()
count_words = 0
count = 0
for i in words:
     count_words +=1
     symbols = list(i)
     k = 0
     for x in symbols:
         k += 1
     if k>10:
         count += 1
rocent = count/count_words*100
print (procent, '%')

         

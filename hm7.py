import random

def noun(): 
    with open ('nouns.txt',encoding='utf-8') as f: 
        text = f.read() 
        nouns = text.split(',') 
        result = random.choice(nouns) 
    return result

def verb(): 
    with open ('verbs.txt',encoding = 'utf-8') as f: 
        text = f.read() 
        verbs = text.split(',') 
        result = random.choice(verbs)
        if (result[-3:] == 'еть') or (result[-3:] == 'ать')or (result[-3:] == 'ять'):
            result = result[:-2]+'ет'
        elif result[-2:] == 'ся':
            result = result[:-4]+'ется'
        else:
            result = result[:-2]+'ит'
    return result

def union(): 
    with open ('unions.txt',encoding = 'utf-8') as f: 
        text = f.read() 
        unions = text.split(',') 
        result = random.choice(unions) 
    return result

def excuse(): 
    with open ('excuses.txt',encoding = 'utf-8') as f: 
        text = f.read() 
        excuses = text.split(',') 
        result = random.choice(excuses)
    return result

def object():
    result = noun()
    if result[-1:] == 'a':
        result = result[:-1]+'y'
    elif result[-1:] == 'я':
        result[-1:] == 'ю'
    return result

for x in range(5):
    subj1 = noun()
    verb1 = verb()
    exc1 = excuses()
    obj1 = object()
    sentence1 = subj1+' '+verb1+' '+exc1+' '+obj1+', '
    conj = union()
    subj2 = noun()
    verb2 = verb()
    exc2 = excuses()
    obj2 = object()
    sentence2 = subj2+' '+verb2+' '+exc2+' '+obj2+'.'
    sentence = sentence1+conj+' '+sentence2
    print(sentence)

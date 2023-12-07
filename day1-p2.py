import re 

f = open("input.txt", "r")
s = f.readlines()

def returnNum(s): 
    if s == 'one':
        return '1'
    elif s == 'two':
        return '2'
    elif s == 'three':
        return '3'
    elif s == 'four':
        return '4'
    elif s == 'five':
        return '5' 
    elif s == 'six': 
        return '6'
    elif s == 'seven':
        return '7'
    elif s == 'eight':
        return '8'
    elif s == 'nine':
        return '9' 
    elif s == 'zero':
        return '0'
    
digit = ['1','2','3','4','5','6','7','8','9','0']
num = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

condi = digit + num

r = 0 

for l in s:
    temp = ''
    indexes = []
    numFound = []
    for i in condi:
        for index in re.finditer(i, l):
            indexes.append(index.start())
            numFound.append(i)
    first = numFound[indexes.index(min(indexes))]
    last = numFound[indexes.index(max(indexes))]
    if first in num: 
        temp += returnNum(first)
    elif first in digit: 
        temp += first
    
    if last in num: 
        temp += returnNum(last)
    elif last in digit: 
        temp += last
    
    print(temp)
    
    r+=int(temp)

print (r)


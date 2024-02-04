import re

f = open('input.txt', 'r')

s = f.readlines()

numeric = '[1-9][0-9]*' 
symbol = '[^.0-9]'      

r = 0

for i in range(len(s)):
    numIndex = []
    prevSym = []
    currSym = []
    nextSym = []
    if i == 0: 
        for n in re.finditer(numeric,s[i].strip()):
            numIndex.append(n)
        for sym in re.finditer(symbol,s[i].strip()):
            currSym.append(sym.start())
        for sym in re.finditer(symbol, s[i+1].strip()):
            nextSym.append(sym.start())
    elif i == (len(s)-1):
        for n in re.finditer(numeric,s[i].strip()):
            numIndex.append(n)
        for sym in re.finditer(symbol,s[i].strip()):
            currSym.append(sym.start())
        for sym in re.finditer(symbol, s[i-1].strip()):
            prevSym.append(sym.start())
    else: 
        for n in re.finditer(numeric,s[i].strip()):
            numIndex.append(n)
        for sym in re.finditer(symbol,s[i].strip()):
            currSym.append(sym.start())
        for sym in re.finditer(symbol, s[i-1].strip()):
            prevSym.append(sym.start())
        for sym in re.finditer(symbol,s[i+1].strip()):
            nextSym.append(sym.start())
    #print(prevSym)
    #print(currSym)
    #print(nextSym)
    for e in numIndex:
        if e.start()-1 in currSym or e.end() in currSym:
            
            r += int(e.group())
        for sym in prevSym:
            if sym >= e.start()-1 and sym <= e.end():
                
                r += int(e.group())
        for sym in nextSym:
            if sym >= e.start()-1 and sym <= e.end():
                
                r += int(e.group())
    
print(r)
import re
f = open('test.txt', 'r')
s = f.readlines()
winning = []
holding = []

r = 0
for l in s:
    temp = l[9:].split('|')
    winning = temp[0]
    holding = temp[1]

    wincondi = winning.strip()
    winnum = re.sub(' +', ' ',wincondi).split(' ')
    hand = holding.strip()
    handnum = re.sub(' +', ' ',hand).split(' ')
    print(wincondi)
    print(hand)
    count = 0
    for num in handnum:
        if num in winnum:
            count += 1
    print('count:', count)
    if count > 0:
        r += pow(2, count - 1)
print(r)


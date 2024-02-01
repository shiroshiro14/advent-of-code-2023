import re
f = open('test.txt', 'r')
s = f.readlines()
winning = []
holding = []
wincount = {}
cardCount = {}
def checkWinning(l):
    temp = l[9:].split('|')
    winning = temp[0]
    holding = temp[1]

    wincondi = winning.strip()
    winnum = re.sub(' +', ' ',wincondi).split(' ')
    hand = holding.strip()
    handnum = re.sub(' +', ' ',hand).split(' ')

    count = 0
    for num in handnum:
        if num in winnum:
            count += 1
    wincount[s.index(l)] = count

def checkCardCount():
    for key, value in wincount.items():
        for i in range(value):
            cardCount[key + i + 1] += cardCount[key]
    #print(cardCount)
def totalCard():
    r = 0
    for key, value in cardCount.items():
        r += value
    print('final: ', r)
for l in s:
    checkWinning(l)
    cardCount[s.index(l)] = 1
checkCardCount()
totalCard()
#print(wincount)


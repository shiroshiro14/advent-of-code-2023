f = open('test.txt', 'r')
s = f.read()[:-1]

r = []
def mapProcess(islandMap):
    temp = islandMap.split('\n')
    final = temp[1:]
    return final

islandMap = s.split("\n\n")

for seed in islandMap[0][7:].split(' '):
    x = float(seed)
    for mapping in islandMap[1:] :
        temp = mapProcess(mapping)
        print(temp)
        for line in temp:
            coordinate = line.strip().split(' ')
            destination = float(coordinate[0])
            source = float(coordinate[1])
            delta = float(coordinate[2])
            if x < (source + delta) and x > source:
                x += destination - source
                break
    r.append(x)

print(min(r))


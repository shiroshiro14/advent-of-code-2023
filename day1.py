f = open("input.txt", "r")
s = f.readlines()
r = 0 
for l in s:
    t = ''
    for c in l: 
        if (c.isdigit()): 
            t += c 
            break 
    for c in reversed(l): 
        if (c.isdigit()):
            t += c
            break 
    r += int(t)

print(r)

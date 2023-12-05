f = open("input.txt", "r")
s = f.readlines()


red = 12
green = 13 
blue = 14


r = 0
games = []
for l in s:  
    i = l.find(":")
    games.append(l[(i+2):].split("; "))

for game in games: 
    r += (games.index(game) + 1)
    for attempt in game:
        red_count = 0
        blue_count = 0
        green_count = 0 
        for i in attempt.split(", "):
            if "red" in i: 
                red_ball = int(i[:i.find("red")-1])
                red_count += red_ball
            if "blue" in i:
                blue_ball = int(i[:i.find("blue")-1])
                blue_count += blue_ball
            if "green" in i: 
                green_ball = int(i[:i.find("green")-1])
                green_count += green_ball
        
        if red_count > red or blue_count > blue or green_count > green:  
            r -= (games.index(game)+1)
            break 


print(r)


#12 red, 13 green, 14 blue
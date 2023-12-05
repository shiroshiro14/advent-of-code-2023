f = open("input.txt", "r")
s = f.readlines()

r = 0
games = []
for l in s:  
    i = l.find(":")
    games.append(l[(i+2):].split("; "))

for game in games: 
    max_red = 0
    max_blue = 0 
    max_green = 0
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
        
        max_red = red_count if red_count > max_red else max_red
        max_blue = blue_count if blue_count > max_blue else max_blue
        max_green = green_count if green_count > max_green else max_green
    r += (max_green * max_blue * max_red) 


print(r)


#12 red, 13 green, 14 blue
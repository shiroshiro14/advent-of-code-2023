s = "3 red, 3 blue, 3 green"
colors = s.split(",")
red = 0
blue = 0
green = 0

for i in colors:
    i = int(i)
    if "red" in i:
        red += 1
    elif "blue" in i:
        blue += 1
    elif "green" in i:
        green +=

input_file = open("input.txt")
text_data = input_file.read()

data = text_data.split(", ")

x, y = 0,0
previous_points = [(0,0)]
direction = 0 #0=up,1=left,2=down,3=right

for i in data:
    if i[0] == "R":
        direction -= 1
    else:
        direction += 1

    direction = direction % 4
    moveAmount = int(i[1:])

    for j in range(moveAmount):
        if direction == 0:
            y += 1
        elif direction == 1:
            x -= 1
        elif direction == 2:
            y -= 1
        else:
            x += 1

        if (x,y) in previous_points:
            print(str(abs(x)+abs(y)))
            exit()

        previous_points.append((x,y))

input_file = open("input.txt")
input_data = input_file.read()
input_file.close()

keypad_numbers = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

x = 1
y = 1

fullCombo = ""

for i in input_data.split("\n"):
    if i == "":
        break
    for j in i:
        if j == "U" and y > 0:
            y -= 1
        elif j == "L" and x > 0:
            x -= 1
        elif j == "R" and x < 2:
            x += 1
        elif j == "D" and y < 2:
            y += 1
    fullCombo += str(keypad_numbers[y][x])

print(fullCombo)

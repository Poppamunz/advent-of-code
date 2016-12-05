input_file = open("input.txt")
input_data = input_file.read()
input_file.close()

keypad_numbers = [
[" "," ","1"," "," "], #this is godawful, but i really don't care
[" ","2","3","4"," "],
["5","6","7","8","9"],
[" ","A","B","C"," "],
[" "," ","D"," "," "]
]

x = 0
y = 2

fullCombo = ""

for i in input_data.split("\n"):
    if i == "":
        break
    for j in i:
        if j == "U" and y > 0 and keypad_numbers[y-1][x] != " ":
            y -= 1
        elif j == "L"  and x > 0 and keypad_numbers[y][x-1] != " ":
            x -= 1
        elif j == "R" and x < 4 and keypad_numbers[y][x+1] != " ":
            x += 1
        elif j == "D" and y < 4 and keypad_numbers[y+1][x] != " ":
            y += 1
    fullCombo += keypad_numbers[y][x]

print(fullCombo)

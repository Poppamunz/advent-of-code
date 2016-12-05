input_file = open("input.txt")
input_data = input_file.read()
input_file.close()

triangles = []

triangleCounter = 0

for i in input_data.split("\n"):
    temporary_triangle = []
    if i == "":
        break
    
    for j in i.split():
        temporary_triangle.append(int(j))
    triangles.append(sorted(temporary_triangle))

for i in triangles:
    if i[0] + i[1] > i[2]:
        triangleCounter += 1

print(str(triangleCounter))

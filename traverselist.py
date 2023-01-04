colorlist = []
repeat = "Y"
while repeat == "Y":
    color = input("Enter a color: ")
    colorlist.append(color)
    repeat = input("Do you want to add another color?(Y/N): ")
for i in range(len(colorlist)):
    print(i, colorlist[i])
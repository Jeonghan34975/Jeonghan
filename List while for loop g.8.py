colorlist = []
repeat = "Y"
while repeat == "Y":
    color = input("Enter a color: ")
    colorlist.append(color)
    repeat = input("Do you want to add another?(Y/N) ")
print(colorlist)
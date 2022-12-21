colorlist = []

while len(colorlist) < 5:
    color = input("Enter a color: ")
    colorlist.append(color)

    for color in colorlist:
        print(color)
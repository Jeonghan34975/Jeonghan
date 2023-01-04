teamlist = []
repeat = "Y"
while repeat == "Y":
    name = input("Enter a name: ")
    teamlist.append(name)
    repeat = input("Do you want to add another name?(Y/N): ")
for i in range(len(teamlist)):
    print(i, teamlist[i])
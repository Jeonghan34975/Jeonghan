football_team = []
repeat = "Y"
while repeat == "Y":
    name = input("Enter the player's name: ")
    football_team.append(name)
    repeat = input("Do you enter another name(Y/N): ")
print(football_team)
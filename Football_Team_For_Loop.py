football_team = []
number = input("How many nmaes of players do you want?: ")
number = int(number)
for i in range(number):
    name = input("Enter the name pf the players: ")
    football_team.append(name)
print(football_team)
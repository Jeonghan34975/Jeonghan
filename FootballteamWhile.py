football_team = []
for i in range(11):
    name = input("Add the name of players: ")
    football_team.append(name)
print(football_team)

repeat = 'y'
while repeat == 'y':
    edit = int(input('Which player do you want to change?: '))
    football_team[edit-1] = input('Enter a new player: ')
    print(football_team)
    
    delete = int(input('Which player do you want to delete?: '))
    del football_team[delete-1]
    print(football_team)
    repeat = input('Do you want to edit or delete name(y/n): ')
print(football_team)
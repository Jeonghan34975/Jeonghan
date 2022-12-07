football_team = []
#append values
for i in range(11):
    name = input("Add the name of players: ")
    football_team.append(name)
repeat = 'y'
while repeat == 'y':
    #edit an item
    print(football_team)
    #identify the range of indexes
    final_index = len(football_team)
    print("You can print any name from the list. Index numbers go from 0 to", final_index)
    i = input("Which name do tou want to change?")
    i = int(i)
    #Validation with while loop
    while i >= len(football_team):
        i = int(input("Enter correct number: "))
    football_team[i] = input("Enter a new name: ")
    print(football_team)

    #delete an item
    print("You can delete any name from the list. Index numbers go from 0 to", )
    i = input("Which name do you want to delete?: ")
    #Validation
    while i >=len(football_team)
    i = int(input("Enter a correct number: "))
    del football_team[i]
    print(football_team)
    repeat = input("do you want to edit or delete more names?(y/n): ")
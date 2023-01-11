#Program interface should have all of these:
#1. Tell the user what the program is and what it can do.
#2. Tell the user to make choices or select option.
#3. Let the user enter the information. -you  should include a helpful message and validation.
#4. Display result or answer.
#5. Let the user to close the program.

teamlist = []
choice = ' '
while choice != 'X':
    print("TEAM MANAGER")
    print("============")
    print("This program will help you to manage your team")
    print("\n")
    print("A: Append a value")
    print("B: Print the teamlist")
    print("C: Print an element")
    print("D: Delete an element")
    print("E: Edit an element")
    print("F: Sort the list")
    print("X: Exit the program")
    choice = input("Enter your choice: ")
    if choice == "A":
        name = input("Enter a name: ")
        teamlist.append(name)
    if choice == "B":
        print(teamlist)
    if choice == "C":
        i = int(input("Which list item do you want to print?: "))
        print(teamlist[i-1])
    if choice == "D":
        delete = int(input("Which list item do you want to delete?: "))
        del(teamlist[delete-1])
    if choice == "E":
        edit = int(input("Which list item do you want to edit?: "))
        teamlist[edit-1] = input("Enter the new name: ")
        print(teamlist)
    if choice == "F":
        teamlist.sort()
        print(teamlist)
    if choice == "X":
        print("Exiting the program")
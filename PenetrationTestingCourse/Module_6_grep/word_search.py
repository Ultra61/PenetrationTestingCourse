check = True
while(check):
    string = input("enter the string that you would like to look for: ")
    path = input("enter the absolute path of the file including the file name and extension: ")
    with open(path) as file:
        if string in file.read():
            print("The string is in the file")
        else:
            print("The string is NOT in the file")
    go_again = input("Would you like to search again? (yes to continue): ")
    if go_again != 'yes':
        check = False
    
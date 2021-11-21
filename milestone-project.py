def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

display(row1,row2,row3)
##[' ', ' ', ' ']
##[' ', ' ', ' ']
##[' ', ' ', ' ']

row2[1] = 'x'

display(row1,row2,row3)

#[' ', ' ', ' ']
#[' ', 'x', ' ']
#[' ', ' ', ' ']

###### ACCEPTING USER INPUT


input("Please enter a value: ")

result = input("Please enter a value: ")

## input function returns a string so you may need to convert it as so:
## int(result)

#Validate user input

def user_choice():
    choice = input("Please enter a number (0-10:) ")

    return int(choice)

user_choice()
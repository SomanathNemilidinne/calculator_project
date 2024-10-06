def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

logo = """
 _____________________
|  _________________  |
| | Python   80085. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
calculator = {"+": add, "-": subtract, "*": multiply, "/": divide}
# print((calculator["*"](8, 4)))
#You can define a function called calculator_operation and at the last if-else condition calling it again
#It will also create a recursive while loop without while function
#well i wanted to have a easter egg in my code so i did it with nested while loop 😁😜
four_twenty = 69
while four_twenty < 420:
    print(logo)
    first_number = float(input("What's the first number?  "))
    if first_number == 8008569420:
        print("Ahh So you got out of the loop, Congratulations!")
        break
    continue_operation = True
    while continue_operation:
        operator = input("+\n"
                         "-\n"
                         "*\n"
                         "/\n"
                         "Pick an operation:   ")
        second_number = float(input("What's the next number?  "))
        if operator in calculator:
            answer = calculator[operator](first_number, second_number)
            print(f"{first_number} {operator} {second_number} = {answer}")
        else:
            print("You've given invalid symbol, DUMBO!")
        continuation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if continuation == "n":
            continue_operation = False
            print("\n" * 25)
        else:
            first_number = int(answer)
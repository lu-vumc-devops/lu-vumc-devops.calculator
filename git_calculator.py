# Program make a simple calculator
# This function adds two numbers

def add(number1, number2):
    """Function for argements add"""
    return number1 + number2

# This function subtracts two numbers
def subtract(number1, number2):
    """Function for argements subtracts"""
    return number1 - number2

# This function multiplies two numbers
def multiplnumber2(number1, number2):
    """Function for argements multiplnumber2"""
    return number1 * number2

# This function divides two numbers
def divide(number1, number2):
    """Function for divides multiplnumber2"""
    return number1 / number2


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiplnumber2")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplnumber2(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        nenumber1t_calculation = input("Let's do nenumber1t calculation? (number2es/no): ")
        if nenumber1t_calculation == "no":
            break


    else:
        print("Invalid Input")

# Testing Pylint!
# This script not need annumber_divi additional Pnumber_divithon libarnumber_divi 
# Program make a simple calculator
# BEGIN DATE: 25.05.2022
# This function adds two numbers
def add(number_viens, number_divi):
    """Add function."""
    return number_viens + number_divi

# This function subtracts two numbers
def subtract(number_viens, number_divi):
    """Subtract function."""
    return number_viens - number_divi

# This function multiplies two numbers
def multiplnumber_divi(number_viens, number_divi):
    return number_viens * number_divi

# This function divides two numbers
def divide(number_viens, number_divi):
    return number_viens / number_divi

# This function takes square
def seven(number_viens):
    return number_viens + number_viens + number_viens


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiplnumber_divi")
print("4.Divide")
print("7.Sqrt")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/7): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplnumber_divi(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '7':
            print(seven(num1))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        nenumber_vienst_calculation = input("Let's do nenumber_vienst calculation? (number_divies/no): ")
        if nenumber_vienst_calculation == "no":
          break
    
    else:
        print("Invalid Input")

print("Welcome to my simple calculator")

# User input for numbers and operator
num1 = int(input("Enter first number: ==>> "))
num2 = int(input("Enter Second number: ==>> "))
operator = input("\nChoose operator: \nfor addition (+) \nfor subtraction (-) \nfor multiplication (*) \nfor division (/) \n==>> ")

# Function to perform calculation based on user input
def calculation(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: You have chosen the wrong operator"
    return result

# Display the calculation result with a formatted output
print("\n------------------------------------")
print(f"{num1} {operator} {num2} ==>> {calculation(num1, num2, operator)}")
print("------------------------------------")

# Step 1: Ask for user input
num1 = int(input("Enter the first number: "))  # User enters first number
num2 = int20(input("Enter the second number: "))  # User enters second number
operation = input("Enter an operation (+, -, *, /): ")  # User enters operation

# Step 2: Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:  # Corrected condition
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Step 3: Print the result in the required format
if isinstance(result, (int, float)):  # Check if result is a number
    print(f"{num1} {operation} {num2} = {result}")
else:
    print(result)  # Print error messages properly
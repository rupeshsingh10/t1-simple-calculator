print("Welcome to Simple Calculator")

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation choices
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user's choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation based on choice
if choice == '1':
    result = num1 + num2
    print("Result: ", result)
elif choice == '2':
    result = num1 - num2
    print("Result: ", result)
elif choice == '3':
    result = num1 * num2
    print("Result: ", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")

import functions

print("What do you want to do?")
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

choice = input('Enter your choice (1-4): ')

try:
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    # Use defined functions for calculations
    if choice == '1':
        result = functions.addition(num1, num2)
    elif choice == '2':
        result = functions.subtraction(num1, num2)
    elif choice == '3':
        result = functions.multiplication(num1, num2)
    elif choice == '4':
        result = functions.division(num1, num2)
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        result = None  # Indicate error

    if result is not None:
        print(f"{num1} {choice.replace('.', '')} {num2} = {result}")  # Clearer output formatting
except ValueError:
    print("Invalid input. Please enter valid numbers.")
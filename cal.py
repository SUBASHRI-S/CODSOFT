import math

# Function definitions for basic and advanced operations

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero"
        result /= num
    return result

def power(numbers):
    base = numbers[0]
    exponent = numbers[1]
    return base ** exponent

def square_root(numbers):
    result = []
    for num in numbers:
        if num < 0:
            result.append("Error: Imaginary number")
        else:
            result.append(math.sqrt(num))
    return result

def logarithm(numbers):
    base = numbers[0]
    number = numbers[1]
    return math.log(number, base)

def sine(numbers):
    result = []
    for num in numbers:
        result.append(math.sin(num))
    return result

def cosine(numbers):
    result = []
    for num in numbers:
        result.append(math.cos(num))
    return result

def tangent(numbers):
    result = []
    for num in numbers:
        result.append(math.tan(num))
    return result

# Main calculator function
def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")

    # Get user input
    choice = input("Enter your choice (1-10): ")

    if choice in ['6', '7', '8', '9', '10']:
        numbers = []
        numbers_count = int(input("Enter the number of values you want to calculate: "))
        for i in range(numbers_count):
            numbers.append(float(input(f"Enter number {i+1}: ")))
    else:
        numbers = []
        for i in range(2):
            numbers.append(float(input(f"Enter number {i+1}: ")))

    # Perform calculation based on user choice
    if choice == '1':
        result = add(numbers)
        operation = "+"
    elif choice == '2':
        result = subtract(numbers)
        operation = "-"
    elif choice == '3':
        result = multiply(numbers)
        operation = "*"
    elif choice == '4':
        result = divide(numbers)
        operation = "/"
    elif choice == '5':
        result = power(numbers)
        operation = "^"
    elif choice == '6':
        result = square_root(numbers)
        operation = "√"
    elif choice == '7':
        result = logarithm(numbers)
        operation = "log"
    elif choice == '8':
        result = sine(numbers)
        operation = "sin"
    elif choice == '9':
        result = cosine(numbers)
        operation = "cos"
    elif choice == '10':
        result = tangent(numbers)
        operation = "tan"
    else:
        print("Invalid input. Please enter a valid operation choice (1-10).")
        return

    # Print the result
    if isinstance(result, list):
        for i, res in enumerate(result):
            print(f"{operation}({numbers[i]}) = {res}")
    else:
        print(f"{operation}({', '.join(map(str, numbers))}) = {result}")

# Call the scientific calculator function to start the program
scientific_calculator()

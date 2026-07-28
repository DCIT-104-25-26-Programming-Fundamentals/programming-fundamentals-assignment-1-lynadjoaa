def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)

def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b

def exponentiate(a, b):
    return a ** b

def show_menu():
    print("\n==============================")
    print(" SIMPLE CALCULATOR")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

def main():
    while True:
        show_menu()
        choice = input("Select an operation (1-7): ")
        
        if choice == "7":
            print("Goodbye!")

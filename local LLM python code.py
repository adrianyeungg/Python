# Define a function to calculate the sum of two numbers
def add_numbers(a, b):
    return a + b

# Define a function to calculate the product of two numbers
def multiply_numbers(a, b):
    return a * b

# Create a message prompting the user to enter their choice and numbers
print("Enter your choice: 'add' for addition or 'multiply' for multiplication.")
try:
    # Read the user's input
    choice = input().strip().lower()

    if choice == "add":
        print("Please enter two numbers:")
        try:
            a, b = map(int, input().split())
            print(f"{a} + {b} = {add_numbers(a, b)}")
        except ValueError:
            print("Invalid input. Please try again.")
    elif choice == "multiply":
        print("Please enter two numbers:")
        try:
            a, b = map(int, input().split())
            print(f"{a} * {b} = {multiply_numbers(a, b)}")
        except ValueError:
            print("Invalid input. Please try again.")
except ValueError:
    print("Invalid choice. Please type 'add' or 'multiply'.")

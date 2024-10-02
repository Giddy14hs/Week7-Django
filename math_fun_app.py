# Function to add two numbers

def Sum():

    try:

        # Ask for two numbers from the user

        num1 = float(input("Enter the first number: "))

        num2 = float(input("Enter the second number: "))

       

        # Perform the addition

        result = num1 + num2

       

        # Display the result

        print(f"The sum of {num1} and {num2} is {result}")

       

    except ValueError:

        print("Please enter valid numbers.")

# Function to multiply two numbers

def Product():

    try:

        # Ask for two numbers from the user

        num1 = float(input("Enter the first number: "))

        num2 = float(input("Enter the second number: "))

       

        # Perform the multiplication

        result = num1 * num2

       

        # Display the result

        print(f"The product of {num1}and {num2}is {result}")

       

    except ValueError:

        print("Please enter valid numbers.")

 

# Example usage

if __name__ == "__main__":

    Sum()      # Calls the Sum function

    Product()  # Calls the Product function
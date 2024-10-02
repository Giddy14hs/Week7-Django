# Function to add two numbers (modified for testability)

def Sum(num1, num2):
  return num1 + num2

# Function to multiply two numbers (modified for testability)

def Product(num1, num2):
  return num1 * num2


# Example usage
if __name__ == "__main__":
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  print(f"The sum of {num1} and {num2} is {Sum(num1, num2)}")
  print(f"The product of {num1} and {num2} is {Product(num1, num2)}")
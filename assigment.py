# defininig operation to take 2 numbers as input
def math_operations(a, b):
    """
    Performing mathematical operations on two numbers.
    
    I use:
    a) float: First number.
    b) float: Second number.
    
    printing returned Results:
    tuple: A tuple containing the sum and product of the two numbers.
    """
    # lambda functions for sum and product
    sum = lambda a, b: a + b
    product = lambda a, b: a * b
    
    # Calculate sum and product using lambda functions
    sum =sum(a, b)
    product = product(a, b)
    
    return sum, product

# creating a main function that calls the math_operations function
def main():
    # Get input from the user
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    # Perform math operations
    sum, product = math_operations(a, b)
    
    # Print results
    print(f"Sum of {a} and {b} is: {sum}")
    print(f"Product of {a} and {b} is: {product}")

# Call the main function to execute the program
main()

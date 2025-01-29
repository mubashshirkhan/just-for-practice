# A simple function that prints a greeting
def greet():
    print("Hello, world!")

# A function that takes a name as an argument and prints a personalized greeting
def greet_person(name):
    print(f"Hello, {name}!")

# A function that takes two numbers and returns their sum
def add_numbers(a, b):
    return a + b

# A function that calculates the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# A function that checks if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
if __name__ == "__main__":
    greet()
    greet_person("Alice")
    print(f"Sum of 3 and 5 is: {add_numbers(3, 5)}")
    print(f"Factorial of 5 is: {factorial(5)}")
    print(f"Is 7 a prime number? {'Yes' if is_prime(7) else 'No'}")
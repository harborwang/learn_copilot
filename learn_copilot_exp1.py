# a function that prints "Hello, World!" to the console.
def hello():
    print("Hello, World!")
    
hello()

# a functiion that adds two numbers.
def add(a, b):
    return a + b

print(add(1, 2))

# a function that finds the roots of a quadratic equation.
def find_roots(a, b, c):
    # calculate the discriminant
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        return -b / (2 * a)
    else:
        # find two solutions
        x1 = (-b - D ** 0.5) / (2 * a)
        x2 = (-b + D ** 0.5) / (2 * a)
        return x1, x2
    
print(find_roots(10, 22, -28))


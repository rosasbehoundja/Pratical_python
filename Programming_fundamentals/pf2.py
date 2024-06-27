# a function to generate the Fibonacci sequence up to n terms

def fbn(x):
    fib = 1
    if x == 0:
        return "Please enter a non null integer"
    elif x == 1:
        fib = [0]
    elif x == 2:
        fib = [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, x):
            fib.append(fib[i-1] + fib[i-2])
    
    return f"Fibonacci sequence for {x} terms: {fib}"

def fibonacci(x):
    if isinstance(x, int):
        return fbn(x)
    else:
        return f"Please enter a valid input!"
    
print(fibonacci(10))


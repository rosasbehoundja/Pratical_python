# a program to check if a number is even or odd.

def odd_or_even(x):
    if isinstance(x, int):
        if x % 2 == 0:
            return f"{x} is even! Did you know that 2 is the only even number that is prime ?"
        else :
            return f"Oh sorry! {x} is an odd number"
    else : 
        return f"Your input must be an integrer"
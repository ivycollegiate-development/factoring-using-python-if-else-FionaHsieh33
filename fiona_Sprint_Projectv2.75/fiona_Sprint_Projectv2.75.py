# List all of the factors of a value
def list_factors(n):
    # Explain the line of code below
    return [i for i in range (1, n+1) if n % i == 0]
    # Comment your explination here
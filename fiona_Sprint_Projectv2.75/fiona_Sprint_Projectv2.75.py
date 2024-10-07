# List all of the factors of a value
def list_factors(n):
    # Explain the line of code below
    return [i for i in range (1, n+1) if n % i == 0]
    # This will take whatever number we put in and check for factors using a list

if _name_ == '_main_': #Checks to see if the applicationa is running locally
    # Ask the user for a number
    user_input = input('Please enter a number here: ')

try:
    # Convert that user input to an interger
    number = int(user_input)
    factors = list_factors(number)
    # Print the factors of the input value
    Print(f'The factors of {number} are {factors}')
else:
    # Get the factors for that value input
    factors = list_factors(number)
    # Print the factors of the input value
    Print(f'The factors of {number} are {factors}')
except valueError:
    #Handles the exception negative values or 0
    print('That is an invalid number. Please input a posiyive interger.')
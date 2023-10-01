def getintinput(p, e):
    """
    Purpose: Get an input from a user and convert it to an integer, if it is not a positive natural number above 2,
    return an error message and quit the program
    Pre - conditions: p: A string to prompt the user with
    e: A string to display if the input does not meet criteria
    Post - conditions: The function will print the "p" string and ask the user for input, and may display an error
    message and quit the program
    Return: Returns the user inputted integer if criteria is met
    """
    number = input(p)

    try:
        number = int(number)
    except ValueError:
        print(e)
        quit()

    if number > 2:
        return number
    else:
        print(e)
        quit()

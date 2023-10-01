import random


def pimidapprox(n):
    """
    Purpose: Approximates pi using midpoint approximation of area under semicircle
    Pre - conditions: n: Integer number of sub-intervals to approximate with
    Post - conditions:
    Return: Returns floating-point approximation of pi
    """
    pi = 0
    x = -1
    dx = 2/n
    # Sum all the rectangles of height at a point in the semicircle and width dx
    for i in range(0, n):
        pi += dx * 2 * (1 - ((x + x + dx)/2) ** 2) ** (1/2)
        x += dx
    return abs(pi)


def pitrapapprox(n):
    """
    Purpose: Approximates pi using trapezoidal approximation of area under semicircle (this is partially unnecessary as
    the function being approximation is a semicircle so L approx = R approx = T approx)
    Pre - conditions: n: Integer number of sub-intervals to approximate with
    Post - conditions:
    Return: Returns floating-point approximation of pi
    """
    pil = 0
    pir = 0
    x = -1
    dx = 2/n
    for i in range(0, n):
        # Find left endpoint approximation
        pil += 2 * dx * ((1 - x ** 2) ** (1/2))
        x += dx
    x = -1
    for i in range(0, n):
        # Find right endpoint approximation
        pir += 2 * dx * ((1 - (x + dx) ** 2) ** (1/2))
        x += dx
    # Return the average of the two approximations
    return abs(0.5 * (pil + pir))


def pisimpapprox(n):
    """
    Purpose: Approximate pi using Simpson's rule
    Pre - conditions: n: Integer to approximate with (will be doubled)
    Post - conditions:
    Return: Returns floating-point value of Simpson's approximation of pi using 2 * n sub - intervals
    """
    # Combine the two prior approximations using Simpson's rule ratios
    return abs(((2 * pimidapprox(n)) + pitrapapprox(n)) / 3)


def leibniz(n):
    """
    Purpose: Approximate pi using the Leibniz formula
    Pre - conditions: n: Integer number of desired steps of formula to complete
    Post - conditions:
    Return: Returns floating-point approximation of pi using leibniz formula
    """
    pi = 0
    for i in range(n):
        pi += (-1) ** i/(2 * i + 1)
    return pi * 4


def monte_carlo_pi(n):
    """
    Purpose: Approximate pi using Monte Carlo method
    Pre - conditions: n: Integer number of random points to use
    Post - conditions:
    Return: Returns floating-point approximation of pi using Monte Carlo method with n random points
    """
    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
    return 4 * count/n

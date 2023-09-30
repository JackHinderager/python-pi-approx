# python-pi-approx
This program uses five methods to approximate pi, midpoint approximation of the area of
a semicircle of radius 1, trapezoidal approximation of this semicircle, and a combination of the two in a
Simpson’s approximation. Leibniz approximator for pi is also included as it is considered the most simple
way to calculate the constant. The Monte Carlo method was also implemented. =I did
not import math, numpy, or any similar libraries as I wanted to work under some constraints.
# Usage
When main.py is run with a Python 3 interpreter in a console, it will prompt the user to enter a
number “n”. This number represents the number of iterations the program will use for each method to
approximate pi, the higher the number, the closer to pi you will get, but the program will require more time
and memory.
Upon entering a value for “n”, the program may have to load for a moment depending on the size
of “n”. After loading is complete the user will see three graphs:
Figure 1: The approximation of each method as they use higher and higher “n” values up until the value
specified by the user.
Figure 2: The time each calculation took as “n” gets higher and higher, note that this can be impacted by
other processes running on the system but generally show a linear trend upward as “n” enters the triple
digits.
Figure 3: This graph attempts to visualize the process of trapezoidal approximation of the area of a
semicircle, the black vertical lines represent subdivisions with distance dx between them. The shaded
blue area is the area calculated with trapezoidal integration. The orange line shows the actual location of
the semicircle bounds.
## Note
This program is not intended to calculate pi efficiently. I made it to visualize different methods of
finding pi and compare them with metrics of both accuracy and time. The best way to use this program is
to first enter values in the double digits and work up from there. As the number of subdivisions of the
semicircle grows, the semicircle may appear black, you can use the magnifying glass tool to zoom in and
see these smaller divisions.

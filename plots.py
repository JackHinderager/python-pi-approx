import matplotlib.pyplot as plt
import approximation as app
import time as t


def plotapprox(n):
    """
    Purpose: - Plots the approximations of pi using trapezoidal, midpoint, and Simpson's approximation of the area of a
    semicircle along with the output of a Leibniz formula and the Monte Carlo method
    - Generates a graph of a semicircle with n sub - divisions and a trapezoidal approximation overlay to visualise
    approximated area
    - Generates a graph of calculation time for all five approximation methods
    Pre - conditions: n: integer, number of sub-intervals, summation steps, and random points to complete approximations
     with
    Post - conditions: Displays a graph as described and outputs the values of each approximation at their highest
    "n" and displays a plot of the semicircle with approximation intervals marked out, also displays a
    graph of time for each calculation of pi for each method
    Return:
    """

    # Tell the user that the program is loading
    print("loading...")

    # Get the approximation data and time data lists ready
    xaxis = []
    ytrap = []
    ymid = []
    ysimp = []
    yleib = []
    ymont = []
    pi = []

    traptime = []
    midtime = []
    simptime = []
    leibtime = []
    monttime = []

    for i in range(1, n):
        xaxis.append(i)

        # Time each calculation
        start = t.time()
        ytrap.append(app.pitrapapprox(i))
        traptime.append(t.time() - start)

        start = t.time()
        ymid.append(app.pimidapprox(i))
        midtime.append(t.time() - start)

        start = t.time()
        ysimp.append(app.pisimpapprox(i))
        simptime.append(t.time() - start)

        start = t.time()
        yleib.append(app.leibniz(i))
        leibtime.append(t.time() - start)

        start = t.time()
        ymont.append(app.monte_carlo_pi(i))
        monttime.append(t.time() - start)

        pi.append(3.14159265359)

    print("The simpsons approximation of pi at ", 2 * n, " sub-intervals is ", ysimp[-1])
    print("The trapezoidal approximation of pi at ", n, " sub-intervals is ", ytrap[-1])
    print("The midpoint approximation of pi at ", n, " sub-intervals is ", ymid[-1])
    print("The Leibniz formula approximation of pi at ", n, " repetitions is ", yleib[-1])
    print("The Monte Carlo method approximation of pi at ", n, " random points is ", ymont[-1])

    fig, ax = plt.subplots()
    ax.plot(xaxis, ytrap, label='Trapezoidal Approximation')
    ax.plot(xaxis, ymid, label='Midpoint Approximation')
    ax.plot(xaxis, ysimp, label="Simpsons Approximation")
    ax.plot(xaxis, yleib, label="Leibniz Approximation")
    ax.plot(xaxis, ymont, label="Monte Carlo Approximation")
    ax.plot(xaxis, pi, label='Pi')

    ax.legend(loc='lower right')
    plt.ylabel("Approximated value of Pi")
    plt.xlabel('"n" value')

    plt.figure(1)

    # Plot time required for each calculation
    fig, ax = plt.subplots()
    ax.plot(xaxis, traptime, label='Trapezoidal Approximation Time')
    ax.plot(xaxis, midtime, label='Midpoint Approximation Time')
    ax.plot(xaxis, simptime, label="Simpsons Approximation Time")
    ax.plot(xaxis, leibtime, label="Leibniz Approximation Time")
    ax.plot(xaxis, monttime, label="Monte Carlo Approximation Time")

    ax.legend(loc='upper left')
    plt.ylabel("Calculation Time (seconds)")
    plt.xlabel('"n" value')

    plt.figure(2)

    # Get the semicircle ready
    yaxis = []
    xaxis = []
    semiy = []
    semix = []

    i = -1
    dx = 2 / n

    while i <= 1.000000001:
        xaxis.append(i)
        yaxis.append(abs((1 - (i ** 2)) ** (1 / 2)))
        i += dx

    i = -1
    dx = 0.000001

    while i <= 1.000000001:
        semix.append(i)
        semiy.append((abs((1 - (i ** 2)) ** (1 / 2))))
        i += dx

    fig, ax = plt.subplots()
    ax.plot(xaxis, yaxis)
    ax.plot(semix, semiy)
    ax.vlines(xaxis, ymin=0, ymax=yaxis, color='black')

    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    ax.set_aspect(abs((xright - xleft) / (ybottom - ytop)) * 0.5)
    ax.fill_between(xaxis, yaxis, 0, color='blue')

    plt.figure(3)

    # Display the plots
    plt.show()

import input as ask
import plots as plot

x = ask.getintinput('Please enter the "n" you would like to approximate up to: ',
                    "Oops! Please enter an integer above 3.")

plot.plotapprox(x)

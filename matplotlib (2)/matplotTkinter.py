# import all classes/methods
# from the tkinter module
from tkinter import *
from matplotlib.figure import Figure
# call the back matplotlib modules which will show the plot on the tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
def plot():
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    # list of squares
    y = [i ** 2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
# The main tkinter window
window = Tk()

# setting the title and
window.title('Plotting in Tkinter')

# setting the dimensions of
# the main window
window.geometry("500x500")

# button that would displays the plot
plot_button = Button(master = window,
					height = 2,
					width = 10,
					text = "Plot",
                     command=plot)
# place the button
# into the window
plot_button.pack()

# run the gui
window.mainloop()




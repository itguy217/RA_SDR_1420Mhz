#     Python SDR - Radio Astronomy
#     Author: Todd Chevrier - Citizen Scientist
#     Description: This code is for radio astronomers 
#     that want to give Raspbery Pi 4 a try
# ***This code requires a USB SDR Dongle in order to work properly ***
# ***You will need to install the proper modules listed below ***
# ***This script provides a baseline in which you will need to calibrate on your system. ***
###############################################
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import numpy as np
import re

from tkinter import *
from tkinter import filedialog

#Pi Desktop location - You can change this location
initialdir = '/home/pi/Desktop/'

#no need to change anything here as it gets overwritten
filename = 'obs.cvs'



def run():
    string = open(filename).read()
    new_Line = re.sub('\d+:\d+:\d+,\s\d{0,4}$', '', string)

    open('Fobs.csv', 'w').write(new_Line)

    I020 = [ line.strip('\n').split(",") for line in open('Fobs.csv')][1:]
      
    Time = [datetime.datetime.strptime(line[0],"%H:%M:%S") for line in I020]
    Time1 = [mdates.date2num(line) for line in Time]
        
    RadioData = [float(line[1]) for line in I020]


    xs = np.array(Time1)  # You don't really need to do this but I've left it in
    ys = np.array(RadioData)

    fig, ax = plt.subplots(figsize=(30,14)) # using matplotlib's Object Oriented API
    fig.patch.set_facecolor('xkcd:mint green')
    fig.canvas.set_window_title('Python SDR - Radio Astronomy Viewing Data')
    
    ax.set_xlabel('Time')
    ax.set_ylabel('Intensity')
    ax.plot_date(xs, ys, 'k-')
    ax.set_facecolor('xkcd:cream')

    hfmt = mdates.DateFormatter('%H:%M:%S')
    ax.xaxis.set_major_formatter(hfmt)
    plt.title(filename)
    plt.gcf().autofmt_xdate()
    plt.grid()
    plt.gca().get_lines()[0].set_color("red")
    plt.show()


# Function for opening the
# file explorer window
def browseFiles():
    global filename
    global initialdir
    filename = filedialog.askopenfilename(initialdir = initialdir, title = "Select a File",filetypes = (("CSV files","*.csv*"),("all files","*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

# Create the root window
window = Tk()

# Set window title
window.title('Python File Explorer')

# Set window size
window.geometry("600x170")

#Set window background color
window.config(background = "lightgray")

# Create a File Explorer label
label_file_explorer = Label(window,text = "Python Tkinter File Explorer",width = 65, height = 4,fg = "blue")

button_explore = Button(window,text = "Browse Files",command = browseFiles)
button_open = Button(window,text = "Open File",command=lambda: run())
button_exit = Button(window,text = "EXIT",command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_open.grid(column = 1,row = 3)

button_exit.grid(column = 1,row = 4)

# Let the window wait for any events
window.mainloop()
os.sys.exit(0)

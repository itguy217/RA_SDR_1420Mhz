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

string = open('obs.csv').read()
new_Line = re.sub('\d+:\d+:\d+,\s\d{0,4}$', '', string)

open('Fobs.csv', 'w').write(new_Line)

I020 = [ line.strip('\n').split(",") for line in open('Fobs.csv')][1:]
  
Time = [datetime.datetime.strptime(line[0],"%H:%M:%S") for line in I020]
Time1 = [mdates.date2num(line) for line in Time]
    
RadioData = [float(line[1]) for line in I020]


xs = np.array(Time1)  # You don't really need to do this but I've left it in
ys = np.array(RadioData)

fig, ax = plt.subplots() # using matplotlib's Object Oriented API
fig.patch.set_facecolor('xkcd:mint green')
ax.set_title('RA data')
ax.set_xlabel('Time')
ax.set_ylabel('Intensity')
ax.plot_date(xs, ys, 'k-')
ax.set_facecolor('xkcd:cream')

hfmt = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(hfmt)
plt.gcf().autofmt_xdate()
plt.grid()
plt.gca().get_lines()[0].set_color("red")
plt.show()
#     Python SDR - Radio Astronomy
#     Author: Todd Chevrier - Citizen Scientist
#     Description: This code is for radio astronomers 
#     that want to give Raspbery Pi 4 a try
# ***This code requires a USB SDR Dongle in order to work properly ***
###############################################
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from rtlsdr import RtlSdr
import numpy as np
from matplotlib.gridspec import GridSpec

# configure device
sdr = RtlSdr()
sdr.sample_rate = 2.4e6  # Hz
sdr.center_freq = 1420e6  # Hz
sdr.freq_correction = 1   # PPM
sdr.gain = 'auto'

#Configure grid plot
fig = plt.figure('Python SDR - Radio Astronomy',figsize=(30,14))
gs = GridSpec(2,2, height_ratios=[1.5, 1])

#graph_out = fig.add_subplot(1,1,1)
ax1 = fig.add_subplot(gs[1,:])
ax2 = fig.add_subplot(gs[0,:])

#Create realtime graph and display
def animate(i):
    
    #graph_out.clear()
    ax1.clear()
    ax2.clear()
    
    #samples = sdr.read_samples(128*1024) This is where you would add to database
    # Inputting data from the signal received from the feedhorn
    samples = sdr.read_samples(1024*1024)

    # use matplotlib to estimate and plot the PSD   (matplotlib.pyplot.)
    # Other Graph options are: graph_out.magnitude_spectrum, graph_out.specgram
    
    #graph_out.psd(samples, Fs=sdr.sample_rate / 1e6, Fc=sdr.center_freq/1e6)
    ax1.psd(samples, Fs=sdr.sample_rate / 1e6, Fc=sdr.center_freq/1e6)
    ax1.axvline(x=1420.4057517667, color='darkred', linestyle='--', linewidth=2) #xy=(447, 471)
    ax1.annotate('1420.405 MHz Hydrogen Line\nReference Frequency', xy=(585, 5), xycoords='axes points', size=14, ha='center', va='bottom', color='darkred')
    ax1.set_xlabel("Frequency (MHz)")
    ax1.set_ylabel("Relative Power")
    ax1.set_title("1420 MHz (21 cm) Hydrogen Line Spectrum")
    
    #graph_out.specgram(samples, Fs=sdr.sample_rate / 1e6, Fc=sdr.center_freq/1e6)
    ax2.specgram(samples, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6, NFFT = 1024)
    ax2.set_ylabel("Frequency (MHz)")
    ax2.set_xlabel("Time (ms)")
    ax2.set_title("Waterfall Spectrum (Dynamic)")
    
try:
    ani = animation.FuncAnimation(fig, animate, interval=50)

    plt.show()
    
except KeyboardInterrupt:
    pass
finally:
    sdr.close()

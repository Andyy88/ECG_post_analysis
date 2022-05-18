from scipy.signal import filtfilt
import scipy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

mydata = pd.read_csv("Sample12_Need_filtering.csv")
heart_rate = mydata['heart rate'].values
time_elapsed = mydata['time'].values


data = heart_rate
time = time_elapsed

def bandPassfilter(signal):
    fs = 200.0
    lowcut = 5.0
    highcut = 50.0

    nyq = 0.5*fs
    low = lowcut/nyq
    high = highcut/nyq

    order = 6

    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)
    return(y)

filtered_signal = bandPassfilter(data)

# plt.plot(time,data)
# plt.show()

plt.plot(time,filtered_signal)
plt.show()
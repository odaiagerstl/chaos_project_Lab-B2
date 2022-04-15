import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import pandas as pd
from scipy.signal import find_peaks


def saving_data():
    path = r'C:\Google One\University\Third year\Spring\LAB B2\Choas\23-Mar-22 Second week\input-9V_Smo2.csv'
    df = pd.read_csv(path)
    Time = np.array(df["Time"].tolist())
    D_Voltage = np.array(df["D_Voltage"].tolist())
    return Time, D_Voltage


def local_maximum():
    _, D_Voltage = saving_data()
    peaks, _ = find_peaks(D_Voltage, height=-0.5, distance=29000)
    print('****** \npeaks is ', peaks)
    print('****** \nx[peaks] is ', D_Voltage[peaks])
    plt.plot(D_Voltage)
    plt.plot(peaks, D_Voltage[peaks], "x")
    plt.plot(np.zeros_like(D_Voltage), "--", color="gray")
    plt.xlabel('Time')
    plt.ylabel('Diode_Voltage')
    plt.title('Diode_Voltage VS Time - Input Cur 9V_Smo2')
    plt.savefig('Input Current 9V_Smo2')
    plt.show()
local_maximum()
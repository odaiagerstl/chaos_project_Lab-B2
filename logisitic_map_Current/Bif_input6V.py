import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks, savgol_filter

import pick_everage


def saving_data(input_voltage):
    path = r'C:\Google One\University\Third year\Spring\LAB B2\Choas\30-Mar-22 Third week\input-{}V.csv'.format(input_voltage)
    df = pd.read_csv(path)
    Time = np.array(df["Time"].tolist())
    D_Voltage = np.array(df["D_Voltage"].tolist())
    return Time, D_Voltage


def local_maximum(input_voltage):
    _, D_Voltage = saving_data(input_voltage)
    D_Voltage = savgol_filter(D_Voltage, 81, 3)

    peaks, _ = find_peaks(D_Voltage, height=-0.48, distance=10000)
    # print('****** \npeaks is ', peaks)
    # print('****** \nx[peaks] is ', D_Voltage[peaks])
    plt.plot(D_Voltage)
    plt.plot(peaks, D_Voltage[peaks], "x")
    plt.plot(np.zeros_like(D_Voltage), "--", color="gray")
    plt.xlabel('Time')
    plt.ylabel('Diode_Voltage')
    plt.title('Diode_Voltage VS Time - Input Cur {}V'.format(input_voltage))
    file_name = 'Input Current {}.png'.format(input_voltage)
    #plt.savefig(file_name)
    plt.ylim([-0.6, -0.4])

    plt.show()
    return D_Voltage[peaks]

def plot_maximum():
    """
    plot the graph of Diode voltage between 0.2V to 1.6V input
    :return:
    """
    o_range = list(map(lambda x: x/10.0, range(52, 64, 2)))
    for i in o_range:
        input_voltage = str(i)
        local_maximum(input_voltage)


def maximum_number() -> dict:
    """
    count for the data of volage between 0.2 to 1.6V the number of local maximum
    :return: dict- the keys are the input values and the values are he maximum value for each of them
    """
    max_dict = dict()
    o_range = list(map(lambda x: x/10.0, range(52, 64, 2)))
    for i in o_range:
        input_voltage = str(i)
        maxi_lst = local_maximum(input_voltage)
        filtered_maximum = pick_everage.maximum_filtering(maxi_lst)
        max_dict[i] = filtered_maximum
    return max_dict


if __name__ == '__main__':
    maximum_number()



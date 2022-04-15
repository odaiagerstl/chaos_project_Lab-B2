import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

import pick_everage


def saving_data(input_voltage):
    path = r'C:\Google One\University\Third year\Spring\LAB B2\Choas\12-April-22 Fifth week\input-{}V.csv'.format(
        input_voltage)
    df = pd.read_csv(path)
    D_Voltage = np.array(df["D-Voltage"].tolist())
    return D_Voltage


def local_maximum(input_voltage):
    D_Voltage = saving_data(input_voltage)
    peaks, _ = find_peaks(D_Voltage, height=0, distance=10000)
    plt.plot(D_Voltage)
    plt.plot(peaks, D_Voltage[peaks], "x")
    plt.plot(np.zeros_like(D_Voltage), "--", color="gray")
    plt.xlabel('Time')
    plt.ylabel('Diode_Voltage')
    plt.title('Diode_Voltage VS Time - Input Cur {}V'.format(input_voltage))
    file_name = 'Input Current {}.png'.format(input_voltage)
    # plt.savefig(file_name)
    if 8.2 < float(input_voltage):
        plt.ylim(0.075, 0.16)
        plt.show()
    return D_Voltage[peaks]


def plot_maximum():
    """
    plot the graph of Diode voltage between 0.2V to 1.6V input
    :return:
    """
    o_range = list(map(lambda x: x / 10.0, range(28, 100, 2)))
    for i in o_range:
        input_voltage = str(i)
        local_maximum(input_voltage)


def maximum_number() -> dict:
    """
    count for the data of volage between 0.2 to 1.6V the number of local maximum
    :return: dict- the keys are the input values and the values are he maximum value for each of them
    """
    max_dict = dict()
    o_range1 = list(map(lambda x: x / 10.0, range(28, 100, 2)))
    o_range = o_range1 + [10]

    for i in o_range:
        input_voltage = str(i)
        maxi_lst = local_maximum(input_voltage)
        if input_voltage == '2.8':
            filtered_maximum = pick_everage.maximum_filtering(maxi_lst, 0.001)
        elif input_voltage == '3.0' or input_voltage == '3.2':
            filtered_maximum = pick_everage.maximum_filtering(maxi_lst[:-1], 0.004)
        elif 3.6 < i < 6.0:
            filtered_maximum = pick_everage.maximum_filtering(maxi_lst[:-1], 0.004)
        elif 8.6 < i <= 10:
            filtered_maximum = pick_everage.maximum_filtering(maxi_lst[:-1], 0.001)
        else:
            filtered_maximum = pick_everage.maximum_filtering(maxi_lst, 0.004)
        max_dict[i] = filtered_maximum
    return max_dict


if __name__ == '__main__':
    maximum_number()

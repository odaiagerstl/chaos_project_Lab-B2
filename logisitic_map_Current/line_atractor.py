import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks, savgol_filter

import pick_everage


def saving_data(input_voltage):
    path = r'C:\Google One\University\Third year\Spring\LAB B2\Choas\12-April-22 Fifth week\input-{}V.csv'.format(
        input_voltage)
    df = pd.read_csv(path)
    D_Voltage = np.array(df["D-Voltage"].tolist())
    return D_Voltage


def local_maximum(input_voltage, height, distance):
    """
    need to determine the hight and voltage for find peaks for each voltage value
    :param input_voltage:
    :param height:
    :param distance:
    :return:
    """
    D_Voltage = saving_data(input_voltage)
    D_Voltage = savgol_filter(D_Voltage, 81, 3)

    peaks, _ = find_peaks(D_Voltage, height=height, distance=distance)
    plt.plot(D_Voltage)
    plt.plot(peaks, D_Voltage[peaks], "x")
    plt.plot(np.zeros_like(D_Voltage), "--", color="gray")
    plt.xlabel('Time')
    plt.ylabel('Diode_Voltage')
    plt.title('Diode_Voltage VS Time - Input Cur {}V'.format(input_voltage))
    file_name = 'Input Current {}.png'.format(input_voltage)
    #plt.savefig(file_name)
    plt.show()
    return D_Voltage[peaks]


def single_attractor():
    """
    Just change the voltage
    :return:
    """
    voltage = '10'
    row_data = local_maximum(voltage, height=0, distance=10000)
    maximum_in_order = pick_everage.maximum_save_order(row_data, 0.0001)
    x = maximum_in_order[:-1]
    y = maximum_in_order[1:]
    print('X_n vector- ', x)
    print('X_n+1 vector- ', y)
    plt.plot(x, y, 'o', color='black', markersize=3)
    plt.xlabel('X_n- axis')
    plt.ylabel('X_n+1 - axis')
    plt.title('Attractor for voltage' + voltage)
    plt.show()


def many_voltage_attractor():
    o_range1 = list(map(lambda x: x / 10.0, range(78, 100, 2)))
    o_range = o_range1 + [10]
    for i in o_range:
        input_voltage = str(i)
        row_data = local_maximum(input_voltage, height=0, distance=10000)
        if input_voltage == '2.8':
            maximum_in_order = pick_everage.maximum_save_order(row_data, 0.001)
        elif input_voltage == '3.0' or input_voltage == '3.2':
            maximum_in_order = pick_everage.maximum_save_order(row_data[:-1], 0.004)
        elif input_voltage == '8.8':
            maximum_in_order = pick_everage.maximum_save_order(row_data[:-1], 0.0005)
        elif 3.6 < i < 6.0:
            maximum_in_order = pick_everage.maximum_save_order(row_data[:-1], 0.004)
        elif 8.6 < i <= 10:
            maximum_in_order = pick_everage.maximum_save_order(row_data[:-1], 0.0001)
        else:
            maximum_in_order = pick_everage.maximum_save_order(row_data, 0.004)
        #maximum_in_order = pick_everage.maximum_save_order(row_data)
        x = maximum_in_order[:-1]
        y = maximum_in_order[1:]
        plt.plot(x, y, 'o', color='black', markersize=4)
        plt.xlabel('X_n- axis')
        plt.ylabel('X_n+1 - axis')
        plt.title('Attractor for voltage' + input_voltage)
        #plt.savefig('Attractor for voltage ' + input_voltage + '.jpg')
        plt.show()


if __name__ == '__main__':
    single_attractor()
    #many_voltage_attractor()

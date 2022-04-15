import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks, savgol_filter

import pick_everage


def saving_data(input_voltage):
    path = r'C:\Google One\University\Third year\Spring\LAB B2\Choas\30-Mar-22 Third week\input-{}V.csv'.format(
        input_voltage)
    df = pd.read_csv(path)
    Time = np.array(df["Time"].tolist())
    D_Voltage = np.array(df["D_Voltage"].tolist())
    return Time, D_Voltage


def local_maximum(input_voltage, height, distance):
    """
    need to determine the hight and voltage for find peaks for each voltage value
    :param input_voltage:
    :param height:
    :param distance:
    :return:
    """
    _, D_Voltage = saving_data(input_voltage)
    D_Voltage = savgol_filter(D_Voltage, 81, 3)

    peaks, _ = find_peaks(D_Voltage, height=height, distance=distance)
    # print('****** \npeaks is ', peaks)
    # print('****** \nx[peaks] is ', D_Voltage[peaks])
    plt.plot(D_Voltage)
    plt.plot(peaks, D_Voltage[peaks], "x")
    plt.plot(np.zeros_like(D_Voltage), "--", color="gray")
    plt.xlabel('Time')
    plt.ylabel('Diode_Voltage')
    plt.title('Diode_Voltage VS Time - Input Cur {}V'.format(input_voltage))
    file_name = 'Input Current {}.png'.format(input_voltage)
    # plt.savefig(file_name)
    #plt.savefig(file_name)
    plt.show()
    return D_Voltage[peaks]


def single_attractor():
    """
    Just change the voltage
    :return:
    """
    voltage = '4.0'
    row_data = local_maximum(voltage, height=-0.48, distance=20000)
    maximum_in_order = pick_everage.maximum_save_order(row_data)
    x = maximum_in_order[:-1]
    y = maximum_in_order[1:]
    plt.plot(x, y, 'o', color='black')
    # x1 = local_maximum('8.5')[:-1]
    # y1 = local_maximum('8.5')[1:]
    # plt.plot(x1, y1,'o', color='black')
    plt.xlabel('X_n- axis')
    plt.ylabel('X_n+1 - axis')
    plt.title('Attractor for voltage' + voltage)
    plt.show()


def many_voltage_attractor():
    o_range1 = list(map(lambda x: x / 10.0, range(64, 74, 2)))
    o_range2 = list(map(lambda x: x / 10.0, range(76, 84, 4)))
    o_range3 = list(map(lambda x: x / 10.0, range(80, 100, 5)))
    o_range = o_range1 + o_range2 + o_range3 + [10]
    for i in o_range:
        input_voltage = str(i)
        row_data = local_maximum(input_voltage, height=-0.51, distance=6000)   #height=-0.51
        maximum_in_order = pick_everage.maximum_save_order(row_data)
        x = maximum_in_order[:-1]
        y = maximum_in_order[1:]
        plt.plot(x, y, 'o', color='black')
        # x1 = local_maximum('8.5')[:-1]
        # y1 = local_maximum('8.5')[1:]
        # plt.plot(x1, y1,'o', color='black')
        plt.xlabel('X_n- axis')
        plt.ylabel('X_n+1 - axis')
        plt.title('Attractor for voltage' + input_voltage)
        #plt.savefig('Attractor for voltage ' + input_voltage + '.jpg')
        plt.ylim([-0.6, -0.4])

        plt.show()


if __name__ == '__main__':
    single_attractor()
    #many_voltage_attractor()


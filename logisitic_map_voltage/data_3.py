import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import pandas as pd


def saving_data():
    path = r'C:\Google One\University\Third year\Spring\LAB B2\Choas\Diode_carcter\diode carctriztion3.csv'
    df = pd.read_csv(path)
    CH1_Time = np.array(df["CH1_Time"].tolist())
    CH1_Voltage = np.array(df["CH1_V"].tolist())
    CH2_Time = np.array(df["CH2_Time"].tolist())
    CH2_Voltage = np.array(df["CH2_V"].tolist())
    return CH1_Time, CH1_Voltage, CH2_Time, CH2_Voltage


def row_data_ch1():
    CH1_Time, CH1_Voltage, CH2_Time, CH2_Voltage = saving_data()
    print(linregress(CH1_Time, CH1_Voltage))
    plt.plot(CH1_Time, CH1_Voltage, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=8)
    plt.xlabel('Time - axis')
    plt.ylabel('CH1_Voltage - axis')
    plt.title('CH1_Voltage VS Time')
    plt.show()


def row_data_ch2():
    CH1_Time, CH1_Voltage, CH2_Time, CH2_Voltage = saving_data()
    print(linregress(CH2_Time, CH2_Voltage))
    plt.plot(CH2_Time, CH2_Voltage, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=8)
    plt.xlabel('Time - axis')
    plt.ylabel('CH2_Voltage - axis')
    plt.title('CH2_Voltage VS Time')
    plt.show()


def Diode_characteristic():
    CH1_Time, CH1_Voltage, CH2_Time, CH2_Voltage = saving_data()
    Current = CH1_Voltage / 98
    print(linregress(Current, CH2_Voltage))
    plt.plot(Current, CH2_Voltage, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=6)
    plt.xlabel('Current - axis')
    plt.ylabel('Diode_Voltage - axis')
    plt.title('Diode_Voltage VS Current')
    plt.show()


row_data_ch1()
row_data_ch2()
Diode_characteristic()

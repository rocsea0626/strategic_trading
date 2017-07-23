import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def run(threshold, show_plot=False):
    df = pd.read_csv('data/20150429_SZ300276.csv', parse_dates=True, infer_datetime_format=True)
    time_arr = df[['Time']].values
    end_time = 100000

    time_idx = getTimeIndex(time_arr, end_time)
    data = df.loc[0:time_idx, ['Close']]

    plot(data, show_plot)
    return (data.iloc[-1] - data.iloc[0]) / data.iloc[0] >= threshold


def getTimeIndex(time_arr, time):
    return np.where(time_arr == time)[0][0]


def plot(data, show_plot):
    if (show_plot):
        ax = data.plot(title="20140905_SH600018", label='Real price')

        ax.set_xlabel("Time")
        ax.set_ylabel("Price, (RMB)")
        ax.legend(loc='upper left')
        plt.show()
    return


if __name__ == "__main__":
    run()

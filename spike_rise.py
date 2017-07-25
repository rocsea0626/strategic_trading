import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def run(fname, threshold, little=True, show_plot=False):

    df = pd.read_csv(fname, parse_dates=True, infer_datetime_format=True)
    pd.set_option('precision', 2)
    pd.set_option('chop_threshold', 0)

    start_time = end_time = 0

    time_arr = df[['Time']].values
    if (little==True):
        start_time = time_arr[0][0]
        end_time = 100000
    else:
        end_time = time_arr[-1][0]
        start_time = 130000



    start_time_idx = getTimeIndex(time_arr, start_time)
    end_time_idx = getTimeIndex(time_arr, end_time)
    print(start_time_idx)
    print(end_time_idx)

    data = df.loc[start_time_idx:end_time_idx, ['Close']]
    rmd = data.rolling(window=5).mean()

    nrows = rmd.shape[0]

    arr_indices = []

    for i in range(1, nrows - 1):
        lrmd = rmd.iloc[i - 1, 0]
        rrmd = rmd.iloc[i + 1, 0]
        if(rmd.iloc[i, 0] > lrmd and rmd.iloc[i, 0] >= rrmd):
            arr_indices.append(start_time_idx+i)
            print(rmd.iloc[i, 0])

    irmd = (rmd.fillna(0)*1000).astype(int)
    first_max_idx = irmd.idxmax(axis=0)
    print(rmd.iloc[first_max_idx-start_time_idx,0] - rmd.iloc[5,0])

    plot(data, rmd, arr_indices, show_plot)

    # return (data.iloc[-1] - data.iloc[0]) / data.iloc[0] >= threshold


def getTimeIndex(time_arr, time):
    return np.where(time_arr == time)[0][0]


def plot(data, rmd, arr_indices, show_plot):
    if (show_plot):
        ax = data.plot(title="20140905_SH600018", label='Real price (RMB)')
        rmd.plot(label="rolling mean", ax=ax)

        for xc in arr_indices:
            ax.axvline(x=xc)

        ax.set_xlabel("Time")
        ax.set_ylabel("Price, (RMB)")
        ax.legend(loc='upper left')

        plt.show()
    return


if __name__ == "__main__":
    # run('data/20150429_SZ300276.csv', 0.08, little=False, show_plot=True)
    result = run('data/20150526_SZ002592.csv', 0.07, little=False, show_plot=True)
    print("result=", result)

import pandas as pd
import matplotlib.pyplot as plt

def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    upper_band = rm+2*rstd
    lower_band= rm -2*rstd
    return upper_band, lower_band


def test_run():
    df = pd.read_csv('../data/20140905_SH600018.csv', index_col=['Time'], parse_dates=True, infer_datetime_format=True)
    data = df[['Close']]
    rm_data = data.rolling(window=20).mean()
    rstd_data = data.rolling(window=20).std()
    upper_band, lower_band = get_bollinger_bands(rm_data, rstd_data)

    ax = data.plot(title="20140905_SH600018", label='Price')
    rm_data.plot(label="rolling mean", ax=ax)
    upper_band.plot(label="upper band", ax=ax)
    lower_band.plot(label="lower band", ax=ax)

    ax.set_xlabel("Time")
    ax.set_ylabel("Price, (RMB)")
    ax.legend(loc='upper left')
    plt.show()



if __name__ == "__main__":
    test_run()

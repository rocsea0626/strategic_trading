import spike_rise_little as srl

def run():
    is_rising_spike = srl.run(threshold=0.07, show_plot=True)
    print(is_rising_spike)


if __name__ == "__main__":
    run()
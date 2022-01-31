def MA(series, period=5):
    """Calculate moving average with period 5 as default """
    i = 0
    moving_averages = []
    while i < len(numbers) - period + 1:
        this_window = numbers[i: i + period]
    window_average = sum(this_window) / period
    moving_averages.append(window_average)
    i += 1


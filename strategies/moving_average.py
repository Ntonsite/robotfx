import pandas as pd

def calculate_sma(prices, window):
    return pd.Series(prices).rolling(window=window).mean().iloc[-1]

def check_signal(prices):
    sma_short = calculate_sma(prices, 5)
    sma_long = calculate_sma(prices, 20)
    if sma_short > sma_long:
        return "buy"
    elif sma_short < sma_long:
        return "sell"
    else:
        return "hold"

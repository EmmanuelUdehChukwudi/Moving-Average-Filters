# Moving-Average-Filters

# Simple Moving Average (SMA) Filter

## Overview

The Simple Moving Average (SMA) filter is a fundamental technique in signal processing and time series analysis. It is used to smooth out short-term fluctuations and highlight longer-term trends or cycles in data. This README provides an overview of SMA filters, their implementation, and considerations when using them.

## What is SMA?

The Simple Moving Average (SMA) is computed by taking the arithmetic mean of a set of values over a specified window of time or space. It is a linear filter that evenly weights all data points within the window.

### Advantages

- **Simplicity**: Easy to understand and implement.
- **Noise Reduction**: Effective in smoothing out noise and short-term fluctuations.
- **Preservation of Trends**: Maintains the overall trend of the data while reducing noise.

### Limitations

- **Lag**: SMA introduces a lag between the filtered output and the original data due to its averaging nature.
- **Less Effective for Non-Stationary Data**: Performs best on stationary data; less effective with data containing trends or seasonality.
- **Window Size Selection**: The choice of window size affects the trade-off between noise reduction and responsiveness to changes.


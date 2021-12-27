# Air-Quality-Forecasting

This repository contains a series of analysis, transforms and forecasting models frequently used when dealing with time series. The aim of this repository is to showcase how to model time series from the scratch, for this we are using a real usecase dataset

# Dataset

This dataset contains yearly Co2 emmisions levels. data from 1800 to 2014 sampled every 1 year. The dataset is non stationary so we have to use differenced time series for forecasting.

# Analysis and transforms

  * Time series decomposition
    Level
    Trend
    Seasonality
    Noise
    Stationarity

  * AC and PAC plots
    Rolling mean and std
    Dickey-Fuller test
    Making our time series stationary

  * Difference transform
    Log scale
    Smoothing
    Moving average
    
# Models tested

  * Autoregression (AR)
  * Moving Average (MA)
  * Holt's smoothing technique
  * Autoregressive integraded moving average (ARIMA)
  * Auto ARIMA
  * Linear Regression
  * Ridge Regression
  * Lasso Regression
  * Lgbm
  * Xgboost
  * fbprophet
  * LSTM

# Forecasting Results
## Evaluation Metrics
[project81-G5 PPT.pptx](https://github.com/shivanipadaya/Air-Quality-Forecasting/files/7779525/project81-G5.PPT.pptx)

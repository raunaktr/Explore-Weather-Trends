# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:57:53 2017

@author: Raunak
"""

import pandas as pd
import matplotlib.pyplot as plt

temp = pd.read_csv("city_analysis.csv")

def MeanFunction(check, input):
    output = input.rolling(window = check, center=False, on = "year").mean().dropna()
    return output

average_span = 7
moving_avg = MeanFunction(average_span, temp)

plt.plot(moving_avg['year'], moving_avg['london_avg_temp'], label='London')
plt.plot(moving_avg['year'], moving_avg['dublin_avg_temp'], label='Dublin')
plt.plot(moving_avg['year'], moving_avg['global_avg_temp'], label='Global')
plt.legend()
plt.xlabel("Year (C.E.)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in London verus Dublin versus Global values ({} year moving average)".format(average_span))
plt.show()
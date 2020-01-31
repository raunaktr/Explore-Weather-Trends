# Explore Weather Trends!

Current predictions of climate change may significantly underestimate the speed and severity of global warming. Many changes have been unprecedented over the years and continuing to an exponential extent. In this report we will analyze the database obtained from the udacity’s workspace. We will also learn about working with tables and plotting a Moving Average Line chart using tools such as **SQL** and **Python**.

Comparing London’s and Dublin’s average temperature with the Global average temperature, sounds fun, lets get on with it.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

## Prerequisites

Understanding of Python and MySQL required. What things you need to install the software and how to install them.

 1. Python3 [Click here](https://www.python.org/downloads/) to redirect to Python installation page.
 2. MYSQL [Click here](https://www.mysql.com/downloads/) to redirect to MYSQL installation page.
 3. Jupyter Notebook [Click here](https://jupyter.org/install) to redirect to MYSQL installation page.
 
 - Pandas [Click here](https://matplotlib.org/) to redirect to MYSQL installation page.
 - Matplotlib ([Click here](https://matplotlib.org/)) to redirect to Matplotlib installation page.

## Dependencies
**INSTALLATION**
### Spyder
Resource -> ([https://docs.spyder-ide.org/installation.html](https://docs.spyder-ide.org/installation.html)) 

**Install on GNU/Linux**

Please refer to the  [Requirements](https://docs.spyder-ide.org/installation.html#requirements)  to see what other packages you might need.

    sudo apt install spyder3
    
  **Install on Arch Linux**
  Install on arch using AUR package [here](https://aur.archlinux.org/packages/spyder3-git/)

**Install on Fedora**
Install on Fedora. Refer [here](https://fedoraproject.org/wiki/Spyder)

    sudo dnf install python3-spyder
### Matplotlib
Matplotlib and its dependencies are available as wheel packages for macOS, Windows and Linux distributions:

    python -m pip install -U pip
    python -m pip install -U matplotlib

### Pandas

**pandas** is a Python package providing fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time series data both easy and intuitive.

    pip install pandas

Now lets jump into the next section

# Code
### MYSQL
The CSV fies were extracted using the Udacity’s native SQL Workspace:

    SELECT ∗ FROM city data;
    
 

   Joining and creating a columns
  
      ALTER TABLE
        global data RENAME COLUMN
        avg temp to global avg temp;
   
      ALTER TABLE
        city data RENAM E COLUMN
        avg temp to london avg temp;
      
      ALTER TABLE
        city data ADD COLUMN
        dublin avg temp;
        
   

 Now creating a inner join such that the created table can
    be used for plotting Moving Average line chart.
    
    SELECT global data.year,
    global data.global avg temp, london avg temp
    FROM global data INNER JOIN
    city data ON global data.year = city data.year
    WHERE city like 'London';
    
Export your file to CSV. 


## CSV Analysis using Pandas

To accomplish the task of plotting the line chart using pandas for correlation of data from the table and and declaring a function such that different moving averages can be calculated with ease. 
*dropna()* from Pandas module is used to reduce the noise from the CSV file.

    import pandas as pd
    import matplotlib.pyplot as plt
    
    temp = pd.read_csv("city_analysis.csv")
    
    def MeanFunction(check, input):
        output = input.rolling(window = check, center=False, on = "year").mean().dropna()
        return output
   

**Moving Average** is  calculated only after cleaning the CSV files from error to avoid sudden fluctuations in the line chart.
  
 
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


## Graphs 

It is clearly seen that the average temperature have been rising ever since the temperature were being recorded. Global warming to be blamed on this part. 

A 10 year moving Average was taken because it provided a better understanding of the line chart and gave wide range of values where the comparison can be made.

![10 year Moving Average Comparison between London, Dublin and Global](https://github.com/raunaktr/Explore-Weather-Trends/blob/master/exploring-weather-trends/10years.png?raw=true) 

Similarly, 50 years moving Average of London’s versus Dublin’s versus global average temperature as shown in below in line chart.

![50 year Moving Average Comparison between London, Dublin and Global](https://github.com/raunaktr/Explore-Weather-Trends/blob/master/exploring-weather-trends/50years.png?raw=true)

## Analysis
The overall trends tends to give us an idea that *global warming* a very serious issue and it should be taken care of. 

The trends from 1950-present has seen drastic change in terms of global average temperature as well as London’s and Dublin’s average temperature.
The world is getting hotter place to live in. The temperature gives us an idea that these figure will increase exponentially until several strict measures are not taken into account.
The trend has been consistently increasing with each passing decade and will increase or the *climate change* will soon plunder the planet
### Contributors

 **Raunak Tripathi** <br>
  Feel free to reach me @ [Linkedin](https://www.linkedin.com/in/reachtoraunak/)

###  Acknowledgments

 1. [https://pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/)
 2. [https://matplotlib.org/contents.html#](https://matplotlib.org/contents.html)
 3. [https://www.python.org/doc/](https://www.python.org/doc/)
 


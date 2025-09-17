import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    # First of all, we select the X value to be the Year column and the Y value to the CSIRO Adjusted Sea Level column
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # This series was created to make the line of best fit go through 2050. It starts with a range from 1880 (the start of the dataset) till the desired year.
    years_prev = pd.Series(range(1880, 2051))

    # This creates the scatterplot with the years and sea level values
    plt.scatter(x, y)

    # Create first line of best fit and make it go through 2050 (the original data only goes till 2020)
    linearReg = linregress(x, y)

    # Now we plot the line of best fit
    # It uses the range of years from 1880 till 2025 as the X value
    # For the Y value, it uses the formula for finding the best fit, which is the slope times the X value plus the intercept
    plt.plot(years_prev, linearReg.slope * years_prev + linearReg.intercept, color='r')


    # Create second line of best fit
    
    # For the second line of best fit, we select only the data from the year 2000 till 2050
    newX = df['Year'][df['Year'] >= 2000]
    newY = df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000]

    # Now we make a new series, this time from 2000 till 2050
    years_prev2 = pd.Series(range(2000, 2051))

    # We do a second linear regression with the new data
    linearReg2 = linregress(newX, newY)

    # We do the same plot as before, but this time with the new data and the new series
    plt.plot(years_prev2, linearReg2.slope * years_prev2 + linearReg2.intercept, color='g')

    # Add labels and title

    # Adding the new labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()